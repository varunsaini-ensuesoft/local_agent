from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key="AIzaSyAtbpsK6acCNYKxsoglQOkfJ3IEpchfjgk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT

response = client.chat.completions.create(
    model="gemini-2.5-flash", messages=[
        {"role": "user", "content": PROMPT.format(text="Provide me the python code i dont wnat conversions")}
    ])

print(response.choices[0].message.content)