from streamlit_mic_recorder import mic_recorder
from pydub import AudioSegment
import speech_recognition as sr
import tempfile

from g_coding_practice import generate_coding_question

from voice_to_text import speech_to_text

import streamlit as st
from streamlit_calendar import calendar
from datetime import datetime
from a_student_profile import (
    save_profile,
    load_profile
)


import wave



from b_chatbot import get_ai_response
from c_pdf_summarizer import (
    extract_text_from_pdf,
    summarize_pdf,
    generate_detailed_explanation,
    generate_short_notes,
    generate_revision_notes,
  
    generate_important_questions
)
from d_quiz_generator import (
    generate_quiz,
    generate_topic_quiz
)
from e_study_planner import generate_learning_roadmap

from f_performance_tracker import *
from f_performance_tracker import get_subject_scores
from g_flashcards import generate_flashcards
from streamlit_mic_recorder import mic_recorder
from i_rag_learning import ask_pdf_question

from m_chat_history import (
    load_history,
    save_chat
)
from k_resume_analyzer import (
    extract_resume_text,
    analyze_resume
)
from n_study_history import (
    save_study_plan,
    get_study_history
)
from l_history_manager import (
    save_chat,
    get_chat_history,
    save_activity,
    get_activities,
    delete_activity,
    rename_activity
)
st.set_page_config(
    page_title="AI Learning Assistant",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
/* Streamlit Upload Box */

section[data-testid="stFileUploader"] {
    background: white !important;
}

section[data-testid="stFileUploader"] * {
    color: black !important;
}

[data-testid="stFileUploaderDropzone"] {
    background: white !important;
    border: 2px dashed #4F46E5 !important;
}

[data-testid="stFileUploaderDropzone"] * {
    color: black !important;
}
/* Main Background */
.stApp {
    background: #F8FAFC;
}
/* Force all quiz text visible */

.stMarkdown,
.stText,
.stCodeBlock,
code,
pre {
    color: black !important;
}
div[role="radiogroup"] label {
    color: black !important;
    font-weight: bold !important;
}
/* Headers */
h1, h2, h3 {
    color: #111827 !important;
    font-weight: bold !important;
}

/* Text */
p,
label,
span,
small,
div {
    color: #111827 !important;
}

/* Selectbox */
.stSelectbox * {
    color: black !important;
}

.stSelectbox div[data-baseweb="select"] {
    background-color: white !important;
    border-radius: 10px !important;
}

/* Dropdown */
div[role="listbox"] {
    background-color: white !important;
}

div[role="option"] {
    color: black !important;
    background: white !important;
    font-weight: bold !important;
}

div[role="option"]:hover {
    background-color: #E0E7FF !important;
    color: #4F46E5 !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        135deg,
        #2563EB,
        #7C3AED
    ) !important;

    color: white !important;
    border-radius: 20px !important;
    height: 90px !important;
    font-size: 18px !important;
    font-weight: bold !important;
    border: none !important;

    box-shadow: 0px 8px 20px rgba(0,0,0,0.15) !important;
}

.stButton > button:hover {
    transform: translateY(-5px);
}

/* Metrics */
[data-testid="stMetric"] {
    background: white !important;
    border-radius: 15px !important;
    padding: 15px !important;
    border: 2px solid #4F46E5 !important;
}

[data-testid="stMetricLabel"] {
    color: black !important;
    font-weight: bold !important;
}

[data-testid="stMetricValue"] {
    color: #4F46E5 !important;
    font-size: 30px !important;
    font-weight: bold !important;
}

/* Inputs */
    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea,
    .stDateInput input {
    background: white !important;
    color: black !important;
}
    border-radius: 10px !important;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    background: white !important;
    border-radius: 15px !important;
    padding: 15px !important;
    border: 2px solid #CBD5E1 !important;
}

/* Upload Text */
[data-testid="stFileUploader"] * {
    color: #111827 !important;
}

/* Success */
[data-testid="stAlert"] {
    border-radius: 12px !important;
}

/* Radio Buttons */
.stRadio label {
    color: #111827 !important;
}

/* Expander */
.streamlit-expanderHeader {
    color: #111827 !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: white !important;
}
/* File Uploader Fix */

[data-testid="stFileUploader"] {
    background: white !important;
    border-radius: 15px !important;
    padding: 15px !important;
}

[data-testid="stFileUploader"] * {
    color: black !important;
    opacity: 1 !important;
}
/* Upload Button Text Fix */

[data-testid="stFileUploaderDropzone"] button {
    color: black !important;
    background: white !important;
    font-weight: bold !important;
}

[data-testid="stFileUploaderDropzone"] span {
    color: black !important;
}

[data-testid="stFileUploaderDropzone"] p {
    color: black !important;
}

[data-testid="stFileUploaderDropzone"] small {
    color: black !important;
}
/* Study Planner Fix */

/* Date Input */
[data-testid="stDateInput"] input {
    color: black !important;
    background: white !important;
}

/* Number Input */
[data-testid="stNumberInput"] input {
    color: black !important;
    background: white !important;
}

/* Select Box */
[data-baseweb="select"] * {
    color: black !important;
}

/* Calendar */
button[aria-label] {
    color: black !important;
}

/* Input Labels */
[data-testid="stDateInput"] label,
[data-testid="stNumberInput"] label,
[data-testid="stSelectbox"] label {
    color: black !important;
    font-weight: bold !important;
}

/* Calendar Popup */
[role="dialog"] {
    background: white !important;
}

[role="dialog"] * {
    color: black !important;
}
/* Selectbox Fix */

div[data-baseweb="select"] {
    background: white !important;
    color: black !important;
}

/* Selected Value */
div[data-baseweb="select"] span {
    color: black !important;
    font-weight: bold !important;
}

/* Dropdown Menu */
ul[role="listbox"] {
    background: white !important;
}

/* Dropdown Options */
li {
    background: white !important;
    color: black !important;
    font-weight: bold !important;
}

/* Hover Effect */
li:hover {
    background: #E0E7FF !important;
    color: #4F46E5 !important;
}
/* Selectbox Background Fix */

div[data-baseweb="select"] {
    background: white !important;
    border: 2px solid #CBD5E1 !important;
}

div[data-baseweb="select"] > div {
    background: white !important;
    color: black !important;
}

div[data-baseweb="select"] span {
    color: black !important;
    font-weight: bold !important;
}

/* Dropdown Arrow */
div[data-baseweb="select"] svg {
    fill: black !important;
}
/* Number Input Buttons */

button[aria-label="Increment value"],
button[aria-label="Decrement value"] {
    background: white !important;
    color: black !important;
}
</style>


