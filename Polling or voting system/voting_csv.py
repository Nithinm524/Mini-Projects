import csv
import os

POLLS_FILE = "polls.csv"
OPTIONS_FILE = "options.csv"
VOTERS_FILE = "voters.csv"


def create_files():
    if not os.path.exists(POLLS_FILE):
        with open(POLLS_FILE, "w", newline="") as f:
            csv.writer(f).writerow(["ID", "Question"])
    if not os.path.exists(OPTIONS_FILE):
        with open(OPTIONS_FILE, "w", newline="") as f:
            csv.writer(f).writerow(["ID", "PollID", "OptionText", "Votes"])
    if not os.path.exists(VOTERS_FILE):
        with open(VOTERS_FILE, "w", newline="") as f:
            csv.writer(f).writerow(["PollID", "VoterName"])


def read_rows(file_name):
    with open(file_name, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)
        return [row for row in reader if row]


def write_rows(file_name, header, rows):
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)


def get_next_id(rows):
    if not rows:
        return 1
    return max(int(row[0]) for row in rows) + 1


def create_poll():
    create_files()

    question = input("Enter Poll Question: ").strip()
    if not question:
        print("Question cannot be empty!")
        return

    count = input("How many options? (min 2): ").strip()
    if not count.isdigit() or int(count) < 2:
        print("You must enter at least 2 options.")
        return
    count = int(count)

    options_text = []
    for i in range(1, count + 1):
        opt = input(f"Enter Option {i}: ").strip()
        if not opt:
            print("Option text cannot be empty. Poll creation cancelled.")
            return
        options_text.append(opt)

    polls = read_rows(POLLS_FILE)
    poll_id = get_next_id(polls)
    with open(POLLS_FILE, "a", newline="") as f:
        csv.writer(f).writerow([poll_id, question])

    options = read_rows(OPTIONS_FILE)
    next_opt_id = get_next_id(options)
    with open(OPTIONS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        for opt in options_text:
            writer.writerow([next_opt_id, poll_id, opt, 0])
            next_opt_id += 1

    print(f"Poll created successfully! Poll ID: {poll_id}")


def view_polls():
    create_files()
    polls = read_rows(POLLS_FILE)

    print("\n----------- ALL POLLS -----------")
    if not polls:
        print("No polls found.")
        return

    print("{:<5} {:<40}".format("ID", "Question"))
    for row in polls:
        print("{:<5} {:<40}".format(row[0], row[1]))


def vote():
    create_files()

    poll_id = input("Enter Poll ID to Vote On: ").strip()
    if not poll_id.isdigit():
        print("Invalid Poll ID.")
        return

    polls = read_rows(POLLS_FILE)
    poll = next((p for p in polls if p[0] == poll_id), None)
    if not poll:
        print("Poll not found.")
        return

    options = read_rows(OPTIONS_FILE)
    poll_options = [o for o in options if o[1] == poll_id]

    print(f"\n{poll[1]}")
    for opt in poll_options:
        print(f"  {opt[0]}. {opt[2]}")

    voter_name = input("Enter Your Name: ").strip()
    if not voter_name:
        print("Name cannot be empty!")
        return

    voters = read_rows(VOTERS_FILE)
    if any(v[0] == poll_id and v[1].lower() == voter_name.lower() for v in voters):
        print("You have already voted on this poll.")
        return

    option_id = input("Enter Option ID to Vote: ").strip()
    valid_ids = [o[0] for o in poll_options]
    if option_id not in valid_ids:
        print("Invalid Option ID.")
        return

    for opt in options:
        if opt[0] == option_id:
            opt[3] = str(int(opt[3]) + 1)
            break

    write_rows(OPTIONS_FILE, ["ID", "PollID", "OptionText", "Votes"], options)

    with open(VOTERS_FILE, "a", newline="") as f:
        csv.writer(f).writerow([poll_id, voter_name])

    print("Vote cast successfully!")


def view_results():
    create_files()

    poll_id = input("Enter Poll ID to View Results: ").strip()
    if not poll_id.isdigit():
        print("Invalid Poll ID.")
        return

    polls = read_rows(POLLS_FILE)
    poll = next((p for p in polls if p[0] == poll_id), None)
    if not poll:
        print("Poll not found.")
        return

    options = read_rows(OPTIONS_FILE)
    poll_options = [o for o in options if o[1] == poll_id]

    total_votes = sum(int(o[3]) for o in poll_options)

    print(f"\n----------- RESULTS: {poll[1]} -----------")
    print("{:<20} {:<10} {:<10}".format("Option", "Votes", "Percent"))
    for opt in poll_options:
        votes = int(opt[3])
        percent = (votes / total_votes * 100) if total_votes else 0
        print("{:<20} {:<10} {:<9.1f}%".format(opt[2], votes, percent))
    print(f"\nTotal Votes: {total_votes}")


def delete_poll():
    create_files()

    poll_id = input("Enter Poll ID to Delete: ").strip()
    if not poll_id.isdigit():
        print("Invalid Poll ID.")
        return

    polls = read_rows(POLLS_FILE)
    if not any(p[0] == poll_id for p in polls):
        print("Poll not found.")
        return

    polls = [p for p in polls if p[0] != poll_id]
    options = [o for o in read_rows(OPTIONS_FILE) if o[1] != poll_id]
    voters = [v for v in read_rows(VOTERS_FILE) if v[0] != poll_id]

    write_rows(POLLS_FILE, ["ID", "Question"], polls)
    write_rows(OPTIONS_FILE, ["ID", "PollID", "OptionText", "Votes"], options)
    write_rows(VOTERS_FILE, ["PollID", "VoterName"], voters)

    print("Poll deleted successfully!")


def main():
    create_files()

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
