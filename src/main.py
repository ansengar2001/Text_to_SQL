from src.agents.text_to_sql import sql_agent
from src.database.schema import get_schema

# question = "List all customers which have the +1 country code"
question = "List all the tables "

state = {
    "question": question,
    "schema": get_schema()
}

result = sql_agent.invoke(state)

print("Question::::::::::::::::::::::::::::::::::\n\n")
print(result["question"])

print("sql_query::::::::::::::::::::::::::::::::::\n\n")
print(result["sql_query"])


print("sql_result::::::::::::::::::::::::::::::::::")
print(result["sql_result"])


print("Final_Answer::::::::::::::::::::::::::::::::::")
print(result["final_answer"])