""", unsafe_allow_html=True)
if "latest_pdf_result" in st.session_state:
    del st.session_state["latest_pdf_result"]
if "page" not in st.session_state:
    st.session_state["page"] = "🏠 Home"
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "interview_questions" not in st.session_state:
    st.session_state["interview_questions"] = []

if "current_question" not in st.session_state:
    st.session_state["current_question"] = 0

if "interview_results" not in st.session_state:
    st.session_state["interview_results"] = []
if "interview_started" not in st.session_state:
    st.session_state["interview_started"] = False

if "interview_context" not in st.session_state:
    st.session_state["interview_context"] = ""

if "interview_messages" not in st.session_state:
    st.session_state["interview_messages"] = []
option = st.session_state["page"]

top_left, top_center, top_right = st.columns([1,4,1])

with top_left:
    if st.button(
        "🏠 Home",
        key="home_top_button",
        use_container_width=True
    ):
        st.session_state["page"] = "🏠 Home"
        st.rerun()

with top_center:
    st.markdown(
        """
        <h1 style='text-align:center;color:#111827;'>
        🎓 AI Learning Assistant
        </h1>
        """,
        unsafe_allow_html=True
    )

from h_career_guidance import generate_career_guidance

from k_resume_analyzer import (
    extract_resume_text,
    analyze_resume
)

st.markdown("""
<div style="
background: linear-gradient(135deg,#4F46E5,#7C3AED);
padding:40px;
border-radius:25px;
text-align:center;
color:white;
margin-bottom:25px;
">

<h1 style="color:white;">
🎓 AI-Powered Personalized Learning Assistant
</h1>

<h3 style="color:white;">
Your Personal AI Teacher for Learning, Practice and Placement Preparation
</h3>

<p style="color:white;font-size:18px;">
🤖 AI Chatbot | 📝 Quiz Generator | 📄 Notes Generator |
🎤 Mock Interview | 📚 RAG Learning | 🎯 Career Guidance
</p>

</div>
""", unsafe_allow_html=True)


# HOME PAGE
# HOME PAGE
if option == "🏠 Home":

    col_left, col_right = st.columns([4, 1])

    with col_left:
        profile = load_profile()

        if profile:

            st.markdown(
        f"""
        <div style="
        background:white;
        padding:25px;
        border-radius:20px;
        box-shadow:0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom:20px;
        ">

        <h2 style="color:#4F46E5;">
        👋 Welcome {profile['name']}
        </h2>

        <p>
        🎓 Course: {profile['course']}<br>
        📚 Year: {profile['year']}<br>
        🎯 Goal: {profile['goal']}
        </p>

        <hr>

        <h4 style="color:#111827;">
        AI Learning Assistant Status
        </h4>

        <p>
        ✅ Profile Created<br>
        ✅ AI Modules Ready<br>
        ✅ Mock Interview Available<br>
        ✅ Career Guidance Available
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

            
    

     

        st.markdown(
"""
<h1 style="
text-align:center;
color:#4F46E5;
font-size:40px;
font-weight:bold;
margin-bottom:20px;
">
🚀 AI Learning Dashboard
</h1>
""",
unsafe_allow_html=True
)
        st.write("")
        st.markdown("""
<h2 style="
color:#4F46E5;
margin-top:20px;
">
📚 Learning Tools
</h2>
""", unsafe_allow_html=True)
        st.info(
    "Learn smarter using AI-powered notes, quizzes, flashcards and study planning."
)

        row1_col1, row1_col2, row1_col3 = st.columns(3)

        with row1_col1:
            if st.button(
        "👤 Student Profile",
        key="profile_btn",
        use_container_width=True
            ):
                st.session_state["page"] = "👤 Student Profile"
                st.rerun()
        with row1_col2:
                if st.button(
        "🤖 AI Chatbot",
        key="chatbot_btn",
        use_container_width=True
                ):
                    st.session_state["page"] = "🤖 AI Chatbot"
                    st.rerun()       
            

        with row1_col3:
                if st.button(
        "📄 PDF Notes",
        key="notes_btn",
        use_container_width=True
                ):
                    st.session_state["page"] = "📄 PDF Summarizer"
                    st.rerun()

        st.write("")

        row2_col1, row2_col2, row2_col3, row2_col4 = st.columns(4)

        with row2_col1:
                if st.button(
        "📝 Quiz Generator",
        key="quiz_btn",
        use_container_width=True
                ):
                    st.session_state["page"] = "📝 Quiz Generator"
                    st.rerun()

        with row2_col2:
                    if st.button(
        "📅 Study Planner",
        key="planner_btn",
        use_container_width=True
                    ):
                        st.session_state["page"] = "📅 Study Planner"
                        st.rerun()
            

        with row2_col3:
                    if st.button(
        "🃏 Flashcards",
        key="flashcard_btn",
        use_container_width=True
                    ):
                        st.session_state["page"] = "🃏 Flashcards"
                        st.rerun()
        with row2_col4:
            if st.button(
        "💻 Coding Practice",
        key="coding_btn",
        use_container_width=True
            ):
                st.session_state["page"] = "💻 Coding Practice"
                st.rerun()

        st.write("")
        st.markdown("""
<h2 style="
color:#4F46E5;
margin-top:20px;
">
🤖 AI Features
</h2>
""", unsafe_allow_html=True)

        row3_col1, row3_col2, row3_col3 = st.columns(3)

        with row3_col1:
                if st.button(
        "🎯 Career Guidance",
        key="career_btn",
        use_container_width=True
                ):
                    st.session_state["page"] = "🎯 Career Guidance"
                    st.rerun()
        with row3_col2:
                if st.button(
        "📚 RAG Learning",
        key="rag_btn",
        use_container_width=True
                ):
                    st.session_state["page"] = "📚 RAG Learning"
                    st.rerun()

        with row3_col3:
                if st.button(
        "📄 Resume Analyzer",
        key="resume_btn",
        use_container_width=True
                ):
                    st.session_state["page"] = "📄 Resume Analyzer"
                    st.rerun()
        st.write("")
        st.markdown("""
<h2 style="
color:#4F46E5;
margin-top:20px;
">
📊 Analytics & Tracking
</h2>
""", unsafe_allow_html=True)
        st.info(
    "Track your performance, learning history and placement preparation progress."
)

        row4_col1, row4_col2, row4_col3, row4_col4 = st.columns(4)

        with row4_col1:
            if st.button(
        "📜 Learning History",
        key="history_btn",
        use_container_width=True
            ):
                st.session_state["page"] = "📜 Learning History"
                st.rerun()
        with row4_col2:
            if st.button(
        "💼 Placement Prep",
        key="placement_btn",
        use_container_width=True
            ):
                st.session_state["page"] = "💼 Placement Prep"
                st.rerun()

        with row4_col3:
            if st.button(
        "📊 Performance Tracker",
        key="tracker_btn",
        use_container_width=True
            ):
                st.session_state["page"] = "📊 Performance Tracker"
                st.rerun()
                
        with row4_col4:
            if st.button(
        "📈 Prediction",
        key="prediction_btn",
        use_container_width=True
            ):
                st.session_state["page"] = "📈 Performance Prediction"
                st.rerun()
        st.write("")
        st.markdown("""
<h2 style="
color:#4F46E5;
margin-top:20px;
">
🎤 Interactive Learning
</h2>
""", unsafe_allow_html=True)
        st.info(
    "Practice with Voice Assistant and Interactive AI Mock Interviews."
)
        col1, col2 = st.columns(2)

        with col1:
            if st.button(
        "🎤 Voice Assistant",
        key="voice_btn",
        use_container_width=True
            ):
                st.session_state["page"] = "🎤 Voice Assistant"
                st.rerun()

        with col2:
            if st.button(
        "🎤 Mock Interview",
        key="mock_btn",
        use_container_width=True
            ):
                st.session_state["page"] = "🎤 Mock Interview"
                st.rerun()
        

        
        
        st.markdown("""
<h2 style="
color:#4F46E5;
margin-top:20px;
">
💼 Placement & Career
</h2>
""", unsafe_allow_html=True)
        st.info(
    "Improve employability through Career Guidance, Learning Style Analysis and Placement Readiness."
)

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
        "🧠 Learning Style",
        key="learning_style_btn",
        use_container_width=True
            ):
                st.session_state["page"] = "🧠 Learning Style"
                st.rerun()

        with col2:
            if st.button(
        "🏆 Placement Readiness",
        key="placement_readiness_btn",
        use_container_width=True
            ):
                st.session_state["page"] = "🏆 Placement Readiness"
                st.rerun()

        st.divider()

        data = get_performance()

        average_score = get_average_score()
        mock_score = get_mock_interview_score()

        resume_score = 88
        mock_score = get_mock_interview_score()

        mock_score = get_mock_interview_score()

        placement_readiness = min(
    100,
    round(
        (
            average_score * 0.6
            +
            mock_score * 0.4
        ),
        2
    )
)

        st.metric(
    "🎯 Placement Readiness",
    f"{placement_readiness}%"
) 
        st.divider()

        st.subheader(
    "🧠 K-Means Learner Classification"
)

        learner_type = classify_learner_kmeans()

        if "Advanced" in learner_type:

            st.success(
        learner_type
    )

        elif "Intermediate" in learner_type:

            st.info(
        learner_type
    )

        else:

            st.warning(
        learner_type
    )
        st.subheader(
    "🎤 Mock Interview Score"
)

        st.progress(
    mock_score / 100
)

        st.info(
    f"Mock Interview Score: {mock_score}%"
)

        xp = (
    len(get_performance()) * 100
    + len(load_history()) * 20
    + len(get_study_history()) * 50
)

        if average_score >= 80:
            level = "Advanced"

        elif average_score >= 60:
            level = "Intermediate"

        else:
            level = "Beginner"
        st.markdown("""
<div style="
background:linear-gradient(135deg,#4F46E5,#7C3AED);
padding:25px;
border-radius:20px;
margin-bottom:20px;
">

<h2 style="
color:white;
text-align:center;
margin:0;
">
📊 Student Dashboard
</h2>

<p style="
color:white;
text-align:center;
margin-top:10px;
">
Track your learning progress and achievements
</p>

</div>
""", unsafe_allow_html=True)

        st.markdown("### 📊 Learning Statistics")

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric(
        "⭐ XP",
        xp
    )

        with m2:
            st.metric(
        "🏆 Level",
        level
    )

        with m3:
            st.metric(
        "🔥 Streak",
        len(data)
    )

        with m4:
            st.metric(
        "🎯 Quizzes",
        len(data)
    )

        st.write("")

        st.subheader("⭐ Learning Progress")

        st.progress(
    min(
        xp / 1000,
        1.0
    )
        )

        st.write(
    f"XP Earned: {xp}/1000"
                )

        st.subheader("📈 Learning Analytics")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.info(
        f"💬 Total Chats: {len(load_history())}"
                    )

        with col2:
            st.info(
        f"📝 Total Quizzes: {len(get_performance())}"
              )

        with col3:
            st.info(
        f"📅 Study Plans: {len(get_study_history())}"
            )

        st.subheader("🏅 Achievements")

        if len(get_performance()) >= 1:
            st.success(
        "🎯 First Quiz Completed"
            )

        if len(get_performance()) >= 5:
            st.success(
        "🏆 Quiz Master"
            )

        if len(load_history()) >= 1:
            st.success(
        "🤖 AI Chatbot Used"
            )

        if len(get_study_history()) >= 1:
            st.success(
        "📅 Study Plan Generated"
        )

        st.subheader("🔔 Smart Notifications")

        if len(get_performance()) == 0:
            st.warning(
        "📝 You have not completed any quiz yet."
        )

        if len(load_history()) < 5:
            st.info(
        "🤖 Explore the AI Chatbot to improve learning."
            )

        if len(get_study_history()) == 0:
            st.warning(
        "📅 Create your first study plan."
            )
        if len(get_performance()) >= 5:
            st.success(
        "🏆 Great job! Keep your learning streak going."
    )

        with col_right:

            st.subheader("📅 Calendar")



            today = datetime.today()

            events = [{
        "title": "Today",
        "start": today.strftime("%Y-%m-%d"),
        "color": "#6C63FF"
    }]

            calendar_options = {
        "initialView": "dayGridMonth",
        "height": 420,
        "headerToolbar": {
            "left": "prev,next",
            "center": "title",
            "right": ""
        }
    }

            calendar(
        events=events,
        options=calendar_options
    )
    st.markdown("## 🚀 Why Choose AI Learning Assistant?")

    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ Personalized Learning Roadmaps")
        st.success("✅ Adaptive Quiz Generation")
        st.success("✅ Resume Analysis")
        st.success("✅ Career Guidance")

    with col2:
        st.success("✅ AI-Powered Doubt Solving")
        st.success("✅ Smart Performance Tracking")
        st.success("✅ Interactive AI Mock Interviews")
        st.success("✅ Placement Preparation")


