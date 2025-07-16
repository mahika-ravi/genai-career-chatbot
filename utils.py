import json

def load_jds():
    with open("jd_sample.json", "r") as f:
        return json.load(f)

def call_llm_api(prompt):
    # 👇 Mocked response for development (NO API call)
    return """### 🔍 Matching Internships:

1. **Data Science Intern at Flipkart** – Your Python and SQL skills align perfectly with this role.

2. **Analytics Intern at BCG** – Your experience with dashboards in Power BI/Tableau makes you a great fit.

🧠 Tip: Consider improving your deployment skills with Streamlit or Flask for bonus points!
"""
