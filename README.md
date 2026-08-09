# 🤖 Placement Assistant — Multi-Agent AI

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" alt="Python">

<img src="https://img.shields.io/badge/AI-Agentic%20AI-purple?style=for-the-badge" alt="Agentic AI">

<img src="https://img.shields.io/badge/LLM-Groq-orange?style=for-the-badge" alt="Groq">

<img src="https://img.shields.io/badge/UI-Streamlit-red?style=for-the-badge&logo=streamlit" alt="Streamlit">

<img src="https://img.shields.io/badge/Database-SQLite-blue?style=for-the-badge" alt="SQLite">

</p>

<p align="center">
  <b>🚀 An AI-powered Multi-Agent Placement Preparation Assistant</b>
</p>

<p align="center">
  <i>One platform to prepare for Resume Screening, DSA, Aptitude, Companies, Interviews and Study Planning.</i>
</p>

---

## 📌 Overview

**Placement Assistant** is an **Agentic AI-based placement preparation platform** designed to help students prepare for campus recruitment through multiple specialized AI agents.

Instead of using one general-purpose chatbot for every task, the system uses a **Coordinator Agent** that understands the student's current goal and directs the request to the most suitable specialized agent.

### 🎯 The system helps students with:

* 📄 Resume Analysis
* 🧠 DSA Preparation
* 🧮 Aptitude Practice
* 🏢 Company Research
* 🎤 HR Interview Preparation
* 💻 Technical Interview Preparation
* 📅 Study Planning
* 📊 Progress Tracking

---

# 🧠 Multi-Agent Architecture

```text
                         👨‍🎓 STUDENT
                              │
                              ▼
                  ┌─────────────────────┐
                  │  🎯 COORDINATOR     │
                  │       AGENT         │
                  └──────────┬──────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
    📄 Resume            🧠 DSA             🧮 Aptitude
      Agent              Agent                Agent
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
    🏢 Company          🎤 HR Interview    💻 Technical
      Agent                Agent             Agent
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                  ┌──────────▼──────────┐
                  │ 📅 Study Planner    │
                  │ 📊 Progress Tracker │
                  └──────────┬──────────┘
                             │
                             ▼
                    🗄️ SQLite Database
                             │
                             ▼
                     📊 STREAMLIT UI
```

---

# ⭐ Key Features

## 📄 1. AI Resume Analyzer

Upload your resume in PDF format and receive AI-generated feedback.

### Features

* 📤 PDF Resume Upload
* 📊 ATS-style Resume Score
* 🔍 Resume Analysis
* 💡 Improvement Suggestions
* 📝 AI-generated Feedback

---

## 🧠 2. DSA Roadmap Generator

Generate a personalized DSA preparation roadmap.

### Covers

```text
Arrays
  ↓
Strings
  ↓
Searching
  ↓
Sorting
  ↓
Linked List
  ↓
Stack & Queue
  ↓
Trees
  ↓
Graphs
  ↓
Dynamic Programming
```

Students can track completed topics and continue their preparation progressively.

---

## 🧮 3. Aptitude Practice

AI-generated aptitude quizzes for placement preparation.

### Includes

* 🔢 Quantitative Aptitude
* 🧠 Logical Reasoning
* 📊 Data Interpretation
* ❓ Multiple Choice Questions
* 📈 Score Tracking
* 💡 AI Feedback

---

## 🏢 4. Company Research Agent

Enter a target company and receive a preparation briefing.

### Provides

* 🏢 Company Overview
* 💼 Expected Roles
* 🧠 Technical Preparation
* 🎤 HR Preparation
* 📚 Recommended Topics
* 🎯 Interview Preparation Guidance

> **Note:** Company research is generated using the LLM's general knowledge and does not perform live web research.

---

## 🎤 5. HR Interview Agent

Practice common HR interview questions with AI.

Examples:

```text
"Tell me about yourself."

"What are your strengths and weaknesses?"

"Why should we hire you?"

"Where do you see yourself in 5 years?"

"Why do you want to join our company?"
```

The agent provides feedback to help improve answers.

---

## 💻 6. Technical Interview Agent

Practice technical questions based on core CS subjects.

### Topics

* 💻 C++
* 🧠 OOP
* 🗄️ DBMS
* ⚙️ Operating Systems
* 🌐 Computer Networks
* 📊 DSA
* 🐍 Python
* 🧮 SQL

---

## 📅 7. AI Study Planner

Generate personalized study schedules based on:

* Target role
* Available time
* Preparation goals
* Current progress
* Target company

Example:

```text
Day 1
├── Arrays
├── SQL Basics
└── Aptitude Practice

Day 2
├── Strings
├── OOP
└── Logical Reasoning

Day 3
├── Linked List
├── DBMS
└── Mock Interview
```

---

## 📊 8. Progress Tracker

Track preparation progress from a centralized dashboard.

