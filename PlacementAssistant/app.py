"""
app.py
Multi-Agent Placement Preparation Assistant
"""

import streamlit as st

from config import APP_NAME, APP_ICON
from database.database import init_db, get_or_create_student

from pages import (
    dashboard,
    resume,
    dsa,
    aptitude,
    company,
    interview,
    planner,
    progress,
)

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Load CSS ---------------- #

def load_css():
    from pathlib import Path
    with open(Path(__file__).parent / "styles.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------------- Database ---------------- #

init_db()

# ---------------- Login ---------------- #

def login_gate():

    if "student" in st.session_state:
        return st.session_state["student"]

    st.title("🤖 Multi-Agent Placement Preparation Assistant")
    st.write("AI Powered Career Coach using Multi-Agent System & Groq AI")

    st.divider()

    st.subheader("🔐 Student Login")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input("👤 Full Name")

        email = st.text_input("📧 Email")

        role = st.text_input(
            "🎯 Target Role",
            value="Software Engineer"
        )

        if st.button("🚀 Enter Dashboard", use_container_width=True):

            if name.strip() == "" or email.strip() == "":
                st.error("Please enter Name and Email.")
            else:

                student = get_or_create_student(
                    name.strip(),
                    email.strip(),
                    role.strip()
                )

                st.session_state["student"] = student
                st.rerun()

    with col2:

        st.subheader("✨ Features")

        st.success("📄 Resume ATS Analysis")
        st.success("💻 DSA Roadmap Generator")
        st.success("🧮 Aptitude Practice")
        st.success("🏢 Company Research")
        st.success("🎤 HR Interview")
        st.success("💻 Technical Interview")
        st.success("📅 AI Study Planner")
        st.success("📈 Progress Tracking")

    st.stop()

student = login_gate()

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.markdown("# 🤖 Placement AI")

    st.markdown("---")

    st.success(f"👋 Welcome\n\n**{student['name']}**")

    st.info(f"🎯 {student['target_role']}")

    st.markdown("---")

    if st.button("🚪 Logout"):

        del st.session_state["student"]

        st.rerun()

# ---------------- Navigation ---------------- #

def dashboard_page():
    dashboard.render(student)

def resume_page():
    resume.render(student)

def dsa_page():
    dsa.render(student)

def aptitude_page():
    aptitude.render(student)

def company_page():
    company.render(student)

def interview_page():
    interview.render(student)

def planner_page():
    planner.render(student)

def progress_page():
    progress.render(student)

pg = st.navigation(

    [

        st.Page(dashboard_page, title="Dashboard", icon="🏠", default=True),

        st.Page(resume_page, title="Resume Analyzer", icon="📄"),

        st.Page(dsa_page, title="DSA Roadmap", icon="💻"),

        st.Page(aptitude_page, title="Aptitude", icon="🧮"),

        st.Page(company_page, title="Company", icon="🏢"),

        st.Page(interview_page, title="Interview", icon="🎤"),

        st.Page(planner_page, title="Planner", icon="📅"),

        st.Page(progress_page, title="Progress", icon="📈"),

    ]

)

pg.run()