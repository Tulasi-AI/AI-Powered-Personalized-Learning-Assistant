print("==========================================")
print(" AI-POWERED PERSONALIZED LEARNING ASSISTANT")
print(" SDG 4: QUALITY EDUCATION")
print("==========================================")

# Learning content
lessons = {
    "python": "Python is a programming language used to develop "
              "applications, websites, and AI systems.",

    "java": "Java is an object-oriented programming language "
            "used to develop software applications.",

    "ai": "Artificial Intelligence (AI) enables computers to "
          "perform tasks that normally require human intelligence.",

    "machine learning": "Machine Learning is a branch of AI "
                        "that allows computers to learn patterns "
                        "from data.",

    "excel": "Microsoft Excel is a spreadsheet application "
             "used to organize data and perform calculations."
}

# Practice questions
quizzes = {
    "python": {
        "question": "Which programming language are we using "
                    "to build this prototype?",
        "answer": "python"
    },

    "java": {
        "question": "Which language is known for object-oriented "
                    "programming and runs on the JVM?",
        "answer": "java"
    },

    "ai": {
        "question": "What does AI stand for?",
        "answer": "artificial intelligence"
    }
}

while True:
    print("\nWhat would you like to do?")
    print("1. Learn a topic")
    print("2. Take a quiz")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        topic = input(
            "Enter a topic (Python, Java, AI, "
            "Machine Learning, Excel): "
        ).lower().strip()

        if topic in lessons:
            print("\nExplanation:")
            print(lessons[topic])
        else:
            print("Sorry, this topic is not available yet.")
            print("Try Python, Java, AI, Machine Learning, or Excel.")

    elif choice == "2":
        topic = input(
            "Choose a quiz topic (Python, Java, AI): "
        ).lower().strip()

        if topic in quizzes:
            print("\nQuestion:")
            print(quizzes[topic]["question"])

            answer = input("Your answer: ").lower().strip()

            if answer == quizzes[topic]["answer"]:
                print("Correct! Excellent work.")
            else:
                print("Not quite. Let's review the topic.")
                print("Correct answer:",
                      quizzes[topic]["answer"])

        else:
            print("Quiz not available for this topic yet.")

    elif choice == "3":
        print("Thank you for using the Learning Assistant!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
