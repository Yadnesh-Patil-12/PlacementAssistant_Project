"""
config.py
Configuration for Multi-Agent Placement Preparation Assistant
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# ==========================================================
# Base Directory
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

# ==========================================================
# Environment File
# ==========================================================

ENV_FILE = BASE_DIR / ".env"

if ENV_FILE.exists():
    load_dotenv(dotenv_path=ENV_FILE, override=True)

# ==========================================================
# Groq Configuration
# ==========================================================

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)

# Stop the application if API key is missing
if not GROQ_API_KEY:
    raise ValueError(
        "❌ GROQ_API_KEY not found. Please check your .env file."
    )

# ==========================================================
# Application
# ==========================================================

APP_NAME = "Multi-Agent Placement Preparation Assistant"

APP_ICON = "🎯"

# ==========================================================
# Theme Colors
# ==========================================================

PRIMARY_COLOR = "#7C3AED"

SECONDARY_COLOR = "#4F46E5"

SUCCESS_COLOR = "#22C55E"

WARNING_COLOR = "#F59E0B"

DANGER_COLOR = "#EF4444"

BACKGROUND_COLOR = "#0F172A"

CARD_COLOR = "#1E293B"

TEXT_COLOR = "#F8FAFC"

# ==========================================================
# Database
# ==========================================================

DB_DIR = BASE_DIR / "database"

DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "student.db"

# ==========================================================
# Uploads
# ==========================================================

UPLOAD_DIR = BASE_DIR / "uploads"

UPLOAD_DIR.mkdir(exist_ok=True)

# ==========================================================
# Reports
# ==========================================================

REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)

# ==========================================================
# Assets
# ==========================================================

ASSETS_DIR = BASE_DIR / "assets"

ASSETS_DIR.mkdir(exist_ok=True)

# ==========================================================
# Debug
# ==========================================================

print("=" * 60)
print("Application :", APP_NAME)
print("Base Dir    :", BASE_DIR)
print("ENV File    :", ENV_FILE)
print("ENV Exists  :", ENV_FILE.exists())
print("Database    :", DB_PATH)
print("Groq Model  :", GROQ_MODEL)
print("API Loaded  :", "YES" if GROQ_API_KEY else "NO")
print("=" * 60)