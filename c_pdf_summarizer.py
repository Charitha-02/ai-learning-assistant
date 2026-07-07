from pypdf import PdfReader
from groq import Groq

import streamlit as st
API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)


from pypdf import PdfReader

def extract_text_from_pdf(pdf_file):

    pdf_file.seek(0)

    try:
        reader = PdfReader(pdf_file)

        text = ""

        for page_number, page in enumerate(reader.pages):

            page_text = page.extract_text()

            print(f"Page {page_number+1}: {len(page_text) if page_text else 0} characters")

            if page_text:
                text += page_text + "\n"

        print("Total Extracted Characters:", len(text))

        return text.strip()

    except Exception as e:

        print("PDF Extraction Error:", e)

        return ""

def summarize_pdf(text):

    if not text or len(text.strip()) == 0:
        return "❌ No readable text found in this PDF."

    text = text[:6000]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
Summarize the study material.

Include:
1. Important Concepts
2. Key Points
3. Short Notes

Use simple student-friendly language.
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content


def generate_short_notes(text):

    text = text[:6000]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
Generate concise short notes.

Requirements:
1. Important concepts only
2. Easy to revise
3. Exam-oriented
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content


def generate_revision_notes(text):

    text = text[:6000]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
Generate one-day-before-exam revision notes.

Include:
- Key concepts
- Definitions
- Important formulas
- Quick revision points
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content


def generate_important_questions(text):

    text = text[:6000]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
Generate important exam questions.

Include:
1. Short Answer Questions
2. Long Answer Questions
3. Frequently Asked Questions
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.choices[0].message.content
def generate_detailed_explanation(text):

    if not text or len(text.strip()) == 0:
        return "❌ No readable text found."

    text = text[:6000]

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role": "system",
                "content": """
Explain this study material like an experienced professor.

Requirements:

1. Explain every topic clearly.

2. Use simple student-friendly language.

3. Give examples wherever possible.

4. Explain definitions.

5. Explain diagrams if mentioned.

6. Explain formulas.

7. Highlight important exam points.

8. Make the explanation easy for beginners.

"""
            },

            {
                "role": "user",
                "content": text
            }

        ]

    )

    return response.choices[0].message.content
def generate_detailed_explanation(text):

    if not text or len(text.strip()) == 0:
        return "❌ No readable text found."

    text = text[:6000]

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": """
Explain this study material in detail.

Requirements:

1. Explain every topic.
2. Use simple language.
3. Give examples.
4. Explain definitions.
5. Explain formulas.
6. Highlight important exam points.
7. Make it beginner friendly.
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]

    )
    return response.choices[0].message.content