import json
import openai
import os

def load_jds():
    with open("jd_sample.json", "r") as f:
        return json.load(f)

def call_llm_api(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
