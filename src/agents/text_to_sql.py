from langgraph.graph import StateGraph, START, END
from src.agents.state import SQLAgentState
from src.agents.nodes import execute_sql, generate_sql, validate_sql, generate_answer

graph = StateGraph(SQLAgentState)

graph.add_node("execute", execute_sql)
graph.add_node("validate", validate_sql)
graph.add_node("generate", generate_sql)
graph.add_node("generate_ans", generate_answer)

graph.add_edge(START, "generate")
graph.add_edge("generate", "execute")
graph.add_edge("execute", "generate_ans")
graph.add_edge("generate_ans", END)

sql_agent = graph.compile()