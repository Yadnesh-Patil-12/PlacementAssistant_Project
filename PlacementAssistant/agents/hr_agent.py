"""
agents/hr_agent.py
Generates HR interview questions and gives feedback on candidate answers.
"""

import re
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.groq_api import ask_groq
from utils.prompts import HR_SYSTEM_PROMPT, hr_questions_prompt, hr_feedback_prompt


class HRAgent:
    name = "HR Interview Agent"

    def get_questions(self, target_role: str, count: int = 5) -> list:
        raw = ask_groq(HR_SYSTEM_PROMPT, hr_questions_prompt(target_role, count), temperature=0.6, max_tokens=500)
        return self._parse_numbered_list(raw)

    def evaluate_answer(self, question: str, answer: str) -> str:
        return ask_groq(HR_SYSTEM_PROMPT, hr_feedback_prompt(question, answer), temperature=0.4, max_tokens=600)

    @staticmethod
    def _parse_numbered_list(raw_text: str) -> list:
        lines = [l.strip() for l in raw_text.split("\n") if l.strip()]
        cleaned = []
        for line in lines:
            line = re.sub(r"^\d+[\.\)]\s*", "", line)
            if line:
                cleaned.append(line)
        return cleaned
