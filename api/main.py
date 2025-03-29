from fastapi import FastAPI, File, Form, UploadFile
import json
import os

app = FastAPI()

# Load all assignments data
assignments_dir = "assignments"
assignments = {}

# Read each JSON file and create a question-answer mapping
for filename in os.listdir(assignments_dir):
    if filename.endswith(".json"):
        path = os.path.join(assignments_dir, filename)
        with open(path, "r") as file:
            data = json.load(file)
            # Create a mapping of question_id to answer
            for item in data:
                assignments[item["question_id"]] = item["answer"]

@app.post("/api/")
async def get_answer(question: str = Form(...)):
    # Search for the question in assignments
    answer = assignments.get(question, "Question not found.")
    return {"answer": answer}

