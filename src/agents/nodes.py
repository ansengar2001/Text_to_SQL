from src.LLM import llm_client
from src.prompts.sql_prompt import sql_prompt
from src.prompts.sql_validation_prompt import sql_validation_prompt

def generate_sql(state):
    prompt = sql_prompt(state["question"], state["schema"])

    response = llm_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    state["sql_query"] = response.choices[0].message.content
    return state


def validate_sql(state):
    prompt = sql_validation_prompt(
        schema=state["schema"],
        sql_query=state["sql_query"]
    )

    response = llm_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You validate and fix SQL queries."},
            {"role": "user", "content": prompt}
        ]
    )

    cleaned_sql = response.choices[0].message.content.strip()

    # Safety: remove accidental markdown remnants
    cleaned_sql = cleaned_sql.replace("```sql", "").replace("```", "").strip()

    state["validated_sql"] = cleaned_sql
    return state


from sqlalchemy import text
from src.database.configure_sqllite import db

def execute_sql(state):
    sql = state["validated_sql"]

    # Remove markdown formatting if present
    sql = sql.replace("```sql", "").replace("```", "").strip()

    
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
