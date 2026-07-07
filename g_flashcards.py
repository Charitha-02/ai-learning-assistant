from groq import Groq

import streamlit as st

API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)


def generate_flashcards(text):

    text = text[:6000]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
Generate study flashcards.

Format:

Q: Question

A: Answer

Generate at least 15 flashcards.

Cover all important topics.

Keep answers concise.
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content