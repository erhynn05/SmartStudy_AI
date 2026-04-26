import csv
import os

DATA_FILE = "study_data.csv"


def calculate_priority(confidence, days_until_exam, difficulty):
    urgency_score = 10 - min(days_until_exam, 10)
    weakness_score = 6 - confidence
    difficulty_score = difficulty

    priority_score = urgency_score + weakness_score + difficulty_score
    return priority_score


def get_risk_level(priority_score):
    if priority_score >= 13:
        return "High Risk"
    elif priority_score >= 8:
        return "Medium Risk"
    else:
        return "Low Risk"


def get_recommendation(risk):
    if risk == "High Risk":
        return "Study this first. Review notes, videos, and practice questions."
    elif risk == "Medium Risk":
        return "Review this soon and focus on your weak areas."
    else:
        return "Do a light review to keep the topic fresh."


def save_to_csv(topics):
    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "topic",
                "confidence",
                "days_until_exam",
                "difficulty",
                "priority_score",
                "risk"
            ])

        for topic in topics:
            writer.writerow([
                topic["name"],
                topic["confidence"],
                topic["days_until_exam"],
                topic["difficulty"],
                topic["priority_score"],
                topic["risk"]
            ])


def main():
    print("Hello and Welcome to StudySmart AI!")
    print("This program creates a personalized study plan based on confidence, difficulty, and when your exam will take place.")

    topics = []

    num_topics = int(input("\nHow many topics do you want to add? "))

    for i in range(num_topics):
        print(f"\nTopic {i + 1}")

        name = input("Topic name: ")
        confidence = int(input("Confidence level (1-5): "))
        difficulty = int(input("Difficulty level (1-5): "))
        days_until_exam = int(input("Days until exam: "))

        priority_score = calculate_priority(confidence, days_until_exam, difficulty)
        risk = get_risk_level(priority_score)
        recommendation = get_recommendation(risk)

        topics.append({
            "name": name,
            "confidence": confidence,
            "difficulty": difficulty,
            "days_until_exam": days_until_exam,
            "priority_score": priority_score,
            "risk": risk,
            "recommendation": recommendation
        })

    topics.sort(key=lambda x: x["priority_score"], reverse=True)

    print("\n--- Personalized Study Plan ---")

    for topic in topics:
        print("\nTopic:", topic["name"])
        print("Confidence:", topic["confidence"])
        print("Difficulty:", topic["difficulty"])
        print("Days Until Exam:", topic["days_until_exam"])
        print("Priority Score:", topic["priority_score"])
        print("Risk Level:", topic["risk"])
        print("Recommendation:", topic["recommendation"])

    save_to_csv(topics)

    print("\nYour study data was saved to study_data.csv.")
    print("This dataset can be used later for machine learning evaluation.")


main()
