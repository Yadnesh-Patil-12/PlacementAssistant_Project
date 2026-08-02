"""
pages/planner.py
Generates a personalized day-by-day placement preparation study timetable.
"""

import datetime
import streamlit as st

from agents.planner_agent import PlannerAgent
from database.database import save_study_plan, get_latest_study_plan

planner_agent = PlannerAgent()


def render(student: dict):
    st.title("🗓️ Study Planner")
    st.caption("Get a personalized preparation timetable based on your weak areas and available time.")

    weak_areas = st.text_input(
        "Weak Areas",
        placeholder="e.g. Dynamic Programming, Aptitude, HR communication",
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        hours_per_day = st.slider("Hours available per day", 1, 10, 3)
    with col2:
        days = st.slider("Plan length (days)", 3, 30, 7)
    with col3:
        target_date = st.date_input("Target Placement Date", value=datetime.date.today() + datetime.timedelta(days=30))

    if st.button("Generate Study Plan", type="primary", disabled=not weak_areas.strip()):
        with st.spinner("Study Planner Agent is building your timetable..."):
            plan = planner_agent.generate_plan(weak_areas, hours_per_day, days, str(target_date))
            save_study_plan(student["id"], plan)
        st.markdown(plan)

    st.divider()
    st.subheader("📌 Last Saved Plan")
    latest = get_latest_study_plan(student["id"])
    if latest:
        with st.expander(f"Saved on {latest['created_at'][:16]}"):
            st.markdown(latest["plan_text"])
    else:
        st.info("No study plan generated yet.")
