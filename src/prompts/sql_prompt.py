def sql_prompt(question, schema):
    return f"""
You are an expert SQL generator.

Database schema:
{schema}

User question:
{question}


Generate ONLY valid SQL query.
"""
