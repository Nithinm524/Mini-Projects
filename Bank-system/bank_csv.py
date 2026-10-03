import csv
import os

FILE_NAME = "bank.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["AccNo", "Name", "Pin", "Balance"])


def get_next_acc_no(rows):
    if not rows:
        return 1
    return max(int(row[0]) for row in rows) + 1


def read_accounts():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        return [row for row in reader if row]


def write_accounts(rows):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["AccNo", "Name", "Pin", "Balance"])
        writer.writerows(rows)


def find_account(rows, acc_no):
    for row in rows:
        if row[0] == acc_no:
            return row
    return None


def create_account():
    create_file()

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

    rows = read_accounts()
    acc_no = get_next_acc_no(rows)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([acc_no, name, pin, float(deposit)])

    print(f"Account created successfully! Your Account Number is: {acc_no}")
    print("Please note it down, you'll need it to log in.")


def deposit():
    create_file()

    acc_no = input("Enter Account Number: ").strip()
    if not acc_no.isdigit():
        print("Invalid Account Number.")
        return

    rows = read_accounts()
    account = find_account(rows, acc_no)
    if not account:
        print("Account not found.")
        return

    pin = input("Enter PIN: ").strip()
    if account[2] != pin:
        print("Incorrect PIN.")
        return

    amount = input("Enter Deposit Amount: ").strip()
    if not amount.replace(".", "", 1).isdigit() or float(amount) <= 0:
        print("Amount must be a positive number.")
        return

    account[3] = str(float(account[3]) + float(amount))
    write_accounts(rows)
    print(f"Deposit successful! New Balance: {float(account[3]):.2f}")


def withdraw():
    create_file()

    acc_no = input("Enter Account Number: ").strip()
    if not acc_no.isdigit():
        print("Invalid Account Number.")
        return

    rows = read_accounts()
    account = find_account(rows, acc_no)
    if not account:
        print("Account not found.")
        return

    pin = input("Enter PIN: ").strip()
    if account[2] != pin:
        print("Incorrect PIN.")
        return

    amount = input("Enter Withdrawal Amount: ").strip()
    if not amount.replace(".", "", 1).isdigit() or float(amount) <= 0:
        print("Amount must be a positive number.")
        return

    amount = float(amount)
    balance = float(account[3])
    if amount > balance:
        print("Insufficient balance.")
        return

    account[3] = str(balance - amount)
    write_accounts(rows)
    print(f"Withdrawal successful! New Balance: {float(account[3]):.2f}")


def check_balance():
    create_file()

    acc_no = input("Enter Account Number: ").strip()
    if not acc_no.isdigit():
        print("Invalid Account Number.")
        return

    rows = read_accounts()
    account = find_account(rows, acc_no)
    if not account:
        print("Account not found.")
        return

    pin = input("Enter PIN: ").strip()
    if account[2] != pin:
        print("Incorrect PIN.")
        return

    print(f"\nAccount Holder : {account[1]}")
    print(f"Balance        : {float(account[3]):.2f}")


def delete_account():
    create_file()

    acc_no = input("Enter Account Number to Close: ").strip()
    if not acc_no.isdigit():
        print("Invalid Account Number.")
        return

    rows = read_accounts()
    account = find_account(rows, acc_no)
    if not account:
        print("Account not found.")
        return

    pin = input("Enter PIN: ").strip()
    if account[2] != pin:
        print("Incorrect PIN.")
        return

    new_rows = [row for row in rows if row[0] != acc_no]
    write_accounts(new_rows)
    print("Account closed successfully.")


def main():
    create_file()

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
