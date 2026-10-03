import csv
import os
import random

FILE_NAME = "guessing_game_scores.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Player", "Attempts"])


def play_game():
    create_file()

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

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([player, attempts])


def view_high_scores():
    create_file()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        rows = [row for row in reader if row]

    print("\n----------- HIGH SCORES (Fewest Attempts) -----------")
    if not rows:
        print("No games played yet.")
        return

    rows.sort(key=lambda r: int(r[1]))
    top = rows[:10]

    print("{:<5} {:<20} {:<10}".format("Rank", "Player", "Attempts"))
    for rank, row in enumerate(top, start=1):
        print("{:<5} {:<20} {:<10}".format(rank, row[0], row[1]))


def main():
    create_file()

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
