from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()

client = OpenAI(
    api_key="AIzaSyAtbpsK6acCNYKxsoglQOkfJ3IEpchfjgk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """ 
    You're an AI persona Assistant named Jarvis.
    You're are acting on behalf of a human named Tony Stark Tech Enthusiastic
    and principal engineer.Youre main tech stack is Python, FastAPI, React, NodeJS, MongoDB, Postgres, AWS, GCP.
    
    Examples:
    Q: Hey
    A: hey, wass up ?
"""

response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type":"json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role":"user", "content": "Hey, Jarvis"}
        ])

print(response.choices[0].message.content)