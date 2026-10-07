# 🏨 Hotel Booking System

<div align="center">

<img 
  src="hotel-booking.png"
  alt="Hotel Booking System Python Mini Project"
  width="100%"
>

</div>

<br>
<br>

### A Python-Based Hotel Reservation and Booking Management Application
---
The **Hotel Booking System** is a Python-based mini project developed to demonstrate how a real-world hotel reservation process can be converted into a simple, interactive, and organized software application. The system is designed to manage important hotel booking activities such as viewing available rooms, creating reservations, storing guest information, searching for bookings, updating reservation details, and cancelling reservations.

In a traditional hotel environment, reservation information such as guest details, room numbers, room types, check-in dates, check-out dates, and booking status needs to be maintained accurately. Managing these records manually can become difficult when the number of guests and reservations increases. This project provides a computerized approach for maintaining hotel booking information and performing common reservation operations efficiently.

The application follows a structured reservation-management approach where users can create and manage booking records through a menu-driven interface. The system demonstrates the fundamental **CRUD operations — Create, Read, Update, and Delete**. A new reservation represents the Create operation, viewing and searching reservations represent Read operations, modifying an existing reservation represents Update, and cancelling a reservation represents Delete.

The project can use different methods for storing booking information. A **CSV-based implementation** can store reservations in a structured CSV file, while an **SQLite-based implementation** can maintain reservation records inside a local relational database. These two approaches provide practical experience with both file-based and database-based data storage.

The project combines several important Python programming concepts, including variables, data structures, functions, loops, conditional statements, user input, input validation, file handling, database operations, and record management. By combining these concepts, the project demonstrates how basic programming knowledge can be applied to develop a practical real-world application.

This project was developed as part of my **Python Mini Projects** collection to strengthen programming fundamentals through hands-on implementation and to understand how hotel reservation systems can be designed using Python.

> ⚠️ **Educational Notice:** This project is intended for learning and demonstration purposes. It is not a production-ready hotel reservation platform.

<br>
<br>


## 📌 Project Overview

The **Hotel Booking System** is a menu-driven application designed to simplify basic hotel reservation and booking management.

When the application starts, the user is presented with a set of options that allow different hotel management operations to be performed. Users can view available rooms, create a new booking, view existing reservations, search for a particular booking, update reservation details, cancel a reservation, and exit the application.

The booking process begins when a guest provides the required information. The system can collect details such as the guest name, phone number, room number, room type, check-in date, and check-out date. After receiving the information, the system validates the entered data before creating a reservation.

Once a booking is successfully created, the reservation information can be stored permanently. In a CSV implementation, the information can be stored in a CSV file, while an SQLite implementation can store the information inside a local database.

Existing reservations can be viewed whenever required. The search functionality allows users to locate a specific reservation using information such as a booking ID, guest name, phone number, or room number.

If a guest wants to modify their reservation, the system can update the existing record instead of creating a duplicate booking. If a reservation is cancelled, the system can remove the reservation or update its status and make the associated room available again.

The overall project demonstrates the complete lifecycle of a basic hotel reservation, starting from room selection and booking creation to reservation management and cancellation.

<br>
<br>


## 💡 Problem Statement

Hotels need to maintain a large amount of information related to guests, rooms, and reservations. Managing these records manually can become time-consuming and may result in errors, duplicate bookings, or difficulty finding existing reservation information.

A computerized hotel booking system can simplify this process by providing a structured method for maintaining guest information, room availability, and booking records.

The objective of this project is to develop a Python-based Hotel Booking System that allows users to perform common hotel reservation operations through a simple and interactive interface.

The system should provide functionality for:

- Viewing available rooms.
- Making new hotel reservations.
- Recording guest information.
- Assigning rooms to guests.
- Storing booking details.
- Viewing existing reservations.
- Searching for specific bookings.
- Updating reservation information.
- Cancelling bookings.
- Maintaining room availability.
- Validating user input.
- Managing booking records efficiently.

The project demonstrates how Python can be used to solve a practical record-management problem through structured programming.

<br>
<br>

## 🎯 Objectives

The main objective of this project is to develop a simple and interactive hotel reservation management application using Python.

The specific objectives are:

- To develop a computerized hotel booking system.
- To display available hotel rooms.
- To allow users to make new reservations.
- To collect and store guest information.
- To assign rooms to reservations.
- To maintain booking records.
- To search for existing reservations.
- To update booking information.
- To cancel reservations.
- To maintain room availability.
- To implement CRUD operations.
- To practice Python file handling.
- To understand CSV-based data storage.
- To understand SQLite database storage.
- To implement input validation.
- To practice date-related operations.
- To improve logical thinking and problem-solving skills.
- To understand how real-world reservation systems can be implemented using Python.

<br>
<br>


## ✨ Features

### 🏨 Room Availability

The system can display the rooms that are currently available for reservation.

Room information can include the room number, room type, price, and current availability status.

Example:

```text
Room No.    Room Type       Price/Night      Status
----------------------------------------------------
101         Single          ₹1500            Available
102         Double          ₹2500            Available
201         Deluxe          ₹3500            Booked
202         Suite           ₹5000            Available
```

This feature helps users identify which rooms can currently be reserved.

<br>
<br>

### 🛎️ Make a Booking

The **Make Booking** operation allows a guest to create a new hotel reservation.

The application can request information such as:

```text
Guest Name
Phone Number
Email
Room Number
Check-in Date
Check-out Date
```

After collecting the required information, the system validates the data and creates the reservation.

This operation represents the **Create** part of CRUD.

<br>
<br>


### 🧑 Guest Information

The application maintains important information about guests associated with each reservation.

Guest information may include:

- Guest name
- Phone number
- Email address
- Booking ID
- Assigned room
- Check-in date
- Check-out date

Maintaining these details makes it easier to identify and manage individual reservations.

<br>
<br>

### 🆔 Booking ID

Each reservation can be associated with a unique booking ID.

Example:

```text
Booking ID: HB1001
```

The booking ID provides a simple way to identify an individual reservation.

It can also be used when searching, updating or cancelling a booking.

<br>
<br>

### 👀 View Bookings

The **View Bookings** feature allows users to display existing hotel reservations.

The reservation list can contain information such as:

```text
Booking ID
Guest Name
Room Number
Check-in Date
Check-out Date
Status
```

Example:

```text
Booking ID   Guest       Room    Check-in     Check-out
---------------------------------------------------------
HB1001       Nithin      101     2026-10-10   2026-10-12
HB1002       Rahul       202     2026-10-11   2026-10-15
```

This represents the **Read** operation in CRUD.

<br>
<br>

### 🔍 Search Booking

The **Search Booking** feature allows users to quickly find a specific reservation.

The system can search using:

- Booking ID
- Guest name
- Phone number
- Room number

This is especially useful when the number of stored reservations becomes large.

Instead of checking every reservation manually, the user can provide a search value and retrieve the required record.

<br>
<br>

### ✏️ Update Booking

Guests may need to modify their reservation after it has been created.

The **Update Booking** operation can allow changes to:

- Guest information
- Phone number
- Email
- Room number
- Check-in date
- Check-out date

The existing reservation is modified rather than creating a new duplicate record.

This represents the **Update** operation in CRUD.

---

### ❌ Cancel Booking

The **Cancel Booking** feature allows users to cancel an existing reservation.

After cancellation, the system can update the booking status or remove the reservation depending on the implementation.

The associated room can then become available for another guest.

This represents the **Delete** operation in CRUD when the reservation is physically removed.

---

### 📅 Check-in and Check-out

The application maintains check-in and check-out dates for every reservation.

These dates determine how long the guest will stay at the hotel.

For example:

```text
Check-in  : 2026-10-10
Check-out : 2026-10-13
```

The guest stays for three nights.

The date information can also be used for calculating the total booking cost.

---

### 💰 Booking Cost Calculation

The system can calculate the estimated booking cost using the room price and number of nights.

The basic formula is:

```text
Total Cost = Room Price × Number of Nights
```

Example:

```text
Room Price = ₹2500 per night
Stay       = 3 nights

Total Cost = ₹2500 × 3
           = ₹7500
```

This feature demonstrates how the application can process reservation information and perform calculations.

---

### 💾 CSV Storage

The CSV implementation stores hotel booking records in a CSV file.

CSV provides a simple and lightweight way of maintaining reservation information without requiring a database server.

Each reservation can be stored as one row in the CSV file.

---

### 🗄️ SQLite Storage

The SQLite implementation stores hotel booking information in a local SQLite database.

The database provides structured storage and allows SQL operations to be performed on reservation records.

The SQLite version can support operations such as:

```text
INSERT
SELECT
UPDATE
DELETE
```

This provides practical experience with relational database management.

---

### 🔄 Menu-Driven Interface

