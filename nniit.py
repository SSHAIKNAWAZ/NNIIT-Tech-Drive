from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

DATA_FILE = "questions.json"

# Create the file if not exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Input model
class QuestionInput(BaseModel):
    question: str

# Output model
class QuestionOutput(BaseModel):
    topic: str
    confidence: float

# Simple rule-based classification
def classify_question(question: str) -> QuestionOutput:
    q_lower = question.lower()

    # Define keyword rules
    math_keywords = ["theorem", "triangle", "algebra", "geometry", "calculus"]
    science_keywords = ["photosynthesis", "gravity", "atom", "reaction", "planet"]
    english_keywords = ["grammar", "poem", "essay", "noun", "verb", "adjective"]

    scores = {"Math": 0, "Science": 0, "English": 0}




# GET endpoint to return past questions
@app.get("/questions")
def get_questions():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