elif option == "👤 Student Profile":

    st.markdown("""
<h2>👨‍🎓 Student Profile</h2>

<p>
Create your learning profile and personalize your AI assistant.
</p>

</div>
""", unsafe_allow_html=True)

    st.header("👨‍🎓 Student Profile")

    name = st.text_input(
        "Student Name"
    )

    course = st.text_input(
        "Course"
    )

    year = st.text_input(
        "Year"
    )

    preferred_language = st.selectbox(
        "Preferred Language",
        [
            "English",
            "Hindi",
            "Telugu"
        ]
    )

    study_hours = st.number_input(
        "Daily Study Hours",
        min_value=1,
        max_value=12,
        value=2
    )

    goal = st.selectbox(
        "Learning Goal",
        [
            "Pass Exam",
            "Score Above 80%",
            "Placement Preparation",
            "Competitive Exam",
            "Master Subject"
        ]
    )

    if st.button(
        "Save Profile"
    ):

        save_profile(
            name,
            course,
            year,
            preferred_language,
            study_hours,
            goal
        )

        st.success(
            "Profile Saved Successfully!"
        )

    profile = load_profile()

    if profile:

        st.subheader(
            "Saved Profile"
        )

        st.json(profile)

# AI CHATBOT
elif option == "🤖 AI Chatbot":

    col_history, col_chat = st.columns([1,3])

    with col_history:

        st.subheader("📜 Chat History")

        history = load_history()

        for i, chat in enumerate(
    reversed(history)
        ):

            if st.button(
        chat["question"][:30],
        key=f"history_{i}"
            ):

                st.session_state["selected_chat"] = chat
    with col_chat:

        st.header("🤖 AI Chatbot")
        if "selected_chat" in st.session_state:

            st.subheader("📖 Previous Conversation")

            st.write(
        "**Question:**"
            )

            st.info(
                st.session_state[
            "selected_chat"
        ]["question"]
    )

            st.write(
        "**Answer:**"
    )

            st.success(
        st.session_state[
            "selected_chat"
        ]["answer"]
    )

            st.divider()

        user_question = st.text_input(
            "Ask your question"
        )

        if st.button(
            "Ask AI",
            key="ask_ai_btn"
        ):

            answer = get_ai_response(
                user_question
            )

            st.success(answer)

            save_chat(
    user_question,
    answer
)