The application provides a simple menu-driven interface.

Example:

```text
========== HOTEL BOOKING SYSTEM ==========

1. View Available Rooms
2. Make Booking
3. View Bookings
4. Search Booking
5. Update Booking
6. Cancel Booking
7. Exit

Enter your choice:
```

The user can select an operation and continue performing other operations without restarting the program.

---

### ✅ Input Validation

The application can validate important information before creating or modifying a reservation.

Possible validation rules include:

- Guest name cannot be empty.
- Phone number must be valid.
- Room number must exist.
- Selected room must be available.
- Check-in date must be valid.
- Check-out date must be after check-in.
- Required information must not be empty.
- Invalid menu choices must be rejected.

Input validation helps maintain accurate and reliable reservation records.

---

## 🛠️ Technologies Used

### 🐍 Python

Python is the primary programming language used to develop the Hotel Booking System.

Python is used for:

- User interaction
- Booking logic
- Room management
- Data validation
- Date processing
- Record management
- File operations
- Database operations

---

### 📄 CSV

The CSV implementation uses file-based storage to maintain reservation information.

It provides a simple method for storing structured booking records and demonstrates Python file handling.

---

### 🗄️ SQLite

SQLite can be used as the database storage mechanism for the project.

It provides a lightweight relational database that can store hotel booking records locally without requiring a separate database server.

---

### 📅 Date Processing

Date functionality can be used to manage check-in and check-out dates and determine the duration of a reservation.

---

### 💻 Command-Line Interface

The application uses the terminal or command prompt for user interaction.

The command-line interface keeps the project simple while allowing the main focus to remain on Python programming and reservation-management logic.

---

## 🧠 Programming Concepts Used

This project combines several fundamental Python programming concepts.

### Variables and Data Types

Variables are used to store information such as:

```text
Guest Name
Phone Number
Room Number
Booking ID
Room Price
Check-in Date
Check-out Date
```

---

### User Input

The `input()` function is used to collect information from the user.

For example:

```python
guest_name = input("Enter Guest Name: ")
```

---

### Conditional Statements

`if`, `elif` and `else` statements are used to make decisions.

They can be used to determine:

- Whether a room is available.
- Whether entered information is valid.
- Whether a booking exists.
- Which menu option was selected.

---

### Loops

Loops allow the application to continue displaying the menu and processing multiple operations.

A `while` loop can keep the application running until the user chooses the Exit option.

---

### Functions

Functions divide the application into smaller and manageable operations.

Possible functions include:

```text
view_rooms()
make_booking()
view_bookings()
search_booking()
update_booking()
cancel_booking()
```

Using functions makes the application easier to understand, maintain and extend.

---

### Lists and Dictionaries

Lists and dictionaries can be used to represent rooms and reservation information.

A booking record can be represented as:

```python
{
    "booking_id": "HB1001",
    "guest": "Nithin",
    "room": 101,
    "check_in": "2026-10-10",
    "check_out": "2026-10-12"
}
```

---

### CRUD Operations

The Hotel Booking System follows the basic CRUD model:

```text
Create → Make Booking
Read   → View/Search Booking
Update → Modify Booking
Delete → Cancel Booking
```

These operations form the foundation of many real-world information-management systems.

---

### File Handling

The CSV version uses Python file handling to create, read and update reservation records.

---

### CSV Processing

The CSV module can be used to store structured reservation information in rows and columns.

---

### SQLite Database Operations

The SQLite version demonstrates database connectivity and SQL-based operations.

It provides practical experience with:

```text
CREATE TABLE
INSERT
SELECT
UPDATE
DELETE
```

---

### Date Processing

Date operations help calculate the duration of a guest's stay and validate reservation dates.

---

### Input Validation

Input validation ensures that incorrect or incomplete information is not unnecessarily stored in the system.

---

## ⚙️ How the System Works

When the application starts, the required storage system is initialized.

The main hotel booking menu is then displayed to the user.

The user can first view the available rooms and select an appropriate room.

When the **Make Booking** option is selected, the system asks for the guest's information and reservation dates.

The entered information is then validated.

The system checks whether the selected room is available for the requested reservation.

If the information is valid and the room is available, the system creates a new booking record.

A unique booking ID can then be assigned to the reservation.

The booking information is stored using either the CSV file or SQLite database.

The user can later view all bookings or search for a particular reservation.

If the guest needs to modify the reservation, the update operation changes the existing record.

If the guest cancels the reservation, the system cancels or removes the booking and updates the room availability.

