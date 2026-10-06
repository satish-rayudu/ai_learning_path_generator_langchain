import streamlit as st
from backend import generate_learning_path


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Learning Path Generator",
    page_icon="🚀",
    layout="wide"
)


# =========================================================
# HEADER
# =========================================================

st.title("🚀 AI Learning Path Generator")

st.write(
    "Create a personalized learning roadmap "
    "using LangChain + Gemini."
)

st.divider()


# =========================================================
# USER INPUTS
# =========================================================

st.subheader("🎯 Tell us about your learning goal")

topic = st.text_input(
    "📚 What do you want to learn?",
    placeholder="Example: Generative AI"
)

level = st.selectbox(
    "📊 What is your current level?",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

goal = st.text_input(
    "💼 What is your goal?",
    placeholder="Example: Become job ready"
)

duration = st.selectbox(
    "⏳ How much time do you have?",
    [
        "4 weeks",
        "8 weeks",
        "12 weeks",
        "16 weeks",
        "24 weeks"
    ]
)

hours_per_week = st.number_input(
    "⏰ Hours available per week",
    min_value=1,
    max_value=40,
    value=10
)


st.divider()


# =========================================================
# GENERATE BUTTON
# =========================================================

generate_button = st.button(
    "🚀 Generate Learning Path",
    use_container_width=True
)


# =========================================================
# GENERATE LEARNING PATH
# =========================================================

if generate_button:

    if not topic.strip():

        st.warning("⚠️ Please enter a topic.")

    elif not goal.strip():

        st.warning("⚠️ Please enter your goal.")

    else:

        try:

            with st.spinner(
                "🤖 Creating your personalized learning path..."
            ):

                result = generate_learning_path(
                    topic=topic,
                    level=level,
                    goal=goal,
                    duration=duration,
                    hours_per_week=hours_per_week
                )


            st.success(
                "🎉 Learning path generated successfully!"
            )


            # =================================================
            # TITLE
            # =================================================

            st.header(f"🚀 {result.title}")


            # =================================================
            # OVERVIEW
            # =================================================

            st.subheader("📝 Overview")

            st.write(result.overview)


            # =================================================
            # PREREQUISITES
            # =================================================

            st.subheader("📋 Prerequisites")

            for prerequisite in result.prerequisites:

                st.write(f"✅ {prerequisite}")


            # =================================================
            # LEARNING STAGES
            # =================================================

            st.subheader("📚 Learning Stages")

            for index, stage in enumerate(
                result.stages,
                start=1
            ):

                with st.expander(
                    f"🎯 Stage {index}: "
                    f"{stage.stage} — {stage.duration}"
                ):

                    st.markdown("### 📖 Topics")

                    for topic_item in stage.topics:

                        st.write(
                            f"• {topic_item}"
                        )


                    st.markdown(
                        "### 🛠️ Practical Project"
                    )

                    st.info(stage.project)


            # =================================================
            # FINAL PROJECT
            # =================================================

            st.subheader("🏆 Final Project")

            st.success(result.final_project)


        except Exception as e:

            st.error(
                "❌ Something went wrong while generating "
                "the learning path."
            )

            st.exception(e)