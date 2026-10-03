import sqlite3

DB_NAME = "bank.db"


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            acc_no INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            pin TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


def get_account(acc_no):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE acc_no = ?", (acc_no,))
    row = cursor.fetchone()
    conn.close()
    return row


def verify_pin(row, pin):
    return row is not None and row[2] == pin


def create_account():
    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return

    pin = input("Set 4-digit PIN: ").strip()
    if not (pin.isdigit() and len(pin) == 4):
        print("PIN must be exactly 4 digits.")
        return

    deposit = input("Enter Initial Deposit: ").strip()
    if not deposit.replace(".", "", 1).isdigit() or float(deposit) < 0:
        print("Initial deposit must be a valid non-negative number.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO accounts (name, pin, balance) VALUES (?, ?, ?)",
        (name, pin, float(deposit))
    )
    conn.commit()
    acc_no = cursor.lastrowid
    conn.close()

    print(f"Account created successfully! Your Account Number is: {acc_no}")
    print("Please note it down, you'll need it to log in.")


def deposit():
    acc_no = input("Enter Account Number: ").strip()
    if not acc_no.isdigit():
        print("Invalid Account Number.")
        return

    row = get_account(acc_no)
    if not row:
        print("Account not found.")
        return

    pin = input("Enter PIN: ").strip()
    if not verify_pin(row, pin):
        print("Incorrect PIN.")
        return

    amount = input("Enter Deposit Amount: ").strip()
    if not amount.replace(".", "", 1).isdigit() or float(amount) <= 0:
        print("Amount must be a positive number.")
        return

    new_balance = row[3] + float(amount)
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE accounts SET balance = ? WHERE acc_no = ?", (new_balance, acc_no))
    conn.commit()
    conn.close()

    print(f"Deposit successful! New Balance: {new_balance:.2f}")


def withdraw():
    acc_no = input("Enter Account Number: ").strip()
    if not acc_no.isdigit():
        print("Invalid Account Number.")
        return

    row = get_account(acc_no)
    if not row:
        print("Account not found.")
        return

    pin = input("Enter PIN: ").strip()
    if not verify_pin(row, pin):
        print("Incorrect PIN.")
        return

    amount = input("Enter Withdrawal Amount: ").strip()
    if not amount.replace(".", "", 1).isdigit() or float(amount) <= 0:
        print("Amount must be a positive number.")
        return

    amount = float(amount)
    if amount > row[3]:
        print("Insufficient balance.")
        return

    new_balance = row[3] - amount
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE accounts SET balance = ? WHERE acc_no = ?", (new_balance, acc_no))
    conn.commit()
    conn.close()

    print(f"Withdrawal successful! New Balance: {new_balance:.2f}")


def check_balance():
    acc_no = input("Enter Account Number: ").strip()
    if not acc_no.isdigit():
        print("Invalid Account Number.")
        return

    row = get_account(acc_no)
    if not row:
        print("Account not found.")
        return

    pin = input("Enter PIN: ").strip()
    if not verify_pin(row, pin):
        print("Incorrect PIN.")
        return

    print(f"\nAccount Holder : {row[1]}")
    print(f"Balance        : {row[3]:.2f}")


def delete_account():
    acc_no = input("Enter Account Number to Close: ").strip()
    if not acc_no.isdigit():
        print("Invalid Account Number.")
        return

    row = get_account(acc_no)
    if not row:
        print("Account not found.")
        return

    pin = input("Enter PIN: ").strip()
    if not verify_pin(row, pin):
        print("Incorrect PIN.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE acc_no = ?", (acc_no,))
    conn.commit()
    conn.close()

    print("Account closed successfully.")


def main():
    create_table()

    while True:
        print("\n========== ATM / BANK SYSTEM ==========")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Close Account")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            delete_account()
        elif choice == "6":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()
