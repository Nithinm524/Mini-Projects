import csv
import os

FILE_NAME = "contacts.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Phone", "Name", "Email", "Address"])


def add_contact():
    create_file()

    phone = input("Enter Phone Number: ").strip()
    if not phone:
        print("Phone Number cannot be empty!")
        return
    if not phone.isdigit():
        print("Phone Number must contain digits only.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if not row:
                continue
            if row[0] == phone:
                print("Phone Number already exists!")
                return

    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty. Contact not added.")
        return

    email = input("Enter Email (optional): ").strip()
    address = input("Enter Address (optional): ").strip()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([phone, name, email, address])

    print("Contact added successfully!")


def view_contacts():
    create_file()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        rows = [row for row in reader if row]

    print("\n----------- CONTACT LIST -----------")
    if not rows:
        print("No contacts found.")
        return

    rows.sort(key=lambda r: r[1].lower())

    print("{:<15} {:<20} {:<25} {:<20}".format("Phone", "Name", "Email", "Address"))
    for row in rows:
        email = row[2] if row[2] else "-"
        address = row[3] if row[3] else "-"
        print("{:<15} {:<20} {:<25} {:<20}".format(row[0], row[1], email, address))


def search_contact():
    create_file()

    keyword = input("Enter Name or Phone to Search: ").strip().lower()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        rows = [row for row in reader if row]

    matches = [row for row in rows if row[0] == keyword or keyword in row[1].lower()]

    if not matches:
        print("Contact not found.")
        return

    for row in matches:
        print("\nContact Found")
        print("---------------------------")
        print("Phone   :", row[0])
        print("Name    :", row[1])
        print("Email   :", row[2] if row[2] else "-")
        print("Address :", row[3] if row[3] else "-")


def update_contact():
    create_file()

    phone = input("Enter Phone Number to Update: ").strip()

    contacts = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        contacts.append(header)

        for row in reader:
            if not row:
                continue

            if row[0] == phone:
                print("\nEnter New Details (leave blank to keep current)")
                new_name = input("New Name: ").strip()
                new_email = input("New Email: ").strip()
                new_address = input("New Address: ").strip()

                if new_name:
                    row[1] = new_name
                if new_email:
                    row[2] = new_email
                if new_address:
                    row[3] = new_address

                found = True

            contacts.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact():
    create_file()

    phone = input("Enter Phone Number to Delete: ").strip()

    contacts = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        header = next(reader)
        contacts.append(header)

        for row in reader:
            if not row:
                continue

            if row[0] == phone:
                found = True
                continue

            contacts.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def main():
    create_file()

    while True:
        print("\n========== CONTACT BOOK ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()
