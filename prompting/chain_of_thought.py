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

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type":"json_object"},
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role":"user", "content": "Can you help me with solving 2+3*5/10 ?"},
        # Manually add the messages to the History
        {"role":"assistant", "content": json.dumps({
            "step": "START",
            "content": "I can help you solve the mathematical expression 2+3*5/10."}
        )},
        
        {"role":"assistant", "content": json.dumps({
        "step": "PLAN",
        "content": "First, I need to identify the operations in the expression: addition, multiplication, and division. I will apply the order of operations (PEMDAS/BODMAS) to solve it."
        })},
        
        {"role":"assistant", "content": json.dumps({
        "step": "PLAN",
        "content": "First, I will identify the mathematical operations in the expression. Then, I will apply the order of operations (BODMAS/PEMDAS) to solve the expression: Multiplication and Division take precedence over Addition. Within multiplication and division, I will solve from left to right. Finally, I will perform the addition."
        })},
        
        {"role":"assistant", "content": json.dumps({
        "step": "PLAN",
        "content": "First, I will identify the mathematical operations in the expression. Then, I will apply the order of operations (BODMAS/PEMDAS) to solve the expression: Multiplication and Division take precedence over Addition. Within multiplication and division, I will solve from left to right. Finally, I will perform the addition."
        })},
        
        {"role":"assistant", "content": json.dumps(
        {
        "step": "PLAN",
        "content": "Following the BODMAS/PEMDAS rule, first, I will perform the multiplication: 3 * 5 = 15. Next, I will perform the division: 15 / 10 = 1.5. Finally, I will perform the addition: 2 + 1.5."
        })},
        {"role":"assistant", "content": json.dumps({
        "step": "PLAN",
        "content": "Performing the final addition: 2 + 1.5 = 3.5. The expression is now fully evaluated."
        })},
        
        ])

print(response.choices[0].message.content)