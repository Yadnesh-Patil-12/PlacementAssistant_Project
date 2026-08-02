"""
agents/aptitude_agent.py
Generates placement-style aptitude (quant / logical / verbal) practice sets.
"""

import re
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.groq_api import ask_groq
from utils.prompts import APTITUDE_SYSTEM_PROMPT, aptitude_user_prompt


class AptitudeAgent:
    name = "Aptitude Agent"

    def generate_quiz(self, topic: str, difficulty: str, num_questions: int = 5) -> list:
        user_prompt = aptitude_user_prompt(topic, difficulty, num_questions)
        raw = ask_groq(APTITUDE_SYSTEM_PROMPT, user_prompt, temperature=0.5, max_tokens=1500)
        return self._parse_quiz(raw)

    @staticmethod
    def _parse_quiz(raw_text: str) -> list:
        """Parse the LLM's formatted quiz text into a list of question dicts."""
        questions = []
        blocks = re.split(r"\n(?=Q\d+\.)", raw_text.strip())
        for block in blocks:
            q_match = re.search(r"Q\d+\.\s*(.+)", block)
            options = re.findall(r"([A-D])\)\s*(.+)", block)
            ans_match = re.search(r"Answer:\s*([A-D])", block)
            expl_match = re.search(r"Explanation:\s*(.+)", block)

            if not q_match or not options or not ans_match:
                continue

            questions.append({
                "question": q_match.group(1).strip(),
                "options": {letter: text.strip() for letter, text in options},
                "answer": ans_match.group(1).strip(),
                "explanation": expl_match.group(1).strip() if expl_match else "",
            })
        return questions
