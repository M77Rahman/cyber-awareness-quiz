print("🔐 Welcome to the Cyber Awareness Quiz!")
print("Answer the questions by typing A, B, C, or D.\n")

questions = [
    {
        "question": "What is phishing?",
        "options": ["A. A cooking method", "B. A cyber attack to steal data", "C. A video game", "D. A password manager"],
        "answer": "B"
    },
    {
        "question": "What makes a strong password?",
        "options": ["A. Just your name", "B. '123456'", "C. Mix of letters, numbers, and symbols", "D. Password"],
        "answer": "C"
    },
    {
        "question": "What should you do if you get a suspicious email?",
        "options": ["A. Click all the links", "B. Reply with your info", "C. Ignore or report it", "D. Print it"],
        "answer": "C"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    answer = input("Your answer: ").strip().upper()

    if answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

print(f"🎉 You got {score} out of {len(questions)} correct.")
