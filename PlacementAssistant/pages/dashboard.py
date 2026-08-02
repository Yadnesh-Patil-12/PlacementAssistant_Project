import streamlit as st
import plotly.graph_objects as go

from database.database import get_progress_summary
from agents.coordinator import CoordinatorAgent

coordinator = CoordinatorAgent()


# ==========================================================
# KPI CARD
# ==========================================================

def progress_card(title, value):

    st.metric(
        label=title,
        value=value,
        border=True,
    )


# ==========================================================
# DASHBOARD
# ==========================================================

def render(student):

    summary = get_progress_summary(student["id"])

    # ------------------------------------------------------
    # HERO SECTION
    # ------------------------------------------------------

    st.title(f"🤖 Welcome, {student['name']}")

    st.success(
        f"""
AI Powered Placement Preparation Assistant

🎯 **Target Role:** {student['target_role']}
"""
    )

    st.divider()

    st.subheader("📊 Dashboard")

    # ------------------------------------------------------
    # KPI CARDS
    # ------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        progress_card(
            "📄 ATS Score",
            f"{summary['ats_score']}/100",
        )

    with c2:
        progress_card(
            "💻 DSA Progress",
            f"{summary['dsa_done']}/{summary['dsa_total']}",
        )

    with c3:
        progress_card(
            "🧮 Aptitude",
            f"{summary['aptitude_avg_pct']}%",
        )

    with c4:
        progress_card(
            "🎤 Interviews",
            str(summary["interview_sessions"]),
        )

    st.divider()

    left, right = st.columns([2, 1])
    
        # ==========================================================
    # PROGRESS CHART
    # ==========================================================

    with left:

        dsa_percent = 0

        if summary["dsa_total"] > 0:
            dsa_percent = (
                summary["dsa_done"] / summary["dsa_total"]
            ) * 100

        fig = go.Figure()

        fig.add_trace(
            go.Bar(
                x=[
                    "ATS",
                    "DSA",
                    "Aptitude",
                ],
                y=[
                    summary["ats_score"],
                    dsa_percent,
                    summary["aptitude_avg_pct"],
                ],
                marker_color=[
                    "#38BDF8",
                    "#8B5CF6",
                    "#22C55E",
                ],
                text=[
                    f"{summary['ats_score']}%",
                    f"{dsa_percent:.0f}%",
                    f"{summary['aptitude_avg_pct']}%",
                ],
                textposition="outside",
            )
        )

        fig.update_layout(
            title="📈 Overall Placement Progress",
            template="plotly_dark",
            height=400,
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font=dict(color="white"),
            yaxis=dict(
                title="Percentage",
                range=[0, 100],
            ),
            margin=dict(
                l=20,
                r=20,
                t=50,
                b=20,
            ),
        )

        st.plotly_chart(
            fig,
            width="stretch",
        )

    # ==========================================================
    # AI RECOMMENDATION
    # ==========================================================

    with right:

        st.subheader("🤖 AI Recommendations")

        recommendations = []

        if summary["ats_score"] < 90:
            recommendations.append(
                "📄 Improve your Resume ATS score to 90+."
            )

        if dsa_percent < 80:
            recommendations.append(
                "💻 Complete the remaining DSA roadmap."
            )

        if summary["aptitude_avg_pct"] < 75:
            recommendations.append(
                "🧮 Practise aptitude questions daily."
            )

        if summary["interview_sessions"] < 5:
            recommendations.append(
                "🎤 Attend more mock interviews."
            )

        if not recommendations:
            st.success(
                "🎉 Excellent! You're on track for placements."
            )
        else:
            for item in recommendations:
                st.info(item)

        st.caption(
            "Update your progress regularly to receive better AI recommendations."
        )

    st.divider()
    
        # ==========================================================
    # AI CAREER COORDINATOR
    # ==========================================================

    st.subheader("🤖 AI Career Coordinator")

    goal = st.text_area(
        "Career Goal",
        placeholder="Example: I have a Microsoft interview in 2 weeks. Create a study plan.",
        height=150,
    )

    if st.button("🚀 Generate Action Plan", use_container_width=True):

        if goal.strip() == "":
            st.warning("Please enter your career goal.")

        else:

            with st.spinner("Generating your personalized roadmap..."):

                try:

                    plan = coordinator.create_action_plan(
                        goal,
                        summary,
                    )

                    st.success("Action Plan Generated Successfully")

                    st.markdown("### 📋 Your Action Plan")

                    st.write(plan)

                except Exception as e:

                    st.error(f"Error: {e}")

    st.divider()

    # ==========================================================
    # QUICK ACTIONS
    # ==========================================================

    st.subheader("⚡ Quick Actions")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📄 Resume Analyzer", use_container_width=True):
            st.info("Open Resume Analyzer from the sidebar.")

    with col2:
        if st.button("💻 DSA Roadmap", use_container_width=True):
            st.info("Open DSA Roadmap from the sidebar.")

    with col3:
        if st.button("🧮 Aptitude", use_container_width=True):
            st.info("Open Aptitude Practice from the sidebar.")

    with col4:
        if st.button("🎤 Interview", use_container_width=True):
            st.info("Open Interview Practice from the sidebar.")

    st.divider()

    # ==========================================================
    # TODAY'S SUMMARY
    # ==========================================================

    st.subheader("📌 Today's Progress")

    progress = 0

    progress += summary["ats_score"]

    if summary["dsa_total"] > 0:
        progress += (
            summary["dsa_done"] / summary["dsa_total"]
        ) * 100

    progress += summary["aptitude_avg_pct"]

    progress += min(summary["interview_sessions"] * 20, 100)

    progress = progress / 4

    st.progress(progress / 100)

    st.write(f"Overall Preparation Score: **{progress:.1f}%**")

    if progress >= 80:
        st.success("🎉 Excellent! Keep it up.")
    elif progress >= 60:
        st.info("👍 Good progress. Stay consistent.")
    else:
        st.warning("⚠ Focus more on your preparation.")

    st.divider()

    # ==========================================================
    # FOOTER
    # ==========================================================

    st.caption(
        "🚀 Multi-Agent Placement Preparation Assistant | Built with Streamlit & Groq AI"
    )