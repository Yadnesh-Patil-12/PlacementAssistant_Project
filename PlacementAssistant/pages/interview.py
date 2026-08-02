"""
pages/interview.py
Mock HR and technical interview practice, powered by the HR Agent and
Technical Agent respectively.
"""

import streamlit as st

from agents.hr_agent import HRAgent
from agents.technical_agent import TechnicalAgent
from database.database import save_interview_session, get_interview_sessions

hr_agent = HRAgent()
technical_agent = TechnicalAgent()


def render(student: dict):
    st.title("🗣️ Interview Practice")
    st.caption("Practice with the HR Agent and the Technical Agent, and get instant feedback.")

    tab_hr, tab_tech = st.tabs(["🤝 HR Interview", "💻 Technical Interview"])

    with tab_hr:
        _hr_tab(student)

    with tab_tech:
        _technical_tab(student)


def _hr_tab(student: dict):
    target_role = st.text_input("Target Role", value=student.get("target_role", ""), key="hr_role")

    if st.button("Get HR Questions", key="hr_get_questions"):
        with st.spinner("HR Agent is preparing questions..."):
            st.session_state["hr_questions"] = hr_agent.get_questions(target_role, 5)

    questions = st.session_state.get("hr_questions", [])
    if questions:
        selected_q = st.selectbox("Choose a question to practice", questions, key="hr_selected_q")
        answer = st.text_area("Your Answer", key="hr_answer", height=150)

        if st.button("Get Feedback", key="hr_feedback_btn", disabled=not answer.strip()):
            with st.spinner("HR Agent is reviewing your answer..."):
                feedback = hr_agent.evaluate_answer(selected_q, answer)
                save_interview_session(student["id"], "HR", selected_q, answer, feedback)
            st.markdown(feedback)

    st.divider()
    st.caption("Recent HR sessions")
    for row in get_interview_sessions(student["id"], "HR")[:5]:
        with st.expander(row["question"][:80]):
            st.write("**Your answer:**", row["answer"])
            st.markdown(row["feedback"])


def _technical_tab(student: dict):
    col1, col2 = st.columns(2)
    with col1:
        topic = st.text_input("Topic", placeholder="e.g. OOP, DBMS, Operating Systems, Python", key="tech_topic")
    with col2:
        target_role = st.text_input("Target Role", value=student.get("target_role", ""), key="tech_role")

    if st.button("Get Technical Questions", key="tech_get_questions", disabled=not topic.strip()):
        with st.spinner("Technical Agent is preparing questions..."):
            st.session_state["tech_questions"] = technical_agent.get_questions(topic, target_role, 5)

    questions = st.session_state.get("tech_questions", [])
    if questions:
        selected_q = st.selectbox("Choose a question to practice", questions, key="tech_selected_q")
        answer = st.text_area("Your Answer", key="tech_answer", height=150)

        if st.button("Get Feedback", key="tech_feedback_btn", disabled=not answer.strip()):
            with st.spinner("Technical Agent is reviewing your answer..."):
                feedback = technical_agent.evaluate_answer(selected_q, answer)
                save_interview_session(student["id"], "Technical", selected_q, answer, feedback)
            st.markdown(feedback)

    st.divider()
    st.caption("Recent Technical sessions")
    for row in get_interview_sessions(student["id"], "Technical")[:5]:
        with st.expander(row["question"][:80]):
            st.write("**Your answer:**", row["answer"])
            st.markdown(row["feedback"])
