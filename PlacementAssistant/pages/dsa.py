"""
pages/dsa.py
Generates a personalized DSA roadmap and tracks topic-wise completion.
"""

import streamlit as st

from agents.dsa_agent import DSAAgent
from database.database import upsert_dsa_topic, get_dsa_progress

dsa_agent = DSAAgent()


def render(student: dict):
    st.title("💻 DSA Roadmap")
    st.caption("Get a personalized Data Structures & Algorithms preparation plan.")

    col1, col2, col3 = st.columns(3)
    with col1:
        current_level = st.selectbox("Current Level", ["Beginner", "Intermediate", "Advanced"])
    with col2:
        target_companies = st.text_input("Target Companies", placeholder="e.g. TCS, Infosys, product-based companies")
    with col3:
        weeks = st.slider("Timeframe (weeks)", 2, 16, 8)

    if st.button("Generate Roadmap", type="primary"):
        with st.spinner("DSA Agent is building your roadmap..."):
            roadmap = dsa_agent.generate_roadmap(current_level, target_companies or "any", weeks)
        st.markdown(roadmap)

    st.divider()
    st.subheader("✅ Topic Checklist")
    st.caption("Track your progress across core DSA topics.")

    progress_rows = {row["topic"]: row["status"] for row in get_dsa_progress(student["id"])}

    for topic in dsa_agent.default_topic_checklist():
        current_status = progress_rows.get(topic, "Pending")
        checked = st.checkbox(topic, value=(current_status == "Completed"), key=f"dsa_{topic}")
        new_status = "Completed" if checked else "Pending"
        if new_status != current_status:
            upsert_dsa_topic(student["id"], topic, new_status)
