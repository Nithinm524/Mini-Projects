import sqlite3

DB_NAME = "voting.db"


def create_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS polls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            poll_id INTEGER NOT NULL,
            option_text TEXT NOT NULL,
            votes INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (poll_id) REFERENCES polls(id)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS voters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            poll_id INTEGER NOT NULL,
            voter_name TEXT NOT NULL,
            UNIQUE(poll_id, voter_name)
        )
    """)
    conn.commit()
    conn.close()


def create_poll():
    question = input("Enter Poll Question: ").strip()
    if not question:
        print("Question cannot be empty!")
        return

    count = input("How many options? (min 2): ").strip()
    if not count.isdigit() or int(count) < 2:
        print("You must enter at least 2 options.")
        return
    count = int(count)

    options = []
    for i in range(1, count + 1):
        opt = input(f"Enter Option {i}: ").strip()
        if not opt:
            print("Option text cannot be empty. Poll creation cancelled.")
            return
        options.append(opt)

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO polls (question) VALUES (?)", (question,))
    poll_id = cursor.lastrowid

    for opt in options:
        cursor.execute(
            "INSERT INTO options (poll_id, option_text, votes) VALUES (?, ?, 0)",
            (poll_id, opt)
        )

    conn.commit()
    conn.close()
    print(f"Poll created successfully! Poll ID: {poll_id}")


def view_polls():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM polls ORDER BY id")
    rows = cursor.fetchall()
    conn.close()

    print("\n----------- ALL POLLS -----------")
    if not rows:
        print("No polls found.")
        return

    print("{:<5} {:<40}".format("ID", "Question"))
    for row in rows:
        print("{:<5} {:<40}".format(row[0], row[1]))


def vote():
    poll_id = input("Enter Poll ID to Vote On: ").strip()
    if not poll_id.isdigit():
        print("Invalid Poll ID.")
        return

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM polls WHERE id = ?", (poll_id,))
    poll = cursor.fetchone()
    if not poll:
        print("Poll not found.")
        conn.close()
        return

    cursor.execute("SELECT * FROM options WHERE poll_id = ?", (poll_id,))
    options = cursor.fetchall()

    print(f"\n{poll[1]}")
    for opt in options:
        print(f"  {opt[0]}. {opt[2]}")

    voter_name = input("Enter Your Name: ").strip()
    if not voter_name:
        print("Name cannot be empty!")
        conn.close()
        return

    option_id = input("Enter Option ID to Vote: ").strip()
    if not option_id.isdigit() or int(option_id) not in [o[0] for o in options]:
        print("Invalid Option ID.")
        conn.close()
        return

    try:
        cursor.execute(
            "INSERT INTO voters (poll_id, voter_name) VALUES (?, ?)",
            (poll_id, voter_name)
        )
    except sqlite3.IntegrityError:
        print("You have already voted on this poll.")
        conn.close()
        return

    cursor.execute("UPDATE options SET votes = votes + 1 WHERE id = ?", (option_id,))
    conn.commit()
    conn.close()
    print("Vote cast successfully!")


def view_results():
    poll_id = input("Enter Poll ID to View Results: ").strip()
    if not poll_id.isdigit():
        print("Invalid Poll ID.")
        return

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM polls WHERE id = ?", (poll_id,))
    poll = cursor.fetchone()
    if not poll:
        print("Poll not found.")
        conn.close()
        return

    cursor.execute("SELECT * FROM options WHERE poll_id = ?", (poll_id,))
    options = cursor.fetchall()
    conn.close()

    total_votes = sum(opt[3] for opt in options)

    print(f"\n----------- RESULTS: {poll[1]} -----------")
    print("{:<20} {:<10} {:<10}".format("Option", "Votes", "Percent"))
    for opt in options:
        percent = (opt[3] / total_votes * 100) if total_votes else 0
        print("{:<20} {:<10} {:<9.1f}%".format(opt[2], opt[3], percent))
    print(f"\nTotal Votes: {total_votes}")


def delete_poll():
    poll_id = input("Enter Poll ID to Delete: ").strip()
    if not poll_id.isdigit():
        print("Invalid Poll ID.")
        return

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM polls WHERE id = ?", (poll_id,))
    if not cursor.fetchone():
        print("Poll not found.")
        conn.close()
        return

    cursor.execute("DELETE FROM options WHERE poll_id = ?", (poll_id,))
    cursor.execute("DELETE FROM voters WHERE poll_id = ?", (poll_id,))
    cursor.execute("DELETE FROM polls WHERE id = ?", (poll_id,))
    conn.commit()
    conn.close()
    print("Poll deleted successfully!")


def main():
    create_tables()

    while True:
        print("\n========== POLLING / VOTING SYSTEM ==========")
        print("1. Create Poll")
        print("2. View All Polls")
        print("3. Vote")
        print("4. View Results")
        print("5. Delete Poll")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_poll()
        elif choice == "2":
            view_polls()
        elif choice == "3":
            vote()
        elif choice == "4":
            view_results()
        elif choice == "5":
            delete_poll()
        elif choice == "6":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()
