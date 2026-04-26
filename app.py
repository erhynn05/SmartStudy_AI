print("Hello and Welcome to StudySmart AI!")

topic = input("What topic are you currently studying? ")
confidence = int(input("Now rate your confidence on this topic (1-5): "))

if confidence <= 2:
    print("You should focus really on this topic.")
elif confidence == 3:
    print("You're improving, keep it going.")
else:
    print("Great work, just review lightly.")
