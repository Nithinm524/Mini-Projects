import csv
import os

FILE_NAME = "quiz_scores.csv"

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 3
    },
    {
        "question": "Which language is Python named after?",
        "options": ["A snake", "Monty Python", "A programmer", "A movie"],
        "answer": 2
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Process Unit", "Central Processing Unit",
                     "Computer Personal Unit", "Central Processor Utility"],
        "answer": 2
    },
    {
        "question": "Which data structure uses FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": 2
    },
    {
        "question": "What is 2 to the power of 10?",
        "options": ["512", "1000", "1024", "2048"],
        "answer": 3
    },
]


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Player", "Score", "Total"])


def take_quiz():
    create_file()

    player = input("Enter Your Name: ").strip()
    if not player:
        print("Name cannot be empty!")
        return

    score = 0
    total = len(QUESTIONS)

    for i, q in enumerate(QUESTIONS, start=1):
        print(f"\nQ{i}. {q['question']}")
        for idx, option in enumerate(q["options"], start=1):
            print(f"  {idx}. {option}")

        choice = input("Your Answer (1-4): ").strip()
        if choice.isdigit() and int(choice) == q["answer"]:
            print("Correct!")
            score += 1
        else:
            correct_option = q["options"][q["answer"] - 1]
            print(f"Wrong! Correct answer: {correct_option}")

    print(f"\nQuiz Over! {player}, you scored {score}/{total}")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([player, score, total])


def view_leaderboard():
    create_file()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        rows = [row for row in reader if row]

    print("\n----------- LEADERBOARD -----------")
    if not rows:
        print("No attempts recorded yet.")
        return

    rows.sort(key=lambda r: int(r[1]), reverse=True)

    print("{:<5} {:<20} {:<10}".format("Rank", "Player", "Score"))
    for rank, row in enumerate(rows, start=1):
        print("{:<5} {:<20} {:<10}".format(rank, row[0], f"{row[1]}/{row[2]}"))


def main():
    create_file()

    while True:
        print("\n========== QUIZ APP ==========")
        print("1. Take Quiz")
        print("2. View Leaderboard")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            take_quiz()
        elif choice == "2":
            view_leaderboard()
        elif choice == "3":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()
