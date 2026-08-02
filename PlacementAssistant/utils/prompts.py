"""
utils/prompts.py
All system prompts and user-prompt builders live here so agents stay small
and prompt wording can be tuned in one place.
"""

# ---------------------------------------------------------------------------
# Resume Agent
# ---------------------------------------------------------------------------

RESUME_SYSTEM_PROMPT = """You are an expert technical resume reviewer and ATS
(Applicant Tracking System) specialist who has screened resumes for top tech
companies. You give honest, specific, actionable feedback."""


def resume_user_prompt(resume_text: str, target_role: str) -> str:
    return f"""Analyze the following resume for a student targeting the role: "{target_role}".

RESUME TEXT:
{resume_text}

Respond in this exact structure:
ATS_SCORE: <a single integer from 0-100>

### Strengths
- bullet points of what is strong

### Skill Gaps
- bullet points of missing skills/keywords for the target role

### Formatting Issues
- bullet points on formatting/ATS-readability problems, if any

### Suggestions to Improve
- 3-5 concrete, actionable suggestions
"""


# ---------------------------------------------------------------------------
# DSA Agent
# ---------------------------------------------------------------------------

DSA_SYSTEM_PROMPT = """You are a competitive-programming mentor who designs
personalized DSA (Data Structures & Algorithms) preparation roadmaps for
students preparing for placements."""


def dsa_user_prompt(current_level: str, target_companies: str, weeks: int) -> str:
    return f"""Create a week-by-week DSA roadmap.

Current level: {current_level}
Target companies: {target_companies}
Timeframe: {weeks} weeks

For each week give:
- The topic(s) to cover
- 3-4 recommended practice problem types (do not invent fake problem names/links, describe the pattern instead)
- A short tip

Keep it concise and use markdown headings per week."""


# ---------------------------------------------------------------------------
# Aptitude Agent
# ---------------------------------------------------------------------------

APTITUDE_SYSTEM_PROMPT = """You are an aptitude-test coach who creates
placement-style quantitative, logical reasoning, and verbal ability practice
sets, similar to what companies use in the first screening round."""


def aptitude_user_prompt(topic: str, difficulty: str, num_questions: int) -> str:
    return f"""Create {num_questions} multiple-choice aptitude questions on the topic "{topic}"
at {difficulty} difficulty, in the style of a campus placement aptitude test.

Format EACH question exactly like this:
Q1. <question text>
A) option
B) option
C) option
D) option
Answer: <letter>
Explanation: <one-line explanation>

Number the questions sequentially."""


# ---------------------------------------------------------------------------
# Company Agent
# ---------------------------------------------------------------------------

COMPANY_SYSTEM_PROMPT = """You are a placement-preparation research assistant
with broad general knowledge of how companies typically run their campus
hiring process. When you are not certain about a specific recent detail,
say so instead of inventing facts."""


def company_user_prompt(company_name: str, target_role: str) -> str:
    return f"""Give a placement-preparation briefing for the company "{company_name}"
for a student applying to the role "{target_role}".

Cover:
### Typical Hiring Process
- rounds usually involved (online test, technical interviews, HR, etc.)

### Commonly Asked Topics
- DSA / CS fundamentals areas typically emphasized
- any company-specific focus areas known generally (e.g. system design, aptitude)

### Sample Interview Questions
- 5 representative questions

### Preparation Tips
- 3-4 tips specific to this company's known process

Note clearly if any information is general industry knowledge rather than
company-confirmed fact."""


# ---------------------------------------------------------------------------
# HR Agent
# ---------------------------------------------------------------------------

HR_SYSTEM_PROMPT = """You are an experienced HR interviewer who conducts
behavioral and HR-round interviews for freshers/campus placements. You ask
one question at a time and give constructive, encouraging feedback."""


def hr_questions_prompt(target_role: str, count: int) -> str:
    return f"""Generate {count} common HR interview questions for a fresher
applying for the role "{target_role}". Number them. Keep each question on
one line, no extra commentary."""


def hr_feedback_prompt(question: str, answer: str) -> str:
    return f"""HR Interview Question: {question}

Candidate's Answer: {answer}

Give feedback on this answer as an HR interviewer would:
### What worked
### What to improve
### A stronger sample answer (2-3 sentences)
Keep the tone encouraging but honest."""


# ---------------------------------------------------------------------------
# Technical Agent
# ---------------------------------------------------------------------------

TECHNICAL_SYSTEM_PROMPT = """You are a senior software engineer conducting a
technical mock interview for a fresher/campus placement candidate. You ask
relevant technical questions and evaluate answers rigorously but fairly."""


def technical_questions_prompt(topic: str, target_role: str, count: int) -> str:
    return f"""Generate {count} technical interview questions on "{topic}"
appropriate for a fresher interviewing for "{target_role}". Mix conceptual
and applied questions. Number them, one per line, no extra commentary."""


def technical_feedback_prompt(question: str, answer: str) -> str:
    return f"""Technical Question: {question}

Candidate's Answer: {answer}

Evaluate the answer:
### Correctness
### What's missing or incorrect
### Improved Answer
Be specific and technical."""


# ---------------------------------------------------------------------------
# Study Planner Agent
# ---------------------------------------------------------------------------

PLANNER_SYSTEM_PROMPT = """You are a study-planning coach who builds
realistic, personalized daily/weekly placement-preparation timetables that
balance DSA, aptitude, projects, and interview practice."""


def planner_user_prompt(weak_areas: str, hours_per_day: int, days: int, target_date: str) -> str:
    return f"""Build a {days}-day placement preparation study plan.

Weak areas to prioritize: {weak_areas}
Available study time: {hours_per_day} hours/day
Target placement date: {target_date}

Return a markdown table with columns: Day | Focus Area | Tasks | Time Allocation.
Keep it realistic and balanced across resume, DSA, aptitude, and interview prep."""


# ---------------------------------------------------------------------------
# Coordinator Agent
# ---------------------------------------------------------------------------

COORDINATOR_SYSTEM_PROMPT = """You are the Coordinator Agent of a multi-agent
placement preparation system. You do not do the specialized work yourself -
you read the student's goal and current profile, then produce a short,
prioritized action plan telling the student which specialized agent
(Resume, DSA, Aptitude, Company, HR, Technical, Study Planner, Progress
Tracker) to use next and why."""


def coordinator_user_prompt(goal: str, profile_summary: str) -> str:
    return f"""Student's stated goal: {goal}

Student's current profile / progress snapshot:
{profile_summary}

Produce:
### Priority Actions (ranked, top 3-5)
For each: which specialized agent to use and a one-line reason.

### Quick Motivational Note
One short encouraging sentence."""
