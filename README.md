# StudySmart AI

StudySmart AI is a personalized study planning system that helps students decide what topics to study first based on confidence level, topic difficulty, and how soon the exam is.

## Problem

As a student I often struggle with deciding what to study first. Students may sometimes spend too much time reviewing topics they already understand while avoiding harder or more urgent topics.

## Solution

StudySmart AI asks the user for:
- topic name
- confidence level
- difficulty level
- days until exam

The program then calculates a priority score, classifies each topic as Low Risk, Medium Risk, or High Risk, and with all the information given, it gives a study recommendation.

## AI Techniques Used

- Rule-based decision making
- Risk classification
- Priority scoring
- Personalized recommendations
- Dataset collection using CSV

## How It Works

1. User enters study topics.
2. The system calculates a priority score.
3. Topics are sorted from highest priority to lowest priority.
4. The system gives a risk level and recommendation.
5. Data is saved into `study_data.csv`.

## Files in This Project

- `app.py` - runs the StudySmart AI study planner
- `model.py` - trains and evaluates the machine learning model
- `study_data.csv` - stores user study data
- `README.md` - explains the project
- `app_output.png` - screenshot of the study planner output
- `model_output.png` - screenshot of the model evaluation output

## How to Run

Run the study planner:

```bash
python3 app.py
