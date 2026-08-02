"""
agents/dsa_agent.py
Generates a personalized DSA (Data Structures & Algorithms) preparation
roadmap based on the student's current level and target companies.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.groq_api import ask_groq
from utils.prompts import DSA_SYSTEM_PROMPT, dsa_user_prompt

DEFAULT_TOPICS = [
    "Arrays & Strings",
    "Searching & Sorting",
    "Recursion & Backtracking",
    "Linked List",
    "Stacks & Queues",
    "Trees & Binary Search Trees",
    "Graphs (BFS/DFS)",
    "Dynamic Programming",
    "Greedy Algorithms",
    "Heaps & Priority Queues",
]


class DSAAgent:
    name = "DSA Agent"

    def generate_roadmap(self, current_level: str, target_companies: str, weeks: int) -> str:
        user_prompt = dsa_user_prompt(current_level, target_companies, weeks)
        return ask_groq(DSA_SYSTEM_PROMPT, user_prompt, temperature=0.4, max_tokens=1500)

    def default_topic_checklist(self):
        """Used to seed the DSA progress tracker with a standard topic list."""
        return DEFAULT_TOPICS
