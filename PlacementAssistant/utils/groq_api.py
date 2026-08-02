"""
utils/groq_api.py
Thin wrapper around the Groq chat-completions API.
Every agent calls ask_groq() instead of talking to the SDK directly, so the
LLM provider/model can be swapped in one place.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

_client = None


def get_client() -> Groq:
    global _client
    if _client is None:
        if not GROQ_API_KEY or GROQ_API_KEY == "your_groq_api_key_here":
            raise ValueError(
                "GROQ_API_KEY is not set. Get a free key at https://console.groq.com "
                "and add it to your .env file."
            )
        _client = Groq(api_key=GROQ_API_KEY)
    return _client


def ask_groq(system_prompt: str, user_prompt: str, temperature: float = 0.4, max_tokens: int = 1400) -> str:
    """
    Send a system + user prompt to Groq and return the plain text reply.
    Any failure (missing key, network issue, rate limit) is returned as a
    readable string instead of raising, so Streamlit pages stay usable.
    """
    try:
        client = get_client()
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return (
            "⚠️ Could not reach the AI service.\n\n"
            f"Details: {e}\n\n"
            "Check that GROQ_API_KEY is set correctly in your .env file and that you have an internet connection."
        )
