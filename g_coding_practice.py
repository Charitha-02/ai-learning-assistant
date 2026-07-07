from groq import Groq

import streamlit as st

API_KEY = st.secrets["GROQ_API_KEY"]


client = Groq(api_key=API_KEY)


def generate_coding_question(topic):

    prompt = f"""
Generate ONE professional LeetCode-style coding interview problem.

Topic:
{topic}

Return ONLY in the following format:

# Problem Title

# Difficulty

(Easy / Medium / Hard)

# Problem Statement

Write a detailed problem description of at least 150 words.

# Examples

Example 1

Input:
...

Output:
...

Explanation:
...

Example 2

Input:
...

Output:
...

Explanation:
...

# Constraints

- Constraint 1
- Constraint 2
- Constraint 3
- Constraint 4
- Constraint 5

# Test Cases

Test Case 1

Input:
...

Expected Output:
...

Test Case 2

Input:
...

Expected Output:
...

Test Case 3

Input:
...

Expected Output:
...

# Hint

Provide a useful hint without revealing the full solution.

# Expected Time Complexity

O(...)

# Expected Space Complexity

O(...)

Do NOT provide the solution.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert DSA interviewer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


