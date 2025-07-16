import json

def load_jds():
    with open("jd_sample.json", "r") as f:
        return json.load(f)

def call_llm_api(resume_text):
    resume_text = resume_text.lower()

    # ✅ Expanded skills from Prerana's resume and common tech
    skills = {
        "python": "Python",
        "sql": "SQL",
        "flask": "Flask",
        "cloud": "Cloud Computing",
        "machine learning": "Machine Learning",
        "data analyst": "Data Analyst",
        "chatbot": "Chatbot Development",
        "cybersecurity": "Cybersecurity",
        "gcp": "Google Cloud",
        "blender": "Blender",
        "photoshop": "Photoshop",
        "ai": "Artificial Intelligence",
        "creative": "Creative Tools",
        "communication": "Communication",
        "springboard": "Infosys Springboard",
        "design": "Design",
    }

    # Load job descriptions
    jds = load_jds()
    matches = []

    for jd in jds:
        jd_lower = jd.lower()
        score = 0
        explanation = []
        for kw in skills:
            if kw in resume_text and kw in jd_lower:
                score += 1
                explanation.append(f"✔️ Matched skill: {skills[kw]}")
        matches.append((score, jd, explanation))

    # Sort by best match
    matches.sort(reverse=True, key=lambda x: x[0])
    top_matches = matches[:2]

    # Format results
    result = "### 🔍 Top Matching Internships:\n\n"
    for idx, (score, jd, explanation) in enumerate(top_matches, 1):
        result += f"{idx}. **{jd}**\n"
        if explanation:
            result += "\n".join(explanation)
        else:
            result += "❓ No strong keyword matches found."
        result += "\n\n"

    result += "🧠 Tip: Add more technical details or relevant tools to improve your matches!\n"
    return result
