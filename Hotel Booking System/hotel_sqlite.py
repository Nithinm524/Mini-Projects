import sqlite3
from datetime import datetime

DB_NAME = "hotel.db"


def create_connection():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            room_no TEXT PRIMARY KEY,
            type TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Available',
            guest_name TEXT,
            check_in TEXT,
            check_out TEXT
        )
    """)
    conn.commit()
    conn.close()


def valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_room(room_no):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms WHERE room_no = ?", (room_no,))
    row = cursor.fetchone()
    conn.close()
    return row


def add_room():
    room_no = input("Enter Room Number: ").strip()
    if not room_no:
        print("Room Number cannot be empty!")
        return

    if get_room(room_no):
        print("Room already exists!")
        return

    room_type = input("Enter Room Type (Single/Double/Suite): ").strip()
    if not room_type:
        print("Room Type cannot be empty!")
        return

    price = input("Enter Price per Night: ").strip()
    if not price.replace(".", "", 1).isdigit() or float(price) <= 0:
        print("Price must be a positive number.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO rooms (room_no, type, price, status) VALUES (?, ?, ?, 'Available')",
        (room_no, room_type, float(price))
    )
    conn.commit()
    conn.close()
    print("Room added successfully!")


def view_rooms():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms ORDER BY room_no")
    rows = cursor.fetchall()
    conn.close()

    print("\n----------- ALL ROOMS -----------")
    if not rows:
        print("No rooms found.")
        return

    print("{:<10} {:<10} {:<10} {:<12}".format("Room No", "Type", "Price", "Status"))
    for row in rows:
        print("{:<10} {:<10} {:<10.2f} {:<12}".format(row[0], row[1], row[2], row[3]))


def book_room():
    room_no = input("Enter Room Number to Book: ").strip()

    row = get_room(room_no)
    if not row:
        print("Room not found.")
        return

    if row[3] == "Booked":
        print("Room is already booked.")
        return

    guest_name = input("Enter Guest Name: ").strip()
    if not guest_name:
        print("Guest Name cannot be empty!")
        return

    check_in = input("Enter Check-In Date (YYYY-MM-DD): ").strip()
    check_out = input("Enter Check-Out Date (YYYY-MM-DD): ").strip()

    if not valid_date(check_in) or not valid_date(check_out):
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    if check_out <= check_in:
        print("Check-Out date must be after Check-In date.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE rooms SET status = 'Booked', guest_name = ?, check_in = ?, check_out = ? WHERE room_no = ?",
        (guest_name, check_in, check_out, room_no)
    )
    conn.commit()
    conn.close()
    print("Room booked successfully!")


def checkout_room():
    room_no = input("Enter Room Number to Check-Out: ").strip()

    row = get_room(room_no)
    if not row:
        print("Room not found.")
        return

    if row[3] != "Booked":
        print("Room is not currently booked.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE rooms SET status = 'Available', guest_name = NULL, check_in = NULL, check_out = NULL WHERE room_no = ?",
        (room_no,)
    )
    conn.commit()
    conn.close()
    print("Room checked out successfully!")


def view_booked_rooms():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms WHERE status = 'Booked' ORDER BY room_no")
    rows = cursor.fetchall()
    conn.close()

    print("\n----------- BOOKED ROOMS -----------")
    if not rows:
        print("No rooms currently booked.")
        return

    print("{:<10} {:<15} {:<12} {:<12}".format("Room No", "Guest", "Check-In", "Check-Out"))
    for row in rows:
        print("{:<10} {:<15} {:<12} {:<12}".format(row[0], row[4], row[5], row[6]))


def delete_room():
    room_no = input("Enter Room Number to Delete: ").strip()

    row = get_room(room_no)
    if not row:
        print("Room not found.")
        return

    if row[3] == "Booked":
        print("Cannot delete a room that is currently booked. Check-out first.")
        return

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM rooms WHERE room_no = ?", (room_no,))
    conn.commit()
    conn.close()
    print("Room deleted successfully!")


def main():
    create_table()

    while True:
        print("\n========== HOTEL ROOM BOOKING SYSTEM ==========")
        print("1. Add Room")
        print("2. View All Rooms")
        print("3. Book Room")
        print("4. Check-Out")
        print("5. View Booked Rooms")
        print("6. Delete Room")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_room()
        elif choice == "2":
            view_rooms()
        elif choice == "3":
            book_room()
        elif choice == "4":
            checkout_room()
        elif choice == "5":
            view_booked_rooms()
        elif choice == "6":
            delete_room()
        elif choice == "7":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Please try again.")


if __name__ == "__main__":
    main()
