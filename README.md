# 🚀 AI Learning Path Generator

An AI-powered personalized learning roadmap generator built using **LangChain, Google Gemini, Pydantic, and Streamlit**.

The application takes a learner's topic, current skill level, learning goal, available duration, and weekly study hours, and generates a structured learning roadmap with stages, topics, practical projects, prerequisites, and a final project.

---

## 📌 Project Overview

Choosing what to learn and deciding how to learn it can be difficult, especially when there are many topics and resources available.

The **AI Learning Path Generator** solves this problem by generating a personalized and structured roadmap based on the learner's requirements.

Instead of providing a generic list of topics, the application creates a progressive learning path that:

- Starts from the user's current level
- Progresses from fundamentals to advanced concepts
- Matches the user's learning goal
- Considers the available learning duration
- Considers weekly study hours
- Includes practical projects
- Provides prerequisites
- Suggests a final project

---

## 🎯 Problem Statement

Learners often struggle with:

- Knowing where to start
- Choosing the correct sequence of topics
- Understanding what to learn next
- Planning their learning within a fixed duration
- Finding suitable practical projects
- Creating a job-oriented learning roadmap

This project uses **Generative AI and LangChain** to automatically create a personalized learning path.

---

## 💡 Solution

The application collects the following information:

1. Learning Topic
2. Current Skill Level
3. Learning Goal
4. Available Duration
5. Hours Available Per Week

The information is passed through a LangChain prompt and processed by the Gemini model.

The Gemini response is converted into a structured Pydantic object and displayed through a Streamlit interface.

---

# 🏗️ Architecture

```text
                         👤 User
                            │
                            ▼
                    🖥️ Streamlit UI
                            │
                            ▼
                     User Inputs
                            │
             ┌──────────────┼──────────────┐
             │              │              │
           Topic          Level           Goal
             │              │              │
             └──────────────┼──────────────┘
                            │
                    Duration + Hours
                            │
                            ▼
                 🧩 ChatPromptTemplate
                            │
                            ▼
                    🔗 LangChain Chain
                            │
                            ▼
                 🤖 Google Gemini
                            │
                            ▼
                📦 Pydantic Structured
                       Output
                            │
                            ▼
                  📚 Learning Path
                            │
                            ▼
                    🎨 Streamlit UI
                            │
                            ▼
                    👤 User Result
