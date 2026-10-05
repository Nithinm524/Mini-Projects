import csv
import os
import string
import secrets

FILE_NAME = "passwords.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Site", "Username", "Password"])


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


def get_next_id(rows):
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
        writer.writerow(["ID", "Site", "Username", "Password"])
        writer.writerows(rows)


def save_account(site, username, password):
    if not site or not username:
        print("Site and Username are required. Not saved.")
        return
    rows = read_accounts()
    new_id = get_next_id(rows)
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([new_id, site, username, password])
    print("Account saved successfully!")


def generate_password_menu():
    create_file()

    length = input("Enter Password Length (default 12): ").strip()
    length = int(length) if length.isdigit() and int(length) >= 4 else 12

    use_digits = yes_no("Include digits? (y/n): ")
    use_symbols = yes_no("Include symbols? (y/n): ")

    password = generate_password(length, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")

    if yes_no("Save this password for an account? (y/n): "):
        site = input("Enter Site/App Name: ").strip()
        username = input("Enter Username/Email: ").strip()
        save_account(site, username, password)


def add_account_manual():
    create_file()

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

    save_account(site, username, password)


def view_accounts():
    create_file()

    rows = read_accounts()
    rows.sort(key=lambda r: r[1].lower())

    print("\n----------- SAVED ACCOUNTS -----------")
    if not rows:
        print("No accounts found.")
        return

    print("{:<5} {:<20} {:<20} {:<15}".format("ID", "Site", "Username", "Password"))
    for row in rows:
        print("{:<5} {:<20} {:<20} {:<15}".format(row[0], row[1], row[2], row[3]))


def search_account():
    create_file()

    keyword = input("Enter Site Name to Search: ").strip().lower()

    rows = read_accounts()
    matches = [row for row in rows if keyword in row[1].lower()]

    if not matches:
        print("No matching accounts found.")
        return

    for row in matches:
        print("\nAccount Found")
        print("---------------------------")
        print("Site     :", row[1])
        print("Username :", row[2])
        print("Password :", row[3])


def update_account():
    create_file()

    acc_id = input("Enter Account ID to Update: ").strip()
    if not acc_id.isdigit():
        print("Invalid ID.")
        return

    rows = read_accounts()
    found = False

    for row in rows:
        if row[0] == acc_id:
            print("\nEnter New Details (leave blank to keep current)")
            new_username = input("New Username: ").strip()
            new_password = input("New Password: ").strip()

            if new_username:
                row[2] = new_username
            if new_password:
                row[3] = new_password

            found = True
            break

    if found:
        write_accounts(rows)
        print("Account updated successfully!")
    else:
        print("Account not found.")


def delete_account():
    create_file()

    acc_id = input("Enter Account ID to Delete: ").strip()
    if not acc_id.isdigit():
        print("Invalid ID.")
        return

    rows = read_accounts()
    new_rows = [row for row in rows if row[0] != acc_id]

    if len(new_rows) == len(rows):
        print("Account not found.")
        return

    write_accounts(new_rows)
    print("Account deleted successfully!")


def main():
    create_file()

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
