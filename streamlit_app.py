import streamlit as st
from src.app.agent_runner import run_text_to_sql

import os
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]


st.set_page_config(page_title="Text to SQL Agent", layout="centered")

st.title("🧠 Text to SQL Agent")
st.write("Ask a question in natural language")

# Input box
question = st.text_input("Enter your question:")

# Button
if st.button("Run Query"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            result = run_text_to_sql(question)

        st.success("Query executed successfully")

        # Display outputs
        st.subheader("🔹 Question")
        st.code(result["question"])

        st.subheader("🔹 Generated SQL")
        st.code(result["sql_query"], language="sql")

        st.subheader("🔹 Validated SQL Query")
        st.code(result["validated_sql"], language="sql")

        st.subheader("🔹 Result")
        st.text(result["final_answer"])
