from groq import Groq

# Paste your Groq API Key here
import streamlit as st
API_KEY = st.secrets["GROQ_API_KEY"]

client = Groq(api_key=API_KEY)


def generate_learning_roadmap(
    subject,
    topics,
    goal,
    available_days,
    current_level
):

    prompt = f"""
Create a personalized learning roadmap.

Subject:
{subject}

Topics:
{topics}

Current Level:
{current_level}

Goal:
{goal}

Available Days:
{available_days}

Instructions:

1. Create a day-wise roadmap.
2. Arrange topics from easy to difficult.
3. Include revision sessions.
4. Include practice sessions.
5. Include quizzes and tests.
6. Mention estimated study time.
7. Make the roadmap student-friendly.
8. Suitable for any subject or course.
9. Use proper headings and formatting.

Generate a complete roadmap.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """
You are an expert educational mentor.

You create personalized learning roadmaps for:

- Engineering Subjects
- School Subjects
- Programming Languages
- Certifications
- Competitive Exams
- Any Online Course

Generate practical and realistic study plans.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content