### Tracks

* 📚 DSA Progress
* 🧮 Aptitude Scores
* 📄 Resume Status
* 🎤 Interview Practice
* 📅 Study Progress
* 📈 Overall Preparation

---

# ⚙️ Technology Stack

| Layer              | Technology    |
| ------------------ | ------------- |
| 🖥️ Frontend       | Streamlit     |
| 🐍 Backend         | Python        |
| 🤖 AI / LLM        | Groq API      |
| 🧠 Model           | Llama 3.3     |
| 🗄️ Database       | SQLite        |
| 📊 Data Analysis   | Pandas        |
| 📈 Visualization   | Plotly        |
| 📄 PDF Processing  | pypdf         |
| 🔐 Configuration   | python-dotenv |
| 🛠️ Development    | VS Code       |
| 🌐 Version Control | Git & GitHub  |

---

# 🏗️ Project Architecture

The project follows a **modular multi-agent architecture**.

```text
                         ┌───────────────┐
                         │   Streamlit   │
                         │   Dashboard   │
                         └───────┬───────┘
                                 │
                                 ▼
                      ┌────────────────────┐
                      │ Coordinator Agent  │
                      └─────────┬──────────┘
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
     Resume Agent          DSA Agent           Aptitude Agent
          │                     │                     │
          ▼                     ▼                     ▼
     Company Agent        HR Agent          Technical Agent
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                │
                                ▼
                       Study Planner Agent
                                │
                                ▼
                       Progress Tracker
                                │
                                ▼
                         SQLite Database
```

---

# 📂 Project Structure

```text
PlacementAssistant_Project/
│
├── 📁 PlacementAssistant/
│   │
│   ├── 📄 app.py
│   │
│   ├── 📄 config.py
│   ├── 📄 requirements.txt
│   │
│   ├── 📁 agents/
│   │   ├── coordinator.py
│   │   ├── resume_agent.py
│   │   ├── dsa_agent.py
│   │   ├── aptitude_agent.py
│   │   ├── company_agent.py
│   │   ├── hr_agent.py
│   │   ├── technical_agent.py
│   │   ├── planner_agent.py
│   │   └── progress_agent.py
│   │
│   ├── 📁 database/
│   │   ├── database.py
│   │   └── student.db
│   │
│   ├── 📁 pages/
│   │   ├── dashboard.py
│   │   ├── resume.py
│   │   ├── dsa.py
│   │   ├── aptitude.py
│   │   ├── company.py
│   │   ├── interview.py
│   │   ├── planner.py
│   │   └── progress.py
│   │
│   ├── 📁 utils/
│   │   ├── groq_api.py
│   │   ├── resume_parser.py
│   │   └── prompts.py
│   │
│   ├── 📁 uploads/
│   ├── 📁 reports/
│   └── 📁 assets/
│
├── 📄 .gitignore
├── 📄 README.md
└── 📄 Screenshot Demonstration.pdf
```

---

# 🔄 How the System Works

```text
             👨‍🎓 Student
                  │
                  ▼
          Enter Goal / Request
                  │
                  ▼
        🎯 Coordinator Agent
                  │
          Understands Intent
                  │
                  ▼
      Selects Specialized Agent
                  │
                  ▼
       🤖 Agent Processes Request
                  │
                  ▼
            Groq LLM API
                  │
                  ▼
          Generates Response
                  │
                  ▼
         🗄️ Save to SQLite
                  │
                  ▼
         📊 Update Dashboard
                  │
                  ▼
             👨‍🎓 Student
```

---

# 🧩 Agent Responsibilities

| Agent              | Responsibility                            |
| ------------------ | ----------------------------------------- |
| 🎯 Coordinator     | Understands user goal and routes requests |
| 📄 Resume Agent    | Resume analysis and improvement           |
| 🧠 DSA Agent       | DSA roadmap and preparation               |
| 🧮 Aptitude Agent  | Generate aptitude practice                |
| 🏢 Company Agent   | Company preparation guidance              |
| 🎤 HR Agent        | HR interview practice                     |
| 💻 Technical Agent | Technical interview practice              |
| 📅 Planner Agent   | Personalized study timetable              |
| 📊 Progress Agent  | Progress analytics and insights           |

---

# 🗄️ Database

The application uses **SQLite** for local data persistence.

The database stores information related to:

```text
Student
   │
   ├── Profile
   ├── Resume Analysis
   ├── DSA Progress
   ├── Aptitude Scores
   ├── Interview Practice
   ├── Study Plans
   └── Progress Analytics
```

The database is created automatically when the application is started.

---

# 🔐 Environment Variables

Create a `.env` file inside the `PlacementAssistant` folder.

```env
GROQ_API_KEY=gsk_your_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

⚠️ **Never commit your real API key to GitHub.**

The `.env` file should be included in `.gitignore`.

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Yadnesh-Patil-12/PlacementAssistant_Project.git
```