# PDF SUMMARIZER
# PDF SUMMARIZER
elif option == "📄 PDF Summarizer":
    if "page" not in st.session_state:
        st.session_state["page"] = "📄 PDF Summarizer"

    if st.session_state["page"] != "📄 PDF Summarizer":

        if "latest_pdf_result" in st.session_state:
            del st.session_state["latest_pdf_result"]

    left_col, right_col = st.columns([1, 3])

    with left_col:

        st.subheader("📜 PDF History")

        activities = get_activities()

        if len(activities) == 0:

            st.info("No PDF History")

        else:

            for index, item in enumerate(reversed(activities)):

                st.container(border=True)

                st.markdown(
                f"**📄 {item['title']}**"
                )

                col1, col2, col3 = st.columns([2,1,1])

                with col1:

                    if st.button(
                    "👁 Open",
                    key=f"pdf_open_{index}",
                    use_container_width=True
                    ):

                        st.session_state[
                        "selected_pdf"
                    ] = item

                with col2:

                    if st.button(
                    "✏",
                    key=f"rename_{index}"
                ):

                        st.session_state[
                        f"edit_{index}"
                    ] = True

                with col3:

                    if st.button(
                    "🗑",
                    key=f"delete_{index}"
                    ):

                        delete_activity(
                        len(activities)-1-index
                    )

                        st.rerun()

                if st.session_state.get(
                f"edit_{index}",
                False
                ):

                    new_name = st.text_input(
                    "Rename",
                    value=item["title"],
                    key=f"text_{index}"
                )

                    if st.button(
                    "Save",
                    key=f"save_{index}"
                    ):

                        rename_activity(
                        len(activities)-1-index,
                        new_name
                    )

                        st.session_state[
                        f"edit_{index}"
                    ] = False

                        st.rerun()

            st.write("")
    with right_col:

        st.header("📄 AI Notes Generator")

        uploaded_file = st.file_uploader(
        "📂 Upload PDF / Handwritten Notes",
        type=["pdf", "png", "jpg", "jpeg"],
        key="pdf_upload"
    )

        if uploaded_file is not None:

            import os
            from PIL import Image
            import numpy as np

            pdf_name = os.path.splitext(uploaded_file.name)[0]

            st.success(f"✅ {uploaded_file.name} Uploaded Successfully")

            extension = os.path.splitext(uploaded_file.name)[1].lower()

        # =====================================
        # PDF FILE
        # =====================================

            if extension == ".pdf":

                pdf_text = extract_text_from_pdf(uploaded_file)

                if len(pdf_text.strip()) < 50:

                    st.warning("📷 Scanned PDF Detected. Running OCR...")

                    from o_ocr_reader import extract_text_from_scanned_pdf

                    pdf_text = extract_text_from_scanned_pdf(uploaded_file)

        # =====================================
        # IMAGE FILE
        # =====================================

            else:

                st.warning("📝 Handwritten Image Detected. Running OCR...")

                image = Image.open(uploaded_file)

                image_np = np.array(image)

                from o_ocr_reader import reader

                extracted = reader.readtext(
                image_np,
                detail=0
            )

                pdf_text = "\n".join(extracted)

        # =====================================
        # EXTRACTION CHECK
        # =====================================

            if len(pdf_text.strip()) == 0:

                st.error("❌ Unable to extract any text.")

                st.stop()

            st.success(
            f"✅ Extracted {len(pdf_text)} characters successfully."
        )

        # =====================================
        # OUTPUT TYPE
        # =====================================

            feature = st.selectbox(

            "📚 Choose AI Output",

            [

                "Summary",

                "Detailed Explanation",

                "Short Notes",

                "Revision Notes",

                "Important Questions",

                "Key Concepts",

                "MCQs",

                "Interview Questions",

                "Viva Questions",

                "Cheat Sheet"

            ],

            key="pdf_feature"

        )
            if st.button(
    "🚀 Generate",
    use_container_width=True,
    key="generate_pdf"
            ):

                with st.spinner("🤖 AI is analyzing your PDF..."):

                    if feature == "Summary":

                        result = summarize_pdf(pdf_text)

                    elif feature == "Detailed Explanation":

                        result = generate_detailed_explanation(pdf_text)

                    elif feature == "Short Notes":

                        result = generate_short_notes(pdf_text)

                    elif feature == "Revision Notes":

                        result = generate_revision_notes(pdf_text)

                    elif feature == "Important Questions":

                        result = generate_important_questions(pdf_text)

                    else:

                        result = "🚧 This feature is coming soon."

                    st.session_state["latest_pdf_result"] = result

                    print(save_activity)

                    save_activity(
    uploaded_file.name.replace(".pdf", ""),
    result,
    uploaded_file.name.replace(".pdf", "")
)

                    st.success("✅ Saved to PDF History")

                    st.session_state["selected_pdf"] = {

                    "title": pdf_name,

                    "content": result

                }

                    st.success("✅ Saved to PDF History")
if "latest_pdf_result" in st.session_state:

    st.markdown("---")

    st.subheader("📄 Generated Output")

    st.markdown(
        f"""
<div style="
background:white;
padding:20px;
border-radius:12px;
border:2px solid #E5E7EB;
max-height:650px;
overflow-y:auto;
white-space:pre-wrap;
font-size:16px;
line-height:1.8;
">

{st.session_state["latest_pdf_result"]}

</div>
""",
        unsafe_allow_html=True
    )
