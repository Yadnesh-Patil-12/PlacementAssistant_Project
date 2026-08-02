# Multi-Agent Placement Preparation Assistant Using Agentic AI

A Streamlit application that coordinates multiple specialized AI agents to
guide a student through campus placement preparation — resume review, DSA
planning, aptitude practice, company research, HR & technical mock
interviews, study planning, and progress tracking.

Built for **Program Elective 4 — Agentic AI Design** (Third Year B.Tech
Computer Engineering).

## Architecture

```
Student → Coordinator Agent → [Resume | DSA | Aptitude | Company |
                                HR Interview | Technical | Study Planner |
                                Progress Tracker] Agents
                             → SQLite Database
                             → Groq LLM API
                             → Streamlit Dashboard
```

The **Coordinator Agent** doesn't do specialized work itself — it reads the
student's current goal and progress snapshot and recommends which
specialized agent to use next. Each specialized agent owns one part of the
placement journey and persists its results to a shared SQLite database so
the Progress Tracker can summarize everything in one place.

## Tech Stack

| Layer      | Technology |
|------------|------------|
| Frontend   | Streamlit |
| Backend    | Python |
| LLM        | Groq API (Llama 3.3) |
| Database   | SQLite |
| Libraries  | Pandas, Plotly, pypdf |

## Folder Structure

```
PlacementAssistant/
├── app.py                 # Streamlit entry point + navigation + login
├── config.py               # env vars, paths, constants
├── .env                     # GROQ_API_KEY (create your own, see below)
├── requirements.txt
├── database/
│   ├── database.py         # SQLite schema + all CRUD functions
│   └── student.db          # created automatically on first run
├── agents/
│   ├── coordinator.py      # Coordinator Agent
│   ├── resume_agent.py     # Resume Agent
│   ├── dsa_agent.py        # DSA Agent
│   ├── aptitude_agent.py   # Aptitude Agent
│   ├── company_agent.py    # Company Agent
│   ├── hr_agent.py         # HR Interview Agent
│   ├── technical_agent.py  # Technical Interview Agent
│   └── planner_agent.py    # Study Planner Agent
│   (progress_agent.py lives here too — analytics + insight)
├── pages/                  # One Streamlit page per feature
│   ├── dashboard.py
│   ├── resume.py
│   ├── dsa.py
│   ├── aptitude.py
│   ├── company.py
│   ├── interview.py
│   ├── planner.py
│   └── progress.py
├── utils/
│   ├── groq_api.py         # Groq API wrapper used by every agent
│   ├── resume_parser.py    # PDF text extraction
│   └── prompts.py          # All prompt templates
├── uploads/                # uploaded resumes land here
├── reports/                # reserved for exported reports
└── assets/                 # reserved for images/logos
```

## Setup (VS Code)

### 1. Get a free Groq API key
Sign up at **https://console.groq.com** → API Keys → Create Key.

### 2. Open the project folder in VS Code
`File → Open Folder → PlacementAssistant`

### 3. Create and activate a virtual environment

**Windows (PowerShell):**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Add your API key
Open `.env` and replace the placeholder:
```
GROQ_API_KEY=gsk_your_real_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

### 6. Run the app
```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`. The SQLite database
(`database/student.db`) is created automatically the first time you run it.

## Using the App

1. **Log in** with your name, email, and target role (no password — this is
   an academic prototype, not production auth).
2. **Dashboard** — ask the Coordinator Agent what to do next.
3. **Resume Analyzer** — upload a PDF resume for an ATS score + feedback.
4. **DSA Roadmap** — generate a roadmap and check off topics as you finish them.
5. **Aptitude Practice** — generate and attempt a scored quiz.
6. **Company Research** — get a prep briefing for a target company.
7. **Interview Practice** — practice HR and technical questions with AI feedback.
8. **Study Planner** — generate a day-by-day timetable.
9. **Progress Tracker** — view charts and an AI-generated insight.

## Notes for Evaluation

- All agent responses are generated live via the Groq LLM API, so an
  internet connection and a valid `GROQ_API_KEY` are required at runtime.
- Company research is based on the LLM's general knowledge (no live web
  search), and the UI notes this explicitly.
- The database is local (`SQLite`), so all data is per-machine — fine for a
  demo/unit-test setting.
