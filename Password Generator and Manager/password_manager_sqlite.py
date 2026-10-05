import sqlite3
import string
import secrets

DB_NAME = "passwords.db"


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            site TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def generate_password(length=12, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+"
    return "".join(secrets.choice(chars) for _ in range(length))


def yes_no(prompt):
    ans = input(prompt).strip().lower()
    return ans in ("y", "yes")


def generate_password_menu():
    length = input("Enter Password Length (default 12): ").strip()
    length = int(length) if length.isdigit() and int(length) >= 4 else 12

    use_digits = yes_no("Include digits? (y/n): ")
    use_symbols = yes_no("Include symbols? (y/n): ")

    password = generate_password(length, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")

    if yes_no("Save this password for an account? (y/n): "):
        site = input("Enter Site/App Name: ").strip()
        username = input("Enter Username/Email: ").strip()
        if not site or not username:
            print("Site and Username are required. Not saved.")
            return
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO accounts (site, username, password) VALUES (?, ?, ?)",
            (site, username, password)
        )
        conn.commit()
        conn.close()
        print("Account saved successfully!")


def add_account_manual():
    site = input("Enter Site/App Name: ").strip()
    if not site:
        print("Site cannot be empty!")
        return

    username = input("Enter Username/Email: ").strip()
    if not username:
        print("Username cannot be empty!")
        return

    password = input("Enter Password: ").strip()
    if not password:
        print("Password cannot be empty!")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO accounts (site, username, password) VALUES (?, ?, ?)",
        (site, username, password)
    )
    conn.commit()
    conn.close()
    print("Account saved successfully!")


def view_accounts():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts ORDER BY site")
    rows = cursor.fetchall()
    conn.close()

    print("\n----------- SAVED ACCOUNTS -----------")
    if not rows:
        print("No accounts found.")
        return

    print("{:<5} {:<20} {:<20} {:<15}".format("ID", "Site", "Username", "Password"))
    for row in rows:
        print("{:<5} {:<20} {:<20} {:<15}".format(row[0], row[1], row[2], row[3]))


def search_account():
    keyword = input("Enter Site Name to Search: ").strip().lower()

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE LOWER(site) LIKE ?", (f"%{keyword}%",))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No matching accounts found.")
        return

    for row in rows:
        print("\nAccount Found")
        print("---------------------------")
        print("Site     :", row[1])
        print("Username :", row[2])
        print("Password :", row[3])


def update_account():
    acc_id = input("Enter Account ID to Update: ").strip()
    if not acc_id.isdigit():
        print("Invalid ID.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE id = ?", (acc_id,))
    row = cursor.fetchone()

    if not row:
        print("Account not found.")
        conn.close()
        return

    print("\nEnter New Details (leave blank to keep current)")
    new_username = input("New Username: ").strip()
    new_password = input("New Password: ").strip()

    username = new_username if new_username else row[2]
    password = new_password if new_password else row[3]

    cursor.execute(
        "UPDATE accounts SET username = ?, password = ? WHERE id = ?",
        (username, password, acc_id)
    )
    conn.commit()
    conn.close()
    print("Account updated successfully!")


def delete_account():
    acc_id = input("Enter Account ID to Delete: ").strip()
    if not acc_id.isdigit():
        print("Invalid ID.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE id = ?", (acc_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    if deleted:
        print("Account deleted successfully!")
    else:
        print("Account not found.")


def main():
    create_table()

    while True:
        print("\n========== PASSWORD GENERATOR / MANAGER ==========")
        print("1. Generate Password")
        print("2. Add Account Manually")
        print("3. View All Accounts")
        print("4. Search Account")
        print("5. Update Account")
        print("6. Delete Account")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            generate_password_menu()
        elif choice == "2":
            add_account_manual()
        elif choice == "3":
            view_accounts()
        elif choice == "4":
            search_account()
        elif choice == "5":
            update_account()
        elif choice == "6":
            delete_account()
        elif choice == "7":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()