# QUIZ GENERATOR
elif option == "📝 Quiz Generator":

    st.header("📝 Interactive AI Quiz")

    quiz_mode = st.radio(
        "Choose Quiz Source",
        [
            "Generate from PDF",
            "Generate from Topic"
        ]
    )

    # ==========================
    # PDF QUIZ
    # ==========================

    if quiz_mode == "Generate from PDF":

        uploaded_file = st.file_uploader(
    "📂 Upload PDF or Handwritten Notes",
    type=["pdf", "png", "jpg", "jpeg"],
    key="pdf_upload"
)

        difficulty = st.selectbox(
            "Quiz Difficulty",
            [
                "Easy",
                "Medium",
                "Hard"
            ]
        )

        if uploaded_file is not None:

            st.success(
                "PDF Uploaded Successfully!"
            )

            if st.button(
                "Generate Quiz"
            ):

                pdf_text = extract_text_from_pdf(
                    uploaded_file
                )

                if not pdf_text.strip():

                    from o_ocr_reader import (
                        extract_text_from_scanned_pdf
                    )

                    pdf_text = extract_text_from_scanned_pdf(
                        uploaded_file
                    )

                quiz = generate_quiz(
                    pdf_text,
                    difficulty
                )

                st.session_state["quiz"] = quiz

    # ==========================
    # TOPIC QUIZ
    # ==========================

    else:

        topic = st.text_input(
            "Enter Topic (DSA, DBMS, Python, OS, CN)"
        )

        difficulty = st.selectbox(
            "Quiz Difficulty",
            [
                "Easy",
                "Medium",
                "Hard"
            ],
            key="topic_quiz"
        )

        if st.button(
            "Generate Topic Quiz"
        ):

            prompt = f"""
Generate 10 MCQ questions on {topic}.

Difficulty: {difficulty}

For each question provide:
question
4 options
correct_answer
explanation
topic

Return JSON format only.
"""

            response = get_ai_response(
                prompt
            )

            quiz = generate_topic_quiz(
    topic,
    difficulty
)

            st.session_state["quiz"] = quiz

    # ==========================
    # DISPLAY QUIZ
    # ==========================

    if "quiz" in st.session_state:

        quiz = st.session_state["quiz"]

        st.subheader(
            "Answer the Questions"
        )

        for i, question in enumerate(quiz):

            st.markdown(
                f"### Question {i+1}"
            )

            if "topic" in question:

                st.info(
                    f"📚 Topic: {question['topic']}"
                )

            selected_answer = st.radio(
                question["question"],
                question["options"],
                key=f"question_{i}",
                index=None
            )

            if st.button(
                f"Check Answer {i+1}",
                key=f"check_{i}"
            ):

                if selected_answer == question["correct_answer"]:

                    st.success(
                        "✅ Correct Answer"
                    )

                else:

                    st.error(
                        "❌ Wrong Answer"
                    )

                    st.write(
                        f"Correct Answer: {question['correct_answer']}"
                    )

                st.info(
                    question["explanation"]
                )

        if st.button(
            "Calculate Final Score"
        ):

            final_score = 0

            weak_topics = []

            strong_topics = []

            for i, question in enumerate(quiz):

                selected = st.session_state.get(
                    f"question_{i}"
                )

                topic = question.get(
                    "topic",
                    "Unknown Topic"
                )

                if selected == question["correct_answer"]:

                    final_score += 1

                    strong_topics.append(
                        topic
                    )

                else:

                    weak_topics.append(
                        topic
                    )

            subject_name = topic if "topic" in locals() else "PDF Quiz"

            save_score(
    subject_name,
    final_score,
    len(quiz),
    weak_topics,
    strong_topics
)

            st.success(
                f"🎯 Your Score: {final_score}/{len(quiz)}"
            )

            st.subheader(
                "📊 Learning Analytics"
            )

            st.success(
                "✅ Strong Topics"
            )

            for topic in list(set(strong_topics)):

                st.write(
                    f"• {topic}"
                )

            st.error(
                "❌ Weak Topics"
            )

            for topic in list(set(weak_topics)):

                st.write(
                    f"• {topic}"
                )
# STUDY PLANNER
# STUDY PLANNER
elif option == "📅 Study Planner":

    st.header("🚀 AI Learning Roadmap Generator")

    subject = st.text_input(
        "Enter Subject / Course Name"
    )

    topics = st.text_area(
        "Enter Topics (one per line)",
        height=200
    )

    current_level = st.selectbox(
        "Current Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    goal = st.selectbox(
        "Learning Goal",
        [
            "Pass Exam",
            "Score Above 80%",
            "Placement Preparation",
            "Competitive Exam",
            "Master the Subject",
            "Certification Preparation"
        ]
    )

    available_days = st.number_input(
        "Available Days",
        min_value=1,
        max_value=365,
        value=30
    )

    if st.button(
        "Generate Learning Roadmap"
    ):

        if subject and topics:

            with st.spinner(
    "🚀 AI is creating your learning roadmap..."
):

                roadmap = generate_learning_roadmap(
                    subject,
                    topics,
                    goal,
                    available_days,
                    current_level
                )

            st.subheader(
                "📚 Personalized Learning Roadmap"
            )

            st.success(
                roadmap
            )
            save_study_plan(
    subject,
    roadmap
)

        else:

            st.warning(
                "Please enter subject and topics."
            )
# RESUME ANALYZER
elif option == "📄 Resume Analyzer":

    st.header(
        "📄 AI Resume Analyzer"
    )

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        key="resume_pdf"
    )

    if uploaded_resume is not None:

        if st.button(
            "Analyze Resume"
        ):

            with st.spinner(
    "📄 AI is analyzing your resume..."
):

                resume_text = (extract_resume_text(uploaded_resume)
                )

                result = analyze_resume(
                    resume_text
                )
      

               

            st.subheader(
    "📊 Resume Analysis Report"
)

            st.markdown(
    result
)

     


