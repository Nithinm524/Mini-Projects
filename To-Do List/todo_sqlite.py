import sqlite3

DB_NAME = "todo.db"


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pending'
        )
    """)
    conn.commit()
    conn.close()


def add_task():
    task = input("Enter Task: ").strip()
    if not task:
        print("Task cannot be empty!")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, status) VALUES (?, ?)", (task, "Pending"))
    conn.commit()
    conn.close()
    print("Task added successfully!")


def view_tasks():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY id")
    rows = cursor.fetchall()
    conn.close()

    print("\n----------- TO-DO LIST -----------")
    if not rows:
        print("No tasks found.")
        return

    print("{:<5} {:<40} {:<10}".format("ID", "Task", "Status"))
    for row in rows:
        print("{:<5} {:<40} {:<10}".format(row[0], row[1], row[2]))


def mark_done():
    task_id = input("Enter Task ID to mark as Done: ").strip()
    if not task_id.isdigit():
        print("Invalid ID.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'Done' WHERE id = ?", (task_id,))
    conn.commit()
    updated = cursor.rowcount
    conn.close()

    if updated:
        print("Task marked as Done!")
    else:
        print("Task not found.")


def update_task():
    task_id = input("Enter Task ID to Update: ").strip()
    if not task_id.isdigit():
        print("Invalid ID.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()

    if not row:
        print("Task not found.")
        conn.close()
        return

    new_task = input("Enter New Task Description: ").strip()
    if not new_task:
        print("Task description cannot be empty. Update cancelled.")
        conn.close()
        return

    cursor.execute("UPDATE tasks SET task = ? WHERE id = ?", (new_task, task_id))
    conn.commit()
    conn.close()
    print("Task updated successfully!")


def delete_task():
    task_id = input("Enter Task ID to Delete: ").strip()
    if not task_id.isdigit():
        print("Invalid ID.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    if deleted:
        print("Task deleted successfully!")
    else:
        print("Task not found.")


def main():
    create_table()

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
