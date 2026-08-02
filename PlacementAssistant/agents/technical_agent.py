"""
agents/technical_agent.py
Generates technical mock-interview questions and evaluates candidate answers.
"""

import re
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.groq_api import ask_groq
from utils.prompts import TECHNICAL_SYSTEM_PROMPT, technical_questions_prompt, technical_feedback_prompt


class TechnicalAgent:
    name = "Technical Interview Agent"

    def get_questions(self, topic: str, target_role: str, count: int = 5) -> list:
        raw = ask_groq(
            TECHNICAL_SYSTEM_PROMPT,
            technical_questions_prompt(topic, target_role, count),
            temperature=0.5,
            max_tokens=600,
        )
        return self._parse_numbered_list(raw)

    def evaluate_answer(self, question: str, answer: str) -> str:
        return ask_groq(
            TECHNICAL_SYSTEM_PROMPT,
            technical_feedback_prompt(question, answer),
            temperature=0.3,
            max_tokens=700,
        )

    @staticmethod
    def _parse_numbered_list(raw_text: str) -> list:
        lines = [l.strip() for l in raw_text.split("\n") if l.strip()]
        cleaned = []
        for line in lines:
            line = re.sub(r"^\d+[\.\)]\s*", "", line)
            if line:
                cleaned.append(line)
        return cleaned