---

## 2️⃣ Navigate to Project

```bash
cd PlacementAssistant_Project
cd PlacementAssistant
```

---

## 3️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Configure Groq API

Create `.env`:

```env
GROQ_API_KEY=gsk_your_real_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

---

## 6️⃣ Run Application

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

# 🖥️ Application Workflow

```text
Login
  ↓
Dashboard
  ↓
Choose Preparation Area
  │
  ├── Resume
  ├── DSA
  ├── Aptitude
  ├── Company
  ├── HR Interview
  ├── Technical Interview
  ├── Study Planner
  └── Progress
  ↓
AI Processing
  ↓
Result + Feedback
  ↓
Progress Saved
```

---

# 📸 Screenshots & Demonstration

A complete application demonstration is available in:

📄 **`Screenshot Demonstration.pdf`**

The demonstration covers the major application screens and workflow.

> 💡 You can also add screenshots directly to the repository under `assets/` and display them here.

Example:

```markdown
![Dashboard](assets/dashboard.png)
```

---

# 🎓 Academic Context

### Program Elective 4 — Agentic AI Design

**Project Type:** Academic Project
**Domain:** Artificial Intelligence / Agentic AI
**Application Area:** Education & Career Development

### 🎯 Problem Statement

Students preparing for campus placements often use multiple disconnected resources for:

* Resume preparation
* DSA
* Aptitude
* Company research
* Interview preparation
* Study planning
* Progress tracking

This project brings these activities together into a **single AI-powered multi-agent platform**.

---

# 💡 Why Multi-Agent AI?

A single AI assistant may provide generic responses for different placement tasks.

This project separates responsibilities into specialized agents.

```text
                 Coordinator
                     │
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
   Resume           DSA          Aptitude
   Agent            Agent          Agent
      │              │              │
      ▼              ▼              ▼
   Company           HR          Technical
    Agent           Agent          Agent
```

### Benefits

* 🎯 Specialized responsibilities
* 🧩 Modular architecture
* 🔄 Easier maintenance
* 📈 Better scalability
* 🧠 Task-specific prompts
* 📊 Centralized progress tracking

---

# 🚀 Future Enhancements

Planned improvements include:

* [ ] 🌐 Live company research using web search
* [ ] 🤖 More specialized AI agents
* [ ] 🎤 Voice-based mock interviews
* [ ] 📄 Advanced ATS resume scoring
* [ ] 🧠 Adaptive DSA recommendations
* [ ] 📊 Advanced analytics dashboard
* [ ] 🔔 Study reminders
* [ ] 🏆 Gamification & achievement system
* [ ] ☁️ Cloud database
* [ ] 🔐 Production-level authentication
* [ ] 📱 Mobile-friendly interface
* [ ] 🚀 Cloud deployment

---

# ⚠️ Current Limitations

This project is currently an **academic prototype**.

* Authentication is not production-grade.
* SQLite is used for local storage.
* Company research does not use live web search.
* Internet connectivity is required for LLM requests.
* A valid Groq API key is required.
* The application is primarily designed for demonstration and educational purposes.

---

# 🧪 Example Use Case

### Student Goal

> "I have a placement interview next week for a software developer role."

The Coordinator Agent can determine that the student may need:

```text
🎯 Coordinator
       │
       ├── 📄 Resume Review
       │
       ├── 🧠 DSA Preparation
       │
       ├── 💻 Technical Interview
       │
       ├── 🎤 HR Interview
       │
       └── 📅 Study Plan
```

The student's activities and results can then contribute to the overall progress dashboard.

---

# 📈 Project Highlights

```text
🤖 Multi-Agent Architecture
       +
🧠 LLM-Powered Assistance
       +
📊 Progress Analytics
       +
🗄️ Persistent Database
       +
🎯 Personalized Preparation
       =
🚀 AI Placement Assistant
```

---

# 🛠️ Skills Demonstrated

Through this project, the following concepts are demonstrated:

* Python Programming
* Agentic AI Architecture
* LLM Integration
* Prompt Engineering
* Streamlit Development
* SQLite Database
* CRUD Operations
* PDF Processing
* Data Visualization
* Modular Software Architecture
* Git & GitHub
* AI-powered Application Development

---

# 👨‍💻 Author

## Yadnesh Patil

🎓 Computer Engineering Student
💻 Python | C++ | DSA | SQL
🤖 AI & Agentic AI Enthusiast
🔐 Cybersecurity Enthusiast
🎯 Preparing for Software Engineering & Technical Placements

---

# ⭐ Support

If you find this project useful:

⭐ **Star this repository**

🍴 **Fork the repository**

📚 **Explore the code**

💡 **Suggest improvements**

---

<p align="center">

### 🚀 Learn • Build • Experiment • Improve

<b>Made with Python, AI & ☕</b>

</p>
