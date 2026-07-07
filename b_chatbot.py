from groq import Groq

import streamlit as st
API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)

def get_ai_response(user_question):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI tutor for students."
            },
            {
                "role": "user",
                "content": user_question
            }
        ]
    )

    return response.choices[0].message.content