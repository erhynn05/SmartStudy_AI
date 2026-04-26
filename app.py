print("Hello and Welcome to StudySmart AI!")

topic = input("What topic are you currently studying? ")
confidence = int(input("Now rate your confidence on this topic (1-5): "))
days_until_exam = int(input("How many days do you have until your exam? "))

# Calculate risk level
if confidence <= 2 and days_until_exam <= 3:
    risk = "High Risk"
    recommendation = "Study this topic first. Spend extra time reviewing your notes, watching demonstrations, and doing practice questions."
elif confidence <= 3 or days_until_exam <= 5:
    risk = "Medium Risk"
    recommendation = "Review this topic soon. Do practice questions and focus on the parts your not too confident about."
else:
    risk = "Low Risk"
    recommendation = "You are doing okay with this topic. Do a quick review for a refresh."

print("\n--- StudySmart AI Recommendation ---")
print("Topic:", topic)
print("Risk Level:", risk)
print("Recommendation:", recommendation)
