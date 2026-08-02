"""
pages/company.py
Generates a placement-preparation briefing for a specific target company.
"""

import streamlit as st

from agents.company_agent import CompanyAgent
from database.database import save_company_research, get_company_research_history

company_agent = CompanyAgent()


def render(student: dict):
    st.title("🏢 Company Research")
    st.caption("Get a prep briefing for a company you're applying to.")

    col1, col2 = st.columns(2)
    with col1:
        company_name = st.text_input("Company Name", placeholder="e.g. TCS, Infosys, Amazon")
    with col2:
        target_role = st.text_input("Role", value=student.get("target_role", ""))

    if st.button("Research Company", type="primary", disabled=not company_name.strip()):
        with st.spinner(f"Company Agent is researching {company_name}..."):
            research = company_agent.research(company_name, target_role)
            save_company_research(student["id"], company_name, research)
        st.markdown(research)
        st.caption("ℹ️ Based on general knowledge — always cross-check with the company's official careers page for the latest process.")

    st.divider()
    st.subheader("📚 Past Research")
    history = get_company_research_history(student["id"])
    if history:
        for row in history[:10]:
            with st.expander(f"{row['company']} — {row['created_at'][:16]}"):
                st.markdown(row["research"])
    else:
        st.info("No company research saved yet.")
