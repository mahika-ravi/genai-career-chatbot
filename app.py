import streamlit as st
from prompts import build_prompt
from utils import call_llm_api, load_jds
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="GenAI Career Chatbot")

st.title("🤖 GenAI Career Advisor Chatbot")

resume_input = st.text_area("Paste your resume summary here", height=200)

if st.button("Match Me!"):
    if not resume_input.strip():
        st.warning("Please paste your resume.")
    else:
        jds = load_jds()
        prompt = build_prompt(resume_input, jds)
        result = call_llm_api(prompt)
        st.markdown("### 🔍 Matching Internships:")
        st.write(result)
