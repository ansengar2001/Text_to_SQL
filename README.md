# 🧠 Text-to-SQL Agent (LangGraph + Streamlit)

A production-ready **Text-to-SQL AI Agent** that converts natural language questions into SQL queries, executes them on a relational database, and returns human-readable results.

This project is built using **LangGraph**, **LangChain**, **OpenAI**, **SQLAlchemy**, and **Streamlit**, following the official LangGraph SQL Agent design.

---

## 🚀 Features

* 🔹 Natural language → SQL query generation
* 🔹 Schema-aware SQL generation
* 🔹 Safe SQL execution via LangChain `SQLDatabase`
* 🔹 Result formatting (tabular text output)
* 🔹 Interactive Streamlit UI
* 🔹 Secure API key handling (no hardcoding)
* 🔹 Free deployment using Streamlit Community Cloud

---

## 🏗️ Architecture Overview

```
User Question
     ↓
[ load_schema node ]
     ↓
[ generate_sql node ]
     ↓
[ execute_sql node ]
     ↓
[ generate_answer node ]
     ↓
Final Response (UI)
```

The agent is implemented as a **LangGraph state machine**, where each node explicitly reads and writes to a shared state.

---

## 📁 Project Structure

```
Text_to_SQL/
│
├── streamlit_app.py        # Streamlit frontend (entry point)
├── requirements.txt        # Python dependencies
├── src/
│   ├── agents/
│   │   ├── graph.py        # LangGraph workflow
│   │   └── nodes.py        # Agent nodes
│   │
│   ├── database/
│   │   └── db.py           # SQLDatabase configuration
│   │
│   ├── app/
│   │   └── agent_runner.py # Graph invocation wrapper
│   │
│   └── LLM.py              # Centralized LLM configuration
│

```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv virtual_env
source virtual_env/bin/activate   # Linux / Mac
virtual_env\Scripts\activate      # Windows
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure OpenAI API Key (Local)

Create the file:

```
.streamlit/secrets.toml
```

Add:

```toml
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxx"
```


### 4️⃣ Run the Application Locally

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Example Usage

**Input:**

```
Show all users created last month
```

**Generated SQL:**

```sql
SELECT * FROM Customer ...
```

**Output:**

```
1 | John Doe | USA
2 | Alice | Canada
```


## 👤 Author

**Anshul Sengar**
AI / GenAI Engineer

---

## 📄 License
This project is intended for educational and demonstration purposes.