The application returns to the main menu after completing each operation.

The process continues until the user selects the Exit option.

---

## 🔄 Booking Flow

The overall booking process can be represented as:

```text
Start
  ↓
Initialize Storage
  ↓
Display Menu
  ↓
View Available Rooms
  ↓
Select Room
  ↓
Enter Guest Details
  ↓
Enter Check-in / Check-out
  ↓
Validate Information
  ↓
Check Room Availability
  ↓
Create Booking
  ↓
Generate Booking ID
  ↓
Save Reservation
  ↓
Display Confirmation
  ↓
Return to Menu
  ↓
View / Search / Update / Cancel
  ↓
Exit
```

The system combines user interaction, decision-making, data processing and persistent storage to manage hotel reservations.

---

## 📂 Project Structure

```text
Hotel-Booking/
│
├── hotel_booking_csv.py
├── hotel_booking_sqlite.py
└── README.md
```

### 📄 File Description

**`hotel_booking_csv.py`**

This file contains the Hotel Booking System implementation using **CSV-based storage**.

It manages hotel rooms and reservation records using Python file handling and CSV operations.

The program can be used to create bookings, view reservations, search booking information, update existing records and cancel reservations.

---

**`hotel_booking_sqlite.py`**

This file contains the Hotel Booking System implementation using an **SQLite database**.

It manages hotel reservation information using database tables and SQL operations.

The SQLite implementation provides practical experience with structured database storage and CRUD operations.

---



**`README.md`**

This file contains the complete documentation for the Hotel Booking System.

It explains the project overview, problem statement, objectives, features, technologies, programming concepts, working process, booking flow, project structure, file descriptions, execution instructions, learning outcomes and future enhancements.

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

```bash
python --version
```

---

### Step 2: Open the Project Folder

Open a terminal or command prompt and navigate to the project folder:

```bash
cd Hotel-Booking
```

---

### Step 3: Run the CSV Version

Execute:

```bash
python hotel_booking_csv.py
```

The application will use CSV-based storage for reservation records.

---

### Step 4: Run the SQLite Version

Execute:

```bash
python hotel_booking_sqlite.py
```

The application will use the SQLite database for storing reservation information.

No separate SQLite installation is required because Python includes the `sqlite3` module.

---

## 💻 Example Usage

When the application starts:

```text
========== HOTEL BOOKING SYSTEM ==========

1. View Available Rooms
2. Make Booking
3. View Bookings
4. Search Booking
5. Update Booking
6. Cancel Booking
7. Exit

Enter your choice: 1
```

The system can display available rooms:

```text
----------- AVAILABLE ROOMS -----------

Room No.    Type          Price/Night
101         Single        ₹1500
102         Double        ₹2500
201         Deluxe        ₹3500
202         Suite         ₹5000
```

---

### Making a Booking

The user can select a room and enter guest information:

```text
Enter your choice: 2

Enter Guest Name: Nithin
Enter Phone Number: 9876543210
Enter Room Number: 101
Enter Check-in Date: 2026-10-10
Enter Check-out Date: 2026-10-12

✅ Booking Confirmed!

Booking ID: HB1001
Guest: Nithin
Room: 101
Check-in: 2026-10-10
Check-out: 2026-10-12
```

---

### Viewing Bookings

```text
Enter your choice: 3

----------- BOOKING LIST -----------

Booking ID   Guest      Room    Check-in      Check-out
---------------------------------------------------------
HB1001       Nithin     101     2026-10-10    2026-10-12
HB1002       Rahul      202     2026-10-11    2026-10-15
```

---

### Searching for a Booking

```text
Enter your choice: 4

Enter Booking ID: HB1001

Booking Found!

Guest       : Nithin
Room        : 101
Check-in    : 2026-10-10
Check-out   : 2026-10-12
Status      : Confirmed
```

---

### Updating a Booking

```text
Enter your choice: 5

Enter Booking ID: HB1001

Enter New Check-out Date: 2026-10-13

✅ Booking updated successfully!
```

---

### Cancelling a Booking

```text
Enter your choice: 6

Enter Booking ID: HB1001

✅ Booking cancelled successfully!
```

The room can then become available for another reservation.

---

## 💾 Data Storage

The project demonstrates two different approaches to persistent hotel booking storage.

### 📄 CSV-Based Storage

The CSV version stores reservation information in:

```text
hotel_bookings.csv
```

A simplified representation can be:

