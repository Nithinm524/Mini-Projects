import sqlite3

DB_NAME = "quiz.db"

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


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player TEXT NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def take_quiz():
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

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO scores (player, score, total) VALUES (?, ?, ?)",
        (player, score, total)
    )
    conn.commit()
    conn.close()


def view_leaderboard():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT player, score, total FROM scores ORDER BY score DESC, id ASC")
    rows = cursor.fetchall()
    conn.close()

    print("\n----------- LEADERBOARD -----------")
    if not rows:
        print("No attempts recorded yet.")
        return

    print("{:<5} {:<20} {:<10}".format("Rank", "Player", "Score"))
    for rank, row in enumerate(rows, start=1):
        print("{:<5} {:<20} {:<10}".format(rank, row[0], f"{row[1]}/{row[2]}"))


def main():
    create_table()

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
