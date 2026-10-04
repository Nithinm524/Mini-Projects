import csv
import os

FILE_NAME = "todo.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Task", "Status"])


def get_next_id(rows):
    if not rows:
        return 1
    return max(int(row[0]) for row in rows) + 1


def read_tasks():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        return [row for row in reader if row]


def write_tasks(rows):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Status"])
        writer.writerows(rows)


def add_task():
    create_file()

    task = input("Enter Task: ").strip()
    if not task:
        print("Task cannot be empty!")
        return

    rows = read_tasks()
    new_id = get_next_id(rows)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([new_id, task, "Pending"])

    print("Task added successfully!")


def view_tasks():
    create_file()

    rows = read_tasks()

    print("\n----------- TO-DO LIST -----------")
    if not rows:
        print("No tasks found.")
        return

    print("{:<5} {:<40} {:<10}".format("ID", "Task", "Status"))
    for row in rows:
        print("{:<5} {:<40} {:<10}".format(row[0], row[1], row[2]))


def mark_done():
    create_file()

    task_id = input("Enter Task ID to mark as Done: ").strip()
    if not task_id.isdigit():
        print("Invalid ID.")
        return

    rows = read_tasks()
    found = False

    for row in rows:
        if row[0] == task_id:
            row[2] = "Done"
            found = True
            break

    if found:
        write_tasks(rows)
        print("Task marked as Done!")
    else:
        print("Task not found.")


def update_task():
    create_file()

    task_id = input("Enter Task ID to Update: ").strip()
    if not task_id.isdigit():
        print("Invalid ID.")
        return

    rows = read_tasks()
    found = False

    for row in rows:
        if row[0] == task_id:
            new_task = input("Enter New Task Description: ").strip()
            if not new_task:
                print("Task description cannot be empty. Update cancelled.")
                return
            row[1] = new_task
            found = True
            break

    if found:
        write_tasks(rows)
        print("Task updated successfully!")
    else:
        print("Task not found.")


def delete_task():
    create_file()

    task_id = input("Enter Task ID to Delete: ").strip()
    if not task_id.isdigit():
        print("Invalid ID.")
        return

    rows = read_tasks()
    new_rows = [row for row in rows if row[0] != task_id]

    if len(new_rows) == len(rows):
        print("Task not found.")
        return

    write_tasks(new_rows)
    print("Task deleted successfully!")


def main():
    create_file()

    while True:
        print("\n========== TO-DO LIST APP ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()
