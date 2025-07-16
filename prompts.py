def build_prompt(resume, job_descriptions):
    jd_block = "\n".join([f"{i+1}. {jd}" for i, jd in enumerate(job_descriptions)])
    return f"""
You are a career advisor AI.

Given this resume:
\"\"\"{resume}\"\"\"

And these job descriptions:
{jd_block}

Suggest the top 2 matching roles, explain why, and recommend 1 upskilling tip.
"""
