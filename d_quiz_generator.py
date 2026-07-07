from groq import Groq
import json
import streamlit as st

API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)


def generate_quiz(text, difficulty="Medium"):

    text = text[:8000]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"""
You are an expert teacher.

Generate a quiz from the study material.

Difficulty Level:
{difficulty}

Easy:
- Basic concepts
- Definitions
- Simple questions

Medium:
- Conceptual questions
- Understanding-based questions

Hard:
- Application-based questions
- Analytical questions
- Problem-solving questions

IMPORTANT:

Return ONLY valid JSON.

Generate exactly 10 questions.

Each question must contain:

topic
difficulty
question
options
correct_answer
explanation

Example:

[
    {{
        "topic":"Normalization",
        "difficulty":"{difficulty}",
        "question":"What is First Normal Form?",
        "options":[
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "correct_answer":"Option B",
        "explanation":"Explanation here"
    }}
]

Rules:

1. Cover all important topics.
2. Use the selected difficulty level.
3. Return ONLY JSON.
4. No markdown.
5. No code blocks.
6. No extra text.
"""
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    content = response.choices[0].message.content

    try:

        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        quiz_data = json.loads(content)

        if isinstance(quiz_data, list):
            return quiz_data

        return []

    except Exception as e:

        print("Quiz Parsing Error:", e)
        print(content)

        return []
def generate_topic_quiz(topic, difficulty="Medium"):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"""
You are an expert teacher.

Generate exactly 10 MCQ questions.

Topic:
{topic}

Difficulty:
{difficulty}

Return ONLY valid JSON.

Format:

[
    {{
        "topic":"{topic}",
        "difficulty":"{difficulty}",
        "question":"Question",
        "options":[
            "Option A",
            "Option B",
            "Option C",
            "Option D"
        ],
        "correct_answer":"Option A",
        "explanation":"Explanation"
    }}
]

Rules:
1. Return ONLY JSON.
2. No markdown.
3. No code blocks.
4. Generate exactly 10 questions.
"""
            }
        ]
    )

    content = response.choices[0].message.content

    try:

        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

        quiz_data = json.loads(content)

        if isinstance(quiz_data, list):
            return quiz_data

        return []

    except Exception as e:

        print("Topic Quiz Error:", e)
        print(content)

        return []