# PERFORMANCE TRACKER
elif option == "📊 Performance Tracker":

    st.header(
        "📊 AI Learning Dashboard"
    )

    data = get_performance()

    if len(data) == 0:

        st.warning(
            "No quiz records available."
        )

    else:

        average_score = get_average_score()

        mock_score = get_mock_interview_score()

        resume_score = 88

        strong_topics = get_all_strong_topics()

        weak_topics = get_all_weak_topics()
        placement_readiness = min(
            100,
            round(
                average_score * 0.8 +
                len(data) * 2,
                2
            )
        )

        st.markdown("""
        <div style="
        background:white;
        padding:25px;
        border-radius:20px;
        box-shadow:0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom:20px;
        ">
        <h2 style="color:#4F46E5;">
        🚀 Personalized Learning Dashboard
        </h2>
        </div>
        """, unsafe_allow_html=True)

        # Learning Path

        st.subheader("🛣 Learning Path")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.success("✅ Profile")

        with col2:
            st.success("✅ Learning")

        with col3:
            st.success("✅ Quiz")

        with col4:
            st.info("🎤 Interview")

        with col5:
            st.warning("🏆 Placement")

        st.divider()

        col1, col2 = st.columns(2)

        with col1:

            next_topic = (
                weak_topics[0]
                if len(weak_topics) > 0
                else "Advanced Learning"
            )

            st.markdown(f"""
            ### 📚 Recommended Next

            **Topic:** {next_topic}

            **Duration:** 20 mins

            **Action:** Start Learning
            """)

        with col2:

            st.markdown(
                "### 🤖 AI Recommendation"
            )

            if len(weak_topics) > 0:

                st.write(
                    f"📚 Revise {weak_topics[0]}"
                )

                st.write(
                    "📝 Take another quiz"
                )

                st.write(
                    "🎤 Complete a mock interview"
                )

            else:

                st.success(
                    "🏆 Excellent Performance!"
                )

        st.divider()

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
        "📊 Average Score",
        f"{average_score}%"
    )

        with col2:
            st.metric(
        "📝 Quizzes Taken",
        len(data)
    )

        with col3:
            st.metric(
        "🎯 Placement Readiness",
        f"{placement_readiness}%"
    )

        with col4:
            st.metric(
    "🔥 Learning Activities",
    len(data)
)

        if average_score >= 80:

            st.success(
                "🏆 Performance Level: Advanced Learner"
            )

        elif average_score >= 60:

            st.info(
                "📚 Performance Level: Intermediate Learner"
            )

        else:

            st.warning(
                "🎯 Performance Level: Beginner Learner"
            )
        st.divider()
        placement_probability = round(
    (
        average_score * 0.4 +
        mock_score * 0.3 +
        resume_score * 0.3
    ),
    2
)

        st.divider()

        st.subheader(
    "🎯 Placement Prediction"
)

        st.metric(
    "Placement Success Probability",
    f"{placement_probability}%"
)

        if placement_probability >= 80:

            st.success(
        "🚀 High Placement Potential"
    )

        elif placement_probability >= 60:

            st.info(
        "📚 Moderate Placement Potential"
    )

        else:

            st.warning(
        "⚠ Improve Skills for Better Placement Chances"
    )

        st.subheader(
    "🎯 Placement Readiness Progress"
)

        st.progress(
    placement_readiness / 100
)

        if placement_readiness >= 80:

            st.success(
        "🚀 Ready for Placements"
    )

        elif placement_readiness >= 60:

            st.info(
        "📚 Almost Ready - Keep Practicing"
    )

        else:

            st.warning(
        "⚠ More Practice Required"
    )

        st.divider()
        st.divider()

        st.subheader(
    "📚 Skill Dashboard"
)

        

        subject_scores = get_subject_scores()

        for subject, score in subject_scores.items():

            st.write(
        f"**{subject}**"
    )

            st.progress(
        score / 100
    )

            st.caption(
        f"{score}%"
    )

            st.subheader(
            "💪 Strong Areas"
        )

        if len(strong_topics) == 0:

            st.write(
                "No strong topics yet."
            )

        else:

            for topic in strong_topics:

                st.success(
                    topic
                )

        st.subheader(
            "⚠ Weak Areas"
        )

        if len(weak_topics) == 0:

            st.write(
                "No weak topics yet."
            )

        else:

            for topic in weak_topics:

                st.warning(
                    topic
                )

        st.divider()

        st.subheader(
            "📉 Real-Time Skill Analysis"
        )

        if len(strong_topics) > 0:

            st.success(
                "💪 Strong Areas"
            )

            for topic in strong_topics:

                st.write(
                    f"✅ {topic}"
                )

                st.progress(90)

        if len(weak_topics) > 0:

            st.warning(
                "⚠ Weak Areas"
            )

            for topic in weak_topics:

                st.write(
                    f"❌ {topic}"
                )

                st.progress(40)

        st.divider()

        st.divider()

        st.subheader(
    "🤖 AI Career Coach"
)

        if len(weak_topics) > 0:

            st.info(
        f"📚 Revise {weak_topics[0]}"
    )

        if average_score < 60:

            st.warning(
        "⚠ Focus on fundamentals before moving to advanced topics."
    )

        elif average_score < 80:

            st.info(
        "📈 You're improving. Take more quizzes to strengthen weak areas."
    )

        else:

            st.success(
        "🚀 Excellent performance! Start placement-level preparation."
    )

        if placement_readiness < 70:

            st.info(
        "🎯 Complete more quizzes to improve placement readiness."
    )

        else:

            st.success(
        "🏆 You are approaching placement readiness."
    )

        st.info(
    "🎤 Complete a Mock Interview"
)

        st.info(
    "📄 Analyze your Resume"
)

        st.info(
    "💻 Practice DSA Daily"
)

        

            

        
        st.divider()

        st.subheader(
    "🏆 Achievements & Badges"
)

        badges = get_achievements()

        if len(badges) == 0:

            st.info(
        "No achievements unlocked yet."
    )

        else:

            for badge in badges:

                st.success(
            badge
        )

        st.subheader(
            "📈 Quiz History"
        )

        for item in data:

            st.info(
                f"""
📚 Subject: {item['subject']}

🎯 Score: {item['score']}/{item['total']}

📊 Percentage: {item['percentage']}%
"""
            )

        scores = []

        for item in data:

            scores.append(
                item["percentage"]
            )
        

        if len(scores) >= 2:
            predicted_score = predict_next_score()

            if predicted_score is not None:

                st.divider()

                st.subheader(
        "🤖 ML Performance Prediction"
    )
                
                st.metric(
        "Predicted Next Quiz Score",
        f"{predicted_score}%"
    )

                if predicted_score > average_score:

                    st.success(
            "📈 Model predicts improvement."
        )

                elif predicted_score < average_score:

                    st.warning(
            "📉 Model predicts performance decline."
        )

                else:

                    st.info(
            "➡ Performance likely to remain stable."
        )

            st.subheader(
                "📈 Learning Trend Analysis"
            )

            if scores[-1] > scores[0]:

                st.success(
                    "📈 Learning Trend: Improving"
                )

            elif scores[-1] < scores[0]:

                st.warning(
                    "📉 Learning Trend: Declining"
                )

            else:

                st.info(
                    "➡ Learning Trend: Stable"
                )

            st.line_chart(
                scores
            )

elif option == "📜 Learning History":

    st.header("📜 Learning History Dashboard")

    tab1, tab2, tab3 = st.tabs(
    [
        "🤖 Chat History",
        "📝 Quiz History",
        "📅 Study Plans"
    ]
)

    with tab1:

        history = load_history()

        if len(history) == 0:

            st.warning(
                "No chat history available."
            )

        else:

            for chat in reversed(history):

                st.subheader(
                    chat["question"]
                )

                st.success(
                    chat["answer"]
                )

                st.divider()

    with tab2:

        data = get_performance()

        if len(data) == 0:

            st.warning(
                "No quiz history available."
            )

        else:

            for item in reversed(data):

                st.info(
                    f"Score: {item['score']}/{item['total']}"
                )

                st.write(
                    f"Percentage: {item['percentage']}%"
                )

                st.divider()
    with tab3:

        plans = get_study_history()

        if len(plans) == 0:

            st.warning(
            "No study plans available."
        )

        else:

            for item in reversed(plans):

                st.subheader(
                item["subject"]
            )

                st.success(
                item["roadmap"]
            )

                st.divider()
# FLASHCARDS
elif option == "🃏 Flashcards":

    st.header(
        "🃏 AI Flashcard Generator"
    )

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        key="flashcard_pdf"
    )

    if uploaded_file is not None:

        pdf_text = extract_text_from_pdf(
    uploaded_file
)

        if not pdf_text.strip():

            from o_ocr_reader import (
        extract_text_from_scanned_pdf
    )

            pdf_text = extract_text_from_scanned_pdf(
        uploaded_file
    )

        if st.button(
            "Generate Flashcards"
        ):

            with st.spinner(
                "Creating Flashcards..."
            ):

                flashcards = (
                    generate_flashcards(
                        pdf_text
                    )
                )

            st.subheader(
                "🃏 Flashcards"
            )

            st.success(
                flashcards
            )
# CAREER GUIDANCE
# CAREER GUIDANCE
elif option == "🎯 Career Guidance":

    st.header(
        "🎯 AI Career Guidance"
    )

    strong_topics = st.text_area(
        "Strong Topics"
    )

    weak_topics = st.text_area(
        "Weak Topics"
    )

    goal = st.selectbox(
        "Career Goal",
        [
            "Software Engineer",
            "Data Scientist",
            "AI Engineer",
            "Cybersecurity",
            "Cloud Engineer",
            "Full Stack Developer"
        ]
    )

    if st.button(
        "Generate Career Guidance"
    ):

        with st.spinner(
            "Analyzing..."
        ):

            result = generate_career_guidance(
                strong_topics,
                weak_topics,
                goal
            )

        st.success(result)
# RAG LEARNING
elif option == "📚 RAG Learning":

    st.header(
        "📚 RAG-Based Learning Assistant"
    )

    uploaded_file = st.file_uploader(
        "Upload Notes PDF",
        type=["pdf"],
        key="rag_pdf"
    )

    if uploaded_file is not None:

        pdf_text = extract_text_from_pdf(
    uploaded_file
)

        if not pdf_text.strip():

            from o_ocr_reader import (
        extract_text_from_scanned_pdf
    )

            pdf_text = extract_text_from_scanned_pdf(
        uploaded_file
    )
        

        question = st.text_input(
            "Ask Question From PDF"
        )

        if st.button(
            "Get Answer"
        ):

            with st.spinner(
                "Searching Notes..."
            ):

                answer = ask_pdf_question(
                    pdf_text,
                    question
                )

            st.success(
                answer
            )
