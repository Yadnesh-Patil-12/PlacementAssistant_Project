"""
pages/resume.py
Upload a resume PDF, get an ATS score + skill-gap analysis from the Resume Agent.
"""

import os
import streamlit as st

from agents.resume_agent import ResumeAgent
from utils.resume_parser import extract_text_from_pdf, save_uploaded_file
from database.database import save_resume_analysis, get_latest_resume
from config import UPLOAD_DIR

resume_agent = ResumeAgent()


def render(student: dict):
    st.title("📄 Resume Analyzer")
    st.caption("Upload your resume as a PDF to get an ATS score, skill-gap analysis, and improvement tips.")

    target_role = st.text_input("Target Role", value=student.get("target_role", ""))
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    if st.button("Analyze Resume", type="primary", disabled=uploaded_file is None):
        with st.spinner("Reading and analyzing your resume..."):
            save_path = os.path.join(UPLOAD_DIR, f"student_{student['id']}_{uploaded_file.name}")
            save_uploaded_file(uploaded_file, save_path)

            resume_text = extract_text_from_pdf(save_path)
            if not resume_text.strip():
                st.error("Could not extract text from this PDF. Try a text-based (not scanned) PDF.")
                return

            result = resume_agent.analyze(resume_text, target_role)
            save_resume_analysis(student["id"], result["ats_score"], result["analysis"])

        st.success("Analysis complete!")
        st.metric("ATS Score", f"{result['ats_score']} / 100")
        st.progress(result["ats_score"] / 100)
        st.markdown(result["analysis"])

    st.divider()
    st.subheader("📜 Last Saved Analysis")
    latest = get_latest_resume(student["id"])
    if latest:
        st.metric("ATS Score", f"{latest['ats_score']} / 100")
        with st.expander("View full analysis"):
            st.markdown(latest["analysis"])
    else:
        st.info("No resume analyzed yet.")
