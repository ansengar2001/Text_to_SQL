from src.agents.text_to_sql import sql_agent
from src.database.schema import get_schema

def run_text_to_sql(question: str):
    state = {
        "question": question,
        "schema": get_schema()
    }

    result = sql_agent.invoke(state)

    return {
        "question": question,
        "sql_query": result.get("sql_query", ""),
        "final_answer": result.get("final_answer", "")
    }
