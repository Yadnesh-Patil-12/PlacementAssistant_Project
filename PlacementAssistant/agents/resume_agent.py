"""
agents/resume_agent.py
Analyzes a student's resume text against a target role: ATS score,
strengths, skill gaps, formatting issues, and suggestions.
"""

import re
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.groq_api import ask_groq
from utils.prompts import RESUME_SYSTEM_PROMPT, resume_user_prompt


class ResumeAgent:
    name = "Resume Agent"

    def analyze(self, resume_text: str, target_role: str) -> dict:
        user_prompt = resume_user_prompt(resume_text, target_role)
        raw = ask_groq(RESUME_SYSTEM_PROMPT, user_prompt, temperature=0.3, max_tokens=1200)
        return {
            "ats_score": self._extract_score(raw),
            "analysis": raw,
        }

    @staticmethod
    def _extract_score(text: str) -> int:
        match = re.search(r"ATS_SCORE:\s*(\d{1,3})", text)
        if match:
            return max(0, min(int(match.group(1)), 100))
        return 0
