def sql_validation_prompt(schema: str, sql_query: str):
    return f"""
You are a SQL expert.

Given:
1. Database schema
2. A generated SQL query

Tasks:
- Remove markdown formatting (```sql)
- Fix invalid table or column names using schema
- Ensure SQL is syntactically valid
- Do NOT add explanations
- Return ONLY the corrected SQL

Schema:
{schema}

SQL Query:
{sql_query}
"""
