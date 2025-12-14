from src import LLM

response = LLM.llm_client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system","content":"You are the asssitant of me"},
        {"role": "user","content":"Hi GPT, Just testing"}
    ]
)


print(response.choices[0].message.content)