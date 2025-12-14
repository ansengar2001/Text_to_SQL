from typing import TypedDict, List, Any

class SQLAgentState(TypedDict):
    question: str          # User input
    schema: List[str]      # Selected DB tables
    sql_query: str         # Generated SQL
    sql_result: Any        # Output of SQL execution
    final_answer: str      # Final LLM answer
    error: str             # error in vadilation
