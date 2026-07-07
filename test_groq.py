from groq import Groq
import json
import streamlit as st

API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Say Hello"}
    ]
)

print(response.choices[0].message.content)