elif option == "💼 Placement Prep":

    st.header("💼 AI Placement Preparation Hub")

    placement_query = st.text_area(
        "What do you want to prepare for?",
        placeholder="Example: TCS interview questions, Java interview questions, HR questions, Aptitude questions..."
    )

    if st.button(
        "🚀 Generate Preparation Material",
        key="placement_generate"
    ):

        with st.spinner("Preparing..."):

            prompt = f"""
            You are a placement preparation expert.

            Give:
            1. Important questions
            2. Answers
            3. Tips
            4. Interview preparation roadmap

            Topic:
            {placement_query}
            """

            result = get_ai_response(prompt)

            st.markdown(result)
elif option == "🎤 Voice Assistant":

    st.header("🎤 AI Voice Assistant")

    st.write(
        "Speak through your microphone and the AI will convert your speech to text and answer your question."
    )

    audio = mic_recorder(
        start_prompt="🎤 Start Recording",
        stop_prompt="⏹ Stop Recording",
        key="voice_recorder"
    )

    if audio:
        

        st.success(
            "🎉 Voice Recorded Successfully!"
        )


        try:

            st.write(
                "Processing voice..."
            )

            text = speech_to_text(
                audio["bytes"]
            )

            st.write(
                "Extracted Text:"
            )

            st.write(
                text
            )

            st.subheader(
                "📝 Speech To Text"
            )

            st.info(
                text
            )

            if text.strip() != "":

                response = get_ai_response(
                    text
                )

                st.subheader(
                    "🤖 AI Response"
                )

                st.success(
                    response
                )

            else:

                st.warning(
                    "⚠ No speech detected. Please speak louder and try again."
                )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )
elif option == "🎤 Mock Interview":

    st.header("🎤 Interactive AI Interviewer")
    progress = min(
    len(st.session_state["interview_messages"]) / 20,
    1.0
)

    st.progress(progress)

    st.caption(
    f"Interview Progress: {int(progress*100)}%"
)

    uploaded_resume = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    if uploaded_resume is not None:

        resume_text = extract_resume_text(
            uploaded_resume
        )

        if not st.session_state["interview_started"]:

            if st.button(
                "🚀 Start AI Interview"
            ):

                first_question_prompt = f"""
                You are a professional technical interviewer.

                Candidate Resume:
                {resume_text}

                Start the interview.

                Ask ONLY the first interview question.

                Do not give explanation.
                Do not evaluate.
                Only ask one question.
                """

                first_question = get_ai_response(
                    first_question_prompt
                )

                st.session_state[
                    "interview_started"
                ] = True

                st.session_state[
                    "interview_context"
                ] = resume_text

                st.session_state[
                    "interview_messages"
                ] = [
                    {
                        "role": "ai",
                        "content": first_question
                    }
                ]

                st.rerun()

        else:

            for msg in st.session_state[
                "interview_messages"
            ]:

                if msg["role"] == "ai":

                    st.info(
                        f"🎤 Interviewer: {msg['content']}"
                    )

                else:

                    st.success(
                        f"👤 You: {msg['content']}"
                    )

            user_answer = st.text_area(
                "Your Answer",
                key=f"answer_{len(st.session_state['interview_messages'])}"
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "Submit Answer"
                ):

                    st.session_state[
                        "interview_messages"
                    ].append(
                        {
                            "role": "user",
                            "content": user_answer
                        }
                    )

                    conversation = ""

                    for msg in st.session_state[
                        "interview_messages"
                    ]:

                        conversation += (
                            f"{msg['role']}: "
                            f"{msg['content']}\n"
                        )

                    next_question_prompt = f"""
                    You are conducting a real interview.

                    Resume:
                    {st.session_state['interview_context']}

                    Conversation:
                    {conversation}

                    Ask ONLY the next interview question.

                    Do not give scores.
                    Do not explain.
                    Ask one follow-up question.
                    """

                    next_question = get_ai_response(
                        next_question_prompt
                    )

                    st.session_state[
                        "interview_messages"
                    ].append(
                        {
                            "role": "ai",
                            "content": next_question
                        }
                    )

                    st.rerun()

            with col2:

                if st.button(
                    "🛑 End Interview"
                ):

                    conversation = ""

                    for msg in st.session_state[
                        "interview_messages"
                    ]:

                        conversation += (
                            f"{msg['role']}: "
                            f"{msg['content']}\n"
                        )

                    report_prompt = f"""
                    You are an expert interview panel.

                    Based on this interview:

                    {conversation}

                    Generate:

                    1. Communication Score (/10)
                    2. Technical Knowledge Score (/10)
                    3. Confidence Score (/10)
                    4. Problem Solving Score (/10)
                    5. Placement Readiness (%)
                    6. Strengths
                    7. Areas for Improvement
                    8. Final Verdict

                    Format neatly.
                    """

                    report = get_ai_response(
                        report_prompt
                    )

                    st.subheader(
                        "🏆 Final Interview Report"
                    )

                    st.success(
                        report
                    )

                    if st.button(
                        "🔄 Start New Interview"
                    ):

                        st.session_state[
                            "interview_started"
                        ] = False

                        st.session_state[
                            "interview_context"
                        ] = ""

                        st.session_state[
                            "interview_messages"
                        ] = []

                        st.rerun()
elif option == "🧠 Learning Style":

    st.header("🧠 AI Learning Style Detection")

    learning_choice = st.selectbox(
        "How do you learn best?",
        [
            "Reading Notes",
            "Watching Videos",
            "Solving MCQs",
            "Real World Examples",
            "Hands-on Practice"
        ]
    )

    if st.button(
        "Analyze Learning Style"
    ):

        prompt = f"""
        Analyze the student's learning preference.

        Preferred Method:
        {learning_choice}

        Provide:

        1. Learning Style
        2. Strengths
        3. Weaknesses
        4. Best Study Method
        5. Personalized Recommendations

        Format neatly.
        """

        result = get_ai_response(
            prompt
        )

        st.success(
            result
        )
elif option == "🏆 Placement Readiness":

    st.header(
        "🏆 AI Placement Readiness Dashboard"
    )

    communication = st.slider(
        "Communication Skill",
        1,
        10,
        7
    )

    technical = st.slider(
        "Technical Knowledge",
        1,
        10,
        7
    )

    aptitude = st.slider(
        "Aptitude Skill",
        1,
        10,
        7
    )

    projects = st.slider(
        "Project Strength",
        1,
        10,
        7
    )

    if st.button(
        "Analyze Placement Readiness"
    ):

        prompt = f"""
        Analyze the student's placement readiness.

        Communication: {communication}/10
        Technical Skills: {technical}/10
        Aptitude: {aptitude}/10
        Projects: {projects}/10

        Provide:

        1. Placement Readiness Percentage
        2. Strengths
        3. Weak Areas
        4. Recommended Roles
        5. Improvement Plan
        6. Final Verdict

        Format neatly.
        """

        result = get_ai_response(
            prompt
        )

        st.success(
            result
        )
