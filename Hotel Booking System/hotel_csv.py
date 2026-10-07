import csv
import os
from datetime import datetime

FILE_NAME = "hotel.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["RoomNo", "Type", "Price", "Status", "Guest", "CheckIn", "CheckOut"])


def valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def read_rooms():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        return [row for row in reader if row]


def write_rooms(rows):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["RoomNo", "Type", "Price", "Status", "Guest", "CheckIn", "CheckOut"])
        writer.writerows(rows)


def find_room(rows, room_no):
    for row in rows:
        if row[0] == room_no:
            return row
    return None


def add_room():
    create_file()

    room_no = input("Enter Room Number: ").strip()
    if not room_no:
        print("Room Number cannot be empty!")
        return

    rows = read_rooms()
    if find_room(rows, room_no):
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

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([room_no, room_type, float(price), "Available", "", "", ""])

    print("Room added successfully!")


def view_rooms():
    create_file()

    rows = read_rooms()
    rows.sort(key=lambda r: r[0])

    print("\n----------- ALL ROOMS -----------")
    if not rows:
        print("No rooms found.")
        return

    print("{:<10} {:<10} {:<10} {:<12}".format("Room No", "Type", "Price", "Status"))
    for row in rows:
        print("{:<10} {:<10} {:<10.2f} {:<12}".format(row[0], row[1], float(row[2]), row[3]))


def book_room():
    create_file()

    room_no = input("Enter Room Number to Book: ").strip()

    rows = read_rooms()
    room = find_room(rows, room_no)

    if not room:
        print("Room not found.")
        return

    if room[3] == "Booked":
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

    room[3] = "Booked"
    room[4] = guest_name
    room[5] = check_in
    room[6] = check_out

    write_rooms(rows)
    print("Room booked successfully!")


def checkout_room():
    create_file()

    room_no = input("Enter Room Number to Check-Out: ").strip()

    rows = read_rooms()
    room = find_room(rows, room_no)

    if not room:
        print("Room not found.")
        return

    if room[3] != "Booked":
        print("Room is not currently booked.")
        return

    room[3] = "Available"
    room[4] = ""
    room[5] = ""
    room[6] = ""

    write_rooms(rows)
    print("Room checked out successfully!")


def view_booked_rooms():
    create_file()

    rows = read_rooms()
    booked = [row for row in rows if row[3] == "Booked"]
    booked.sort(key=lambda r: r[0])

    print("\n----------- BOOKED ROOMS -----------")
    if not booked:
        print("No rooms currently booked.")
        return

    print("{:<10} {:<15} {:<12} {:<12}".format("Room No", "Guest", "Check-In", "Check-Out"))
    for row in booked:
        print("{:<10} {:<15} {:<12} {:<12}".format(row[0], row[4], row[5], row[6]))


def delete_room():
    create_file()

    room_no = input("Enter Room Number to Delete: ").strip()

    rows = read_rooms()
    room = find_room(rows, room_no)

    if not room:
        print("Room not found.")
        return

    if room[3] == "Booked":
        print("Cannot delete a room that is currently booked. Check-out first.")
        return

    new_rows = [row for row in rows if row[0] != room_no]
    write_rooms(new_rows)
    print("Room deleted successfully!")


def main():
    create_file()

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
