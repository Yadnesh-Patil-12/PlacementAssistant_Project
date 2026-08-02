"""
agents/company_agent.py
Produces a placement-preparation briefing for a specific target company.
Note: this uses the LLM's general knowledge only (no live web search), so
the UI should present it as a starting point, not a confirmed/current source.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.groq_api import ask_groq
from utils.prompts import COMPANY_SYSTEM_PROMPT, company_user_prompt


class CompanyAgent:
    name = "Company Agent"

    def research(self, company_name: str, target_role: str) -> str:
        user_prompt = company_user_prompt(company_name, target_role)
        return ask_groq(COMPANY_SYSTEM_PROMPT, user_prompt, temperature=0.4, max_tokens=1200)
