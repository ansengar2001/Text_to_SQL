from src.LLM import llm_client
from src.prompts.sql_prompt import sql_prompt

def generate_sql(state):
    prompt = sql_prompt(state["question"], state["schema"])

    response = llm_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    state["sql_query"] = response.choices[0].message.content
    return state


def validate_sql(state):
    if "select" not in state["sql_query"].lower():
        state["error"] = "Invalid SQL"
    return state


from sqlalchemy import text
from src.database.configure_sqllite import db

def execute_sql(state):
    sql = state["sql_query"]

    # Remove markdown formatting if present
    sql = sql.replace("```sql", "").replace("```", "").strip()

    state["sql_query"] = sql
    state["sql_result"] = db.run(sql)

    return state



from tabulate import tabulate
import ast

def generate_answer(state: dict):
    result = state["sql_result"]

    # Handle empty result
    if not result or result.strip() == "":
        state["final_answer"] = "No records found."
        return state

    # Convert string → Python object
    rows = ast.literal_eval(result)

    if not rows:
        state["final_answer"] = "No records found."
        return state

    table = tabulate(rows, tablefmt="grid")
    state["final_answer"] = table
    return state
