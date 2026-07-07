from groq import Groq

import streamlit as st
API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=API_KEY)


def generate_career_guidance(
    strong_topics,
    weak_topics,
    goal
):

    prompt = f"""
Strong Topics:
{strong_topics}

Weak Topics:
{weak_topics}

Student Goal:
{goal}

Suggest:

1. Suitable Career Paths
2. Recommended Certifications
3. Skills To Learn
4. Improvement Areas
5. Future Learning Roadmap
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert career counselor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content