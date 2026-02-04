import random

# Flashcards stored as question: answer
flashcards = {
    "What is the capital of France?": "paris",
    "What keyword is used to define a function in Python?": "def",
    "What data type is returned by input()?": "string",
    "What symbol is used for comments in Python?": "#",
    "What does len() do?": "returns length"
}

correct = 0
incorrect = 0

questions = list(flashcards.keys())
random.shuffle(questions)

print("📘 Flashcard App (type 'quit' to exit)\n")

for question in questions:
    print("Question:", question)
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == "quit":
        break

    correct_answer = flashcards[question].lower()

    if user_answer == correct_answer:
        print("✅ Correct!\n")
        correct += 1
    else:
        print(f"❌ Incorrect. Correct answer: {flashcards[question]}\n")
        incorrect += 1

# Final score
print("📊 Results")
print("Correct:", correct)
print("Incorrect:", incorrect)
print("Total Questions Answered:", correct + incorrect)
