from groq import Groq

import streamlit as st

API_KEY = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=API_KEY)


def ask_pdf_question(
    pdf_text,
    user_question
):

    pdf_text = pdf_text[:10000]

    prompt = f"""
Study Material:

{pdf_text}

Question:

{user_question}

Instructions:

1. Answer ONLY from the study material.
2. If answer is not found, say:
   'Answer not found in uploaded material.'
3. Explain clearly.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content":
                "You are a PDF learning assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content