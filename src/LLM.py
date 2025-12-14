from openai import OpenAI
import os

llm_client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)


print("API KEY FOUND:", bool(os.getenv("OPENAI_API_KEY")))

