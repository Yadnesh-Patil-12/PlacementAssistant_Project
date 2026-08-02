"""
agents/progress_agent.py
Aggregates a student's stored data into an analytics summary and produces a
short AI-generated insight/motivation note based on it.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.groq_api import ask_groq
from database.database import get_progress_summary

PROGRESS_SYSTEM_PROMPT = """You are a supportive placement-preparation coach
who reviews a student's practice analytics and gives one short, specific,
encouraging insight plus one concrete next step."""


class ProgressAgent:
    name = "Progress Tracker"

    def get_summary(self, student_id: int) -> dict:
        return get_progress_summary(student_id)

    def get_insight(self, student_id: int) -> str:
        summary = self.get_summary(student_id)
        user_prompt = f"""Here is a student's placement-prep analytics snapshot:
- Resume ATS score: {summary['ats_score']}/100
- DSA topics completed: {summary['dsa_done']}/{summary['dsa_total']}
- Aptitude average: {summary['aptitude_avg_pct']}% over {summary['aptitude_attempts']} attempts
- Interview practice sessions: {summary['interview_sessions']}

In 3-4 sentences, give one specific insight and one concrete next step."""
        return ask_groq(PROGRESS_SYSTEM_PROMPT, user_prompt, temperature=0.5, max_tokens=300)