```text
BookingID,Guest,Room,CheckIn,CheckOut,Status
HB1001,Nithin,101,2026-10-10,2026-10-12,Confirmed
HB1002,Rahul,202,2026-10-11,2026-10-15,Confirmed
```

Each row represents one reservation.

The CSV approach demonstrates basic file-based persistence and is useful for understanding how Python applications can maintain records without a database.

---

### 🗄️ SQLite-Based Storage

The SQLite version stores booking information inside:

```text
hotel.db
```

A simplified booking table can contain:

```text
---------------------------------------------------------
ID | BookingID | Guest  | Room | CheckIn    | CheckOut
---------------------------------------------------------
1  | HB1001    | Nithin | 101  | 2026-10-10 | 2026-10-12
2  | HB1002    | Rahul  | 202  | 2026-10-11 | 2026-10-15
```

SQL operations can then be used to manage the records:

```text
INSERT → Create Booking
SELECT → View/Search Booking
UPDATE → Modify Booking
DELETE → Cancel Booking
```

This provides practical experience with relational database management.

---

## 💰 Booking Cost Calculation

The system can calculate the estimated total booking cost using the room price and number of nights.

The basic formula is:

```text
Total Cost = Room Price × Number of Nights
```

For example:

```text
Room Type  : Deluxe
Price      : ₹3500/night
Stay       : 3 nights

Total Cost = ₹3500 × 3
           = ₹10500
```

This functionality demonstrates how a reservation system can perform calculations based on user-provided dates and room information.

---

## 🔐 Data Validation and Booking Rules

A reservation system must validate information before creating a booking.

The application can apply rules such as:

```text
Guest name cannot be empty.
Room number must be valid.
Selected room must be available.
Check-in date must be valid.
Check-out date must be after check-in.
Required contact information must be provided.
Invalid menu choices must be rejected.
```

These validations help maintain accurate booking records and reduce invalid data.

---

## 📚 Learning Outcomes

Developing the Hotel Booking System provided practical experience in converting a real-world reservation problem into a structured Python application.

The project helped me understand how information about rooms, guests and reservations can be represented using Python data structures and managed through program logic.

The project provided hands-on experience with **CRUD operations**, where reservations can be created, viewed, searched, updated and cancelled.

Working with room availability introduced the concept of maintaining and updating the state of resources based on user operations.

The project also provided experience with date-based calculations, including determining the duration of a stay and calculating the estimated booking cost.

The CSV implementation helped me understand file-based persistence and how structured reservation records can be stored in a CSV file.

The SQLite implementation provided practical experience with relational databases, SQL queries, table management and database-based CRUD operations.

Input validation also demonstrated the importance of checking user-provided information before storing or processing it.

Overall, this project strengthened my knowledge of **Python programming, functions, loops, conditional statements, data structures, CRUD operations, file handling, CSV processing, SQLite databases, SQL queries, date processing, validation, and menu-driven application development**.

---

## 🔮 Future Enhancements

The current Hotel Booking System provides the basic functionality required for reservation management, but it can be extended with more advanced features.

Possible enhancements include:

- 🏨 Multiple hotel branches.
- 🛏️ More room categories.
- 📅 Advanced room availability checking.
- 💰 Dynamic pricing.
- 🧾 Automatic invoice generation.
- 💳 Online payment integration.
- 📧 Email booking confirmation.
- 📱 SMS notifications.
- 👤 Customer login and registration.
- 🔐 Admin authentication.
- 🧑‍💼 Staff management.
- 🧹 Housekeeping management.
- ⭐ Customer reviews and ratings.
- 🎁 Discount and coupon system.
- 📊 Revenue reports.
- 📈 Booking analytics.
- 🖥️ Graphical User Interface.
- 🌐 Web-based booking platform.
- 📱 Mobile application.
- ☁️ Cloud database integration.

These improvements could transform the basic educational project into a more complete hotel reservation and management platform.

---

## 🎓 Project Purpose

This project was developed as part of my **Python Mini Projects** collection to strengthen programming fundamentals through practical implementation.

The Hotel Booking System demonstrates how a real-world reservation process can be represented using software. It combines guest management, room availability, reservation creation, booking searches, updates, cancellations, and data persistence into a single application.

The project also demonstrates the difference between **file-based storage and database-based storage** through CSV and SQLite implementations.

The application is primarily intended for **learning and educational purposes** and provides a foundation for developing more advanced reservation, hotel management and booking applications.

---



</div>
