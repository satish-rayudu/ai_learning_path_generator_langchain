import os
from typing import List

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found")


os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY


# =========================================================
# PYDANTIC MODELS
# =========================================================

class LearningStage(BaseModel):

    stage: str = Field(
        description="Name of the learning stage"
    )

    duration: str = Field(
        description="Duration of this stage"
    )

    topics: List[str] = Field(
        description="Important topics to learn in this stage"
    )

    project: str = Field(
        description="Practical project for this stage"
    )


class LearningPath(BaseModel):

    title: str = Field(
        description="Title of the learning roadmap"
    )

    overview: str = Field(
        description="Short overview of the roadmap"
    )

    prerequisites: List[str] = Field(
        description="Prerequisites required before starting"
    )

    stages: List[LearningStage] = Field(
        description="Ordered learning stages"
    )

    final_project: str = Field(
        description="Final project recommendation"
    )


# =========================================================
# GEMINI MODEL
# =========================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.7
)


# =========================================================
# PROMPT
# =========================================================

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert learning path designer.

Create a practical and realistic learning roadmap
based on the user's requirements.

The roadmap must:

1. Start from the user's current level.
2. Progress from fundamentals to advanced concepts.
3. Include practical projects.
4. Respect the available duration.
5. Match the user's goal.
6. Avoid unnecessary topics.
"""
    ),

    (
        "human",
        """
Create a learning path for:

Topic: {topic}

Current Level: {level}

Goal: {goal}

Duration: {duration}

Hours Available Per Week: {hours_per_week}
"""
    )
])


# =========================================================
# STRUCTURED OUTPUT
# =========================================================

structured_llm = llm.with_structured_output(LearningPath)


# =========================================================
# LANGCHAIN CHAIN
# =========================================================

chain = prompt | structured_llm


# =========================================================
# GENERATE LEARNING PATH
# =========================================================

def generate_learning_path(
    topic,
    level,
    goal,
    duration,
    hours_per_week
):

    result = chain.invoke({
        "topic": topic,
        "level": level,
        "goal": goal,
        "duration": duration,
        "hours_per_week": hours_per_week
    })

    return result