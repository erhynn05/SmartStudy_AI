import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("study_data.csv")

# Convert risk labels to numbers
data["risk"] = data["risk"].map({
    "Low Risk": 0,
    "Medium Risk": 1,
    "High Risk": 2
})

# Features and labels
X = data[["confidence", "days_until_exam", "difficulty", "priority_score"]]
y = data["risk"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, predictions)

print("\n--- Model Evaluation ---")
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, predictions))
