"""
database/database.py
SQLite persistence layer for the Placement Preparation Assistant.
All agents/pages read and write student data through the functions here.
"""

import sqlite3
import json
from datetime import datetime
from contextlib import contextmanager

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DB_PATH


@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db():
    """Create all tables if they do not already exist. Safe to call every app start."""
    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                target_role TEXT,
                created_at TEXT
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS resume_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                ats_score INTEGER,
                analysis TEXT,
                created_at TEXT,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS dsa_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                topic TEXT,
                status TEXT DEFAULT 'Pending',
                updated_at TEXT,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS aptitude_scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                topic TEXT,
                score INTEGER,
                total INTEGER,
                created_at TEXT,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS interview_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                session_type TEXT,
                question TEXT,
                answer TEXT,
                feedback TEXT,
                created_at TEXT,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS study_plan (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                plan_text TEXT,
                created_at TEXT,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS company_research (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                company TEXT,
                research TEXT,
                created_at TEXT,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """)


# ---------------------------------------------------------------------------
# Students
# ---------------------------------------------------------------------------

def get_or_create_student(name: str, email: str, target_role: str) -> dict:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM students WHERE email = ?", (email,))
        row = cur.fetchone()
        if row:
            # keep target role up to date if the student changed it at login
            cur.execute(
                "UPDATE students SET target_role = ? WHERE id = ?",
                (target_role, row["id"]),
            )
            return {"id": row["id"], "name": row["name"], "email": row["email"], "target_role": target_role}

        cur.execute(
            "INSERT INTO students (name, email, target_role, created_at) VALUES (?, ?, ?, ?)",
            (name, email, target_role, datetime.now().isoformat()),
        )
        new_id = cur.lastrowid
        return {"id": new_id, "name": name, "email": email, "target_role": target_role}


# ---------------------------------------------------------------------------
# Resume
# ---------------------------------------------------------------------------

def save_resume_analysis(student_id: int, ats_score: int, analysis: str):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO resume_analysis (student_id, ats_score, analysis, created_at) VALUES (?, ?, ?, ?)",
            (student_id, ats_score, analysis, datetime.now().isoformat()),
        )


def get_latest_resume(student_id: int):
    with get_connection() as conn:
        cur = conn.execute(
            "SELECT * FROM resume_analysis WHERE student_id = ? ORDER BY id DESC LIMIT 1",
            (student_id,),
        )
        row = cur.fetchone()
        return dict(row) if row else None


# ---------------------------------------------------------------------------
# DSA progress
# ---------------------------------------------------------------------------

def upsert_dsa_topic(student_id: int, topic: str, status: str):
    with get_connection() as conn:
        cur = conn.execute(
            "SELECT id FROM dsa_progress WHERE student_id = ? AND topic = ?",
            (student_id, topic),
        )
        row = cur.fetchone()
        if row:
            conn.execute(
                "UPDATE dsa_progress SET status = ?, updated_at = ? WHERE id = ?",
                (status, datetime.now().isoformat(), row["id"]),
            )
        else:
            conn.execute(
                "INSERT INTO dsa_progress (student_id, topic, status, updated_at) VALUES (?, ?, ?, ?)",
                (student_id, topic, status, datetime.now().isoformat()),
            )


def get_dsa_progress(student_id: int):
    with get_connection() as conn:
        cur = conn.execute(
            "SELECT * FROM dsa_progress WHERE student_id = ? ORDER BY id", (student_id,)
        )
        return [dict(r) for r in cur.fetchall()]


# ---------------------------------------------------------------------------
# Aptitude
# ---------------------------------------------------------------------------

def save_aptitude_score(student_id: int, topic: str, score: int, total: int):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO aptitude_scores (student_id, topic, score, total, created_at) VALUES (?, ?, ?, ?, ?)",
            (student_id, topic, score, total, datetime.now().isoformat()),
        )


def get_aptitude_scores(student_id: int):
    with get_connection() as conn:
        cur = conn.execute(
            "SELECT * FROM aptitude_scores WHERE student_id = ? ORDER BY id", (student_id,)
        )
        return [dict(r) for r in cur.fetchall()]


# ---------------------------------------------------------------------------
# Interview sessions (HR + Technical)
# ---------------------------------------------------------------------------

def save_interview_session(student_id: int, session_type: str, question: str, answer: str, feedback: str):
    with get_connection() as conn:
        conn.execute(
            """INSERT INTO interview_sessions
               (student_id, session_type, question, answer, feedback, created_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (student_id, session_type, question, answer, feedback, datetime.now().isoformat()),
        )


def get_interview_sessions(student_id: int, session_type: str = None):
    with get_connection() as conn:
        if session_type:
            cur = conn.execute(
                "SELECT * FROM interview_sessions WHERE student_id = ? AND session_type = ? ORDER BY id DESC",
                (student_id, session_type),
            )
        else:
            cur = conn.execute(
                "SELECT * FROM interview_sessions WHERE student_id = ? ORDER BY id DESC",
                (student_id,),
            )
        return [dict(r) for r in cur.fetchall()]


# ---------------------------------------------------------------------------
# Study plan
# ---------------------------------------------------------------------------

def save_study_plan(student_id: int, plan_text: str):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO study_plan (student_id, plan_text, created_at) VALUES (?, ?, ?)",
            (student_id, plan_text, datetime.now().isoformat()),
        )


def get_latest_study_plan(student_id: int):
    with get_connection() as conn:
        cur = conn.execute(
            "SELECT * FROM study_plan WHERE student_id = ? ORDER BY id DESC LIMIT 1",
            (student_id,),
        )
        row = cur.fetchone()
        return dict(row) if row else None


# ---------------------------------------------------------------------------
# Company research
# ---------------------------------------------------------------------------

def save_company_research(student_id: int, company: str, research: str):
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO company_research (student_id, company, research, created_at) VALUES (?, ?, ?, ?)",
            (student_id, company, research, datetime.now().isoformat()),
        )


def get_company_research_history(student_id: int):
    with get_connection() as conn:
        cur = conn.execute(
            "SELECT * FROM company_research WHERE student_id = ? ORDER BY id DESC",
            (student_id,),
        )
        return [dict(r) for r in cur.fetchall()]


# ---------------------------------------------------------------------------
# Progress summary (used by Progress Agent / dashboard)
# ---------------------------------------------------------------------------

def get_progress_summary(student_id: int) -> dict:
    resume = get_latest_resume(student_id)
    dsa = get_dsa_progress(student_id)
    aptitude = get_aptitude_scores(student_id)
    interviews = get_interview_sessions(student_id)

    dsa_done = len([d for d in dsa if d["status"] == "Completed"])
    dsa_total = len(dsa)

    apt_avg = 0
    if aptitude:
        apt_avg = round(
            sum(a["score"] / a["total"] for a in aptitude if a["total"]) / len(aptitude) * 100, 1
        )

    return {
        "ats_score": resume["ats_score"] if resume else 0,
        "dsa_done": dsa_done,
        "dsa_total": dsa_total,
        "aptitude_avg_pct": apt_avg,
        "aptitude_attempts": len(aptitude),
        "interview_sessions": len(interviews),
    }
