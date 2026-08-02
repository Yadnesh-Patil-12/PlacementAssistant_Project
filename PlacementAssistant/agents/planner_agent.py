"""
agents/planner_agent.py
Builds a personalized day-by-day study timetable for placement preparation.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.groq_api import ask_groq
from utils.prompts import PLANNER_SYSTEM_PROMPT, planner_user_prompt


class PlannerAgent:
    name = "Study Planner Agent"

    def generate_plan(self, weak_areas: str, hours_per_day: int, days: int, target_date: str) -> str:
        user_prompt = planner_user_prompt(weak_areas, hours_per_day, days, target_date)
        return ask_groq(PLANNER_SYSTEM_PROMPT, user_prompt, temperature=0.4, max_tokens=1600)
