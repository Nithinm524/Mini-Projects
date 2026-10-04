import sqlite3

DB_NAME = "contacts.db"


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            phone TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_contact():
    phone = input("Enter Phone Number: ").strip()
    if not phone:
        print("Phone Number cannot be empty!")
        return
    if not phone.isdigit():
        print("Phone Number must contain digits only.")
        return

    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty. Contact not added.")
        return

    email = input("Enter Email (optional): ").strip()
    address = input("Enter Address (optional): ").strip()

    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO contacts (phone, name, email, address) VALUES (?, ?, ?, ?)",
            (phone, name, email, address)
        )
        conn.commit()
        print("Contact added successfully!")
    except sqlite3.IntegrityError:
        print("Phone Number already exists!")
    finally:
        conn.close()


def view_contacts():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts ORDER BY name")
    rows = cursor.fetchall()
    conn.close()

    print("\n----------- CONTACT LIST -----------")
    if not rows:
        print("No contacts found.")
        return

    print("{:<15} {:<20} {:<25} {:<20}".format("Phone", "Name", "Email", "Address"))
    for row in rows:
        print("{:<15} {:<20} {:<25} {:<20}".format(row[0], row[1], row[2] or "-", row[3] or "-"))


def search_contact():
    keyword = input("Enter Name or Phone to Search: ").strip()

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM contacts WHERE phone = ? OR name LIKE ?",
        (keyword, f"%{keyword}%")
    )
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("Contact not found.")
        return

    for row in rows:
        print("\nContact Found")
        print("---------------------------")
        print("Phone   :", row[0])
        print("Name    :", row[1])
        print("Email   :", row[2] or "-")
        print("Address :", row[3] or "-")


def update_contact():
    phone = input("Enter Phone Number to Update: ").strip()

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE phone = ?", (phone,))
    row = cursor.fetchone()

    if not row:
        print("Contact not found.")
        conn.close()
        return

    print("\nEnter New Details (leave blank to keep current)")
    new_name = input("New Name: ").strip()
    new_email = input("New Email: ").strip()
    new_address = input("New Address: ").strip()

    name = new_name if new_name else row[1]
    email = new_email if new_email else row[2]
    address = new_address if new_address else row[3]

    cursor.execute(
        "UPDATE contacts SET name = ?, email = ?, address = ? WHERE phone = ?",
        (name, email, address, phone)
    )
    conn.commit()
    conn.close()
    print("Contact updated successfully!")


def delete_contact():
    phone = input("Enter Phone Number to Delete: ").strip()

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE phone = ?", (phone,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    if deleted:
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def main():
    create_table()

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
