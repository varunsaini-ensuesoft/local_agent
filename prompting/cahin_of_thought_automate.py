from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()

client = OpenAI(
    api_key="AIzaSyAtbpsK6acCNYKxsoglQOkfJ3IEpchfjgk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """ 
    You're an expert in resolving user queries using chain of thought.
    You work on START, PLAN, and OUTPUT steps.
    You need to first plan what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    RULES:
    - Strictly follow the JSON output format:
    - Only run one step at a time.
    - The sequence of steps are START (where user gives input), PLAN (That can be multiple times) and Finally OUTPUT (where you give final answer).
    
    OUTPUT format:
    {
        "step": "START" | "PLAN" | "OUTPUT",
        "content: "string"
    }
    
    Example:
    START: Hey, can you solve 2+3*5/10 for me?
    PLAN: {"step": "START", "content": "Seems like user is intrested in solving a math problem"}
    PLAN: {"step": "START", "content": "Looking at the problem, we shoudl solve this using bodmas method"}
    PLAN: {"step": "START", "content": "Looking at the problem, we shoudl solve this using bodmas method"}
    PLAN: {"step": "OUTPUT", "content": "Great, we have solved the problem, the answer is 3.5"}
"""
print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("👉 ")
message_history.append({"role":"user", "content": user_query})
while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type":"json_object"},
        messages=message_history
        )
    
    raw_result = response.choices[0].message.content
    parsed_result = json.loads(raw_result)
    message_history.append({"role":"assistant", "content": raw_result})
    
    if parsed_result['step'] == "START":
        print("🔥 ", parsed_result.get("content"))
        continue
    elif parsed_result['step'] == "PLAN":
        print("📝 ", parsed_result.get("content"))
        continue
    elif parsed_result['step'] == "OUTPUT":
        print("✅", parsed_result.get("content"))
        break
    
    
print("\n\n\n")