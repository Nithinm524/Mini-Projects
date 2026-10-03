import sqlite3
import random

DB_NAME = "guessing_game.db"


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player TEXT NOT NULL,
            attempts INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def play_game():
    player = input("Enter Your Name: ").strip()
    if not player:
        print("Name cannot be empty!")
        return

    print("\nI'm thinking of a number between 1 and 100. Try to guess it!")
    target = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ").strip()

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < 1 or guess > 100:
            print("Guess must be between 1 and 100.")
        elif guess < target:
            print("Too Low!")
        elif guess > target:
            print("Too High!")
        else:
            print(f"\nCorrect! You guessed it in {attempts} attempts.")
            break

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scores (player, attempts) VALUES (?, ?)", (player, attempts))
    conn.commit()
    conn.close()


def view_high_scores():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT player, attempts FROM scores ORDER BY attempts ASC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()

    print("\n----------- HIGH SCORES (Fewest Attempts) -----------")
    if not rows:
        print("No games played yet.")
        return

    print("{:<5} {:<20} {:<10}".format("Rank", "Player", "Attempts"))
    for rank, row in enumerate(rows, start=1):
        print("{:<5} {:<20} {:<10}".format(rank, row[0], row[1]))


def main():
    create_table()

    while True:
        print("\n========== NUMBER GUESSING GAME ==========")
        print("1. Play Game")
        print("2. View High Scores")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            play_game()
        elif choice == "2":
            view_high_scores()
        elif choice == "3":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()