elif option == "📈 Performance Prediction":

    st.header(
        "📈 AI Performance Prediction"
    )

    data = get_performance()

    if len(data) < 2:

        st.warning(
            "Complete at least 2 quizzes to enable prediction."
        )

    else:

        from sklearn.linear_model import LinearRegression
        import numpy as np

        scores = []

        for item in data:

            if "score" in item:

                scores.append(
                    item["score"]
                )

        if len(scores) < 2:

            st.warning(
                "Not enough score data available."
            )

        else:

            X = np.array(
                range(1, len(scores) + 1)
            ).reshape(-1, 1)

            y = np.array(scores)

            model = LinearRegression()

            model.fit(X, y)

            next_quiz = np.array(
                [[len(scores) + 1]]
            )

            prediction = model.predict(
                next_quiz
            )[0]

            st.success(
                f"🎯 Predicted Next Quiz Score: {prediction:.2f}%"
            )

            if prediction >= 80:

                st.success(
                    "🏆 Excellent learning trend detected."
                )

            elif prediction >= 60:

                st.info(
                    "📚 Moderate performance trend."
                )

            else:

                st.warning(
                    "⚠ Performance may decline. More revision recommended."
                )

            st.subheader(
                "📈 Quiz Performance Trend"
            )

            st.line_chart(scores)
            if len(scores) >= 2:

                if scores[-1] > scores[0]:
                    st.success("📈 Learning Trend: Improving")

                elif scores[-1] < scores[0]:
                    st.warning("📉 Learning Trend: Declining")

                else:
                    st.info("➡ Learning Trend: Stable")

elif option == "💻 Coding Practice":

    st.header("💻 AI Coding Practice")

    st.markdown("""
    <div style="
    background: linear-gradient(90deg,#4F46E5,#7C3AED);
    padding:20px;
    border-radius:15px;
    color:white;
    margin-bottom:20px;
    ">
    <h2>💻 AI Coding Workspace</h2>
    <p>Practice DSA • Get AI Feedback • Improve Placement Readiness</p>
    </div>
    """, unsafe_allow_html=True)

    topic = st.selectbox(
        "📚 Choose Topic",
        [
            "Arrays",
            "Strings",
            "Linked List",
            "Stack",
            "Queue",
            "Tree",
            "Graph",
            "Dynamic Programming"
        ]
    )
   

    
    
    if "coding_question" not in st.session_state:
        st.session_state["coding_question"] = ""

    if "coding_feedback" not in st.session_state:
        st.session_state["coding_feedback"] = ""
    if st.button(
        "🎯 Generate Coding Question",
        use_container_width=True
    ):

        with st.spinner("Generating Question..."):

            st.session_state["coding_question"] = (
                generate_coding_question(topic)
            )

            st.session_state["coding_feedback"] = ""
            

    if st.session_state["coding_question"] != "":

        left_col, right_col = st.columns([1, 1])

        # ==================================
        # LEFT PANEL
        # ==================================

        with left_col:

            st.subheader("📄 Problem Description")

            st.markdown("""
    <style>
    .problem-box {
        border: 1px solid #d1d5db;
        border-radius: 10px;
        padding: 15px;
        height: 850px;
        overflow-y: auto;
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

            st.markdown(
    st.session_state["coding_question"]
)
        # ==================================
        # RIGHT PANEL
        # ==================================

        with right_col:

            st.subheader("💻 Code Editor")

            language = st.selectbox(
                "🌐 Programming Language",
                [
                    "Python",
                    "Java",
                    "C++",
                    "C",
                    "JavaScript"
                ]
            )

            user_code = st.text_area(
    "",
    height=350,
    placeholder=f"Write your {language} code here..."
)

            st.subheader("🧪 Test Cases")

            selected_case = st.radio(
                "",
                [
                    "Case 1",
                    "Case 2",
                    "Case 3"
                ],
                horizontal=True
            )

            if selected_case == "Case 1":

                test_cases = st.text_area(
                    "Input",
                    value="[1,2,3,4]",
                    height=120
                )

            elif selected_case == "Case 2":

                test_cases = st.text_area(
                    "Input",
                    value="[5,6,7,8]",
                    height=120
                )

            else:

                test_cases = st.text_area(
                    "Input",
                    value="[10,20,30]",
                    height=120
                )

            if st.button(
    "▶ Run & Evaluate",
    use_container_width=True
            ):

                with st.spinner("Analyzing Solution..."):

                    prompt = f"""
You are an expert coding interviewer.

Programming Language:
{language}

Coding Question:
{st.session_state['coding_question']}

Candidate Code:
{user_code}

Test Cases:
{test_cases}

Evaluate the candidate solution.

Provide output EXACTLY in this format:

================================

TEST RESULTS

Test Case 1

Input:
...

Your Output:
...

Expected Output:
...

Status:
PASS or FAIL

--------------------------------

Test Case 2

Input:
...

Your Output:
...

Expected Output:
...

Status:
PASS or FAIL

--------------------------------

Test Case 3

Input:
...

Your Output:
...

Expected Output:
...

Status:
PASS or FAIL

================================

CODE REVIEW

1. Correctness
2. Time Complexity
3. Space Complexity
4. Code Quality
5. Strengths
6. Mistakes
7. Suggested Improvements

================================

FINAL SCORE

Score: X/10

IMPORTANT:
Do not use markdown.
Do not use code blocks.
Return plain text only.
"""

                    st.session_state["coding_feedback"] = (get_ai_response(prompt))
                    save_activity(
    "Coding Practice",
    st.session_state["coding_feedback"]
)
                                # ===============================
            # RESULTS SECTION
            # ===============================

                    if st.session_state.get("coding_feedback", "") == "":

                        st.info(
                    "👆 Click Run & Evaluate to test your solution."
                )

                    else:

                        feedback = st.session_state.get(
                    "coding_feedback",
                    ""
                )

                # Success / Fail Banner

                        if "FAIL" not in feedback.upper():

                            st.success(
                        "✅ All Test Cases Passed!"
                    )

                        else:

                            st.error(
                        "❌ Some Test Cases Failed"
                    )

                # Attractive Header

                        st.markdown("""
                <div style="
                background: linear-gradient(135deg,#4F46E5,#7C3AED);
                padding:15px;
                border-radius:12px;
                color:white;
                margin-top:10px;
                margin-bottom:10px;
                ">
                <h3>📊 Test Results & AI Review</h3>
                <p>AI Evaluation Report</p>
                </div>
                """, unsafe_allow_html=True)

                # Attractive Report Box

                        st.markdown(f"""
                <div style="
                background:white;
                border:2px solid #E5E7EB;
                padding:20px;
                border-radius:15px;
                max-height:500px;
                overflow-y:auto;
                color:black;
                font-family:monospace;
                white-space:pre-wrap;
                box-shadow:0px 4px 15px rgba(0,0,0,0.08);
                ">
                {feedback}
                </div>
                """, unsafe_allow_html=True)
st.markdown("""
<hr>

<div style="
text-align:center;
padding:20px;
">

<h3 style="color:#4F46E5;">
🎓 AI-Powered Personalized Learning Assistant
</h3>

<p>
Personalized Learning • AI Tutoring • Career Guidance • Placement Preparation
</p>

<p>
Built with Python, Streamlit, Groq AI and RAG Technology
</p>

</div>
""", unsafe_allow_html=True)
