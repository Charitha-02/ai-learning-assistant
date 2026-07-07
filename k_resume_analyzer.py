from pypdf import PdfReader
from groq import Groq

import streamlit as st
API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)


def extract_resume_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def analyze_resume(resume_text):

    resume_text = resume_text[:8000]

    prompt = f"""
Analyze this resume.

Resume:

{resume_text}

Return in the following format:

Resume Score: XX/100

Skills Found:
- skill1
- skill2

Missing Skills:
- skill1
- skill2

Strengths:
- point1
- point2

Weaknesses:
- point1
- point2

Suggested Certifications:
- cert1
- cert2

Recommended Career Roles:
- role1
- role2

Placement Readiness:
Ready / Almost Ready / Needs Improvement

Keep the response concise and dashboard-friendly.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert resume reviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
import re

def extract_resume_score(result):

    match = re.search(
        r'(\d+)\s*/\s*100',
        result
    )

    if match:

        return int(
            match.group(1)
        )

    return 50
import re

def extract_resume_score(result):

    match = re.search(
        r'(\d+)\s*/\s*100',
        result
    )

    if match:
        return int(match.group(1))

    return 50