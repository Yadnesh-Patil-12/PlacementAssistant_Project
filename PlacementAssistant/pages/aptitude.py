"""
pages/aptitude.py
Generates and scores a placement-style aptitude practice quiz.
"""

import streamlit as st

from agents.aptitude_agent import AptitudeAgent
from database.database import save_aptitude_score, get_aptitude_scores

aptitude_agent = AptitudeAgent()

TOPICS = [
    "Quantitative Aptitude",
    "Logical Reasoning",
    "Verbal Ability",
    "Data Interpretation",
    "Number Series",
    "Time, Speed & Distance",
    "Probability",
]


def render(student: dict):
    st.title("🧮 Aptitude Practice")
    st.caption("Generate a quick practice quiz and get instant scoring with explanations.")

    col1, col2, col3 = st.columns(3)
    with col1:
        topic = st.selectbox("Topic", TOPICS)
    with col2:
        difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    with col3:
        num_questions = st.slider("Number of Questions", 3, 10, 5)

    if st.button("Generate Quiz", type="primary"):
        with st.spinner("Aptitude Agent is preparing your quiz..."):
            quiz = aptitude_agent.generate_quiz(topic, difficulty, num_questions)
        if not quiz:
            st.error("Could not generate a valid quiz this time. Please try again.")
        else:
            st.session_state["aptitude_quiz"] = quiz
            st.session_state["aptitude_topic"] = topic
            st.session_state.pop("aptitude_submitted", None)

    quiz = st.session_state.get("aptitude_quiz")
    if quiz:
        st.divider()
        st.subheader(f"📝 Quiz: {st.session_state.get('aptitude_topic', topic)}")

        with st.form("aptitude_quiz_form"):
            responses = {}
            for i, q in enumerate(quiz):
                st.markdown(f"**Q{i + 1}. {q['question']}**")
                options_display = [f"{letter}) {text}" for letter, text in q["options"].items()]
                choice = st.radio(
                    f"Select answer for Q{i + 1}",
                    options_display,
                    key=f"apt_q_{i}",
                    label_visibility="collapsed",
                )
                responses[i] = choice[0] if choice else None
                st.write("")
            submitted = st.form_submit_button("Submit Quiz", type="primary")

        if submitted:
            score = sum(1 for i, q in enumerate(quiz) if responses.get(i) == q["answer"])
            total = len(quiz)
            save_aptitude_score(student["id"], st.session_state.get("aptitude_topic", topic), score, total)
            st.success(f"Score: {score} / {total}")

            for i, q in enumerate(quiz):
                is_correct = responses.get(i) == q["answer"]
                icon = "✅" if is_correct else "❌"
                st.markdown(f"{icon} **Q{i + 1}. {q['question']}**")
                st.caption(f"Correct answer: {q['answer']}) {q['options'].get(q['answer'], '')}  \n{q['explanation']}")

    st.divider()
    st.subheader("📈 Past Attempts")
    history = get_aptitude_scores(student["id"])
    if history:
        for row in reversed(history[-10:]):
            pct = round(row["score"] / row["total"] * 100) if row["total"] else 0
            st.write(f"- {row['topic']}: **{row['score']}/{row['total']}** ({pct}%) — {row['created_at'][:16]}")
    else:
        st.info("No quiz attempts yet.")
