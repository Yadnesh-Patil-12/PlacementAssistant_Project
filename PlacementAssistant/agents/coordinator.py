"""
agents/coordinator.py
The Coordinator Agent sits above the specialized agents. It does not do
resume analysis, DSA planning, etc. itself - it looks at the student's goal
and current progress snapshot and tells them which specialized agent to use
next and why. This mirrors the "coordinator controls workflow" pattern used
throughout the project.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.groq_api import ask_groq
from utils.prompts import COORDINATOR_SYSTEM_PROMPT, coordinator_user_prompt


class CoordinatorAgent:
    name = "Coordinator Agent"

    def create_action_plan(self, goal: str, progress_summary: dict) -> str:
        profile_summary = (
            f"- Resume ATS score: {progress_summary.get('ats_score', 0)}/100\n"
            f"- DSA topics completed: {progress_summary.get('dsa_done', 0)}/{progress_summary.get('dsa_total', 0)}\n"
            f"- Aptitude average: {progress_summary.get('aptitude_avg_pct', 0)}% "
            f"over {progress_summary.get('aptitude_attempts', 0)} attempts\n"
            f"- Interview practice sessions completed: {progress_summary.get('interview_sessions', 0)}"
        )
        user_prompt = coordinator_user_prompt(goal, profile_summary)
        return ask_groq(COORDINATOR_SYSTEM_PROMPT, user_prompt, temperature=0.4, max_tokens=700)
