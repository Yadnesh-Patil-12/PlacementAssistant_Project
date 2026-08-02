"""
pages/progress.py
Visual analytics dashboard: resume score, DSA completion, aptitude trend,
and interview practice volume, plus an AI-generated insight.
"""

import streamlit as st
import pandas as pd
import plotly.express as px

from agents.progress_agent import ProgressAgent
from database.database import get_dsa_progress, get_aptitude_scores, get_interview_sessions

progress_agent = ProgressAgent()


def render(student: dict):
    st.title("📊 Progress Tracker")
    st.caption("A snapshot of your placement preparation journey so far.")

    summary = progress_agent.get_summary(student["id"])

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Resume ATS Score", f"{summary['ats_score']}/100")
    col2.metric("DSA Topics Done", f"{summary['dsa_done']}/{summary['dsa_total']}")
    col3.metric("Aptitude Avg", f"{summary['aptitude_avg_pct']}%")
    col4.metric("Interview Sessions", summary["interview_sessions"])

    if st.button("💡 Get AI Insight"):
        with st.spinner("Progress Tracker is analyzing your data..."):
            insight = progress_agent.get_insight(student["id"])
        st.info(insight)

    st.divider()

    dsa_rows = get_dsa_progress(student["id"])
    apt_rows = get_aptitude_scores(student["id"])
    interview_rows = get_interview_sessions(student["id"])

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("DSA Topic Status")
        if dsa_rows:
            df = pd.DataFrame(dsa_rows)
            counts = df["status"].value_counts().reset_index()
            counts.columns = ["Status", "Count"]
            fig = px.pie(counts, names="Status", values="Count", hole=0.45,
            color="Status", color_discrete_map={"Completed": "#7A3FF2", "Pending": "#D8D2F5"})
            st.plotly_chart(fig, width="stretch")
        else:
            st.info("No DSA topics tracked yet. Visit the DSA Roadmap page.")

    with col_b:
        st.subheader("Aptitude Score Trend")
        if apt_rows:
            df = pd.DataFrame(apt_rows)
            df["pct"] = (df["score"] / df["total"] * 100).round(1)
            df["attempt"] = range(1, len(df) + 1)
            fig = px.line(df, x="attempt", y="pct", markers=True, labels={"pct": "Score (%)", "attempt": "Attempt #"})
            fig.update_traces(line_color="#7A3FF2")
            st.plotly_chart(fig, width="stretch")
        else:
            st.info("No aptitude attempts yet. Visit the Aptitude Practice page.")

    st.subheader("Interview Practice Volume")
    if interview_rows:
        df = pd.DataFrame(interview_rows)
        counts = df["session_type"].value_counts().reset_index()
        counts.columns = ["Type", "Sessions"]
        fig = px.bar(counts, x="Type", y="Sessions", color="Type",
        color_discrete_map={"HR": "#2B2E7F", "Technical": "#7A3FF2"})
        st.plotly_chart(fig, width="stretch")
    else:
        st.info("No interview practice sessions yet. Visit the Interview Practice page.")
