# 📱 Phone Contact Book

### A Python-Based Contact Management Application

The **Phone Contact Book** is a Python-based mini project developed to provide a simple and organized way to manage personal contact information. The application allows users to add, view, search, update and delete contacts through an easy-to-use command-line interface.

The project demonstrates how Python can be used to develop a practical data management application by combining user input, conditional statements, loops, functions, file handling and database operations. Users can maintain contact details such as name, phone number, email address and other basic information.

To provide practical experience with different storage approaches, the project contains two implementations. The **CSV version** stores contact information in a CSV file, while the **SQLite version** uses an SQLite database to store and manage contact records.

This project was developed as part of my **Python Mini Projects** collection to strengthen programming fundamentals and understand how basic Python concepts can be applied to build a useful real-world application.

---

<div align="center">

<img 
  src="phone-contact-book.png"
  alt="Phone Contact Book Python Mini Project"
  width="100%"
>

</div>

---

## 📌 Project Overview

The Phone Contact Book is designed to help users maintain their contact information in a simple digital format. Instead of keeping contact details manually, users can use the application to store and manage contacts through a Python-based interface.

When the program starts, the user is presented with a menu containing different operations. The user can choose to add a new contact, view existing contacts, search for a particular contact, update contact information or delete a contact.

The application processes the selected operation and updates the stored information accordingly. The CSV implementation uses file handling to maintain contact records, while the SQLite implementation uses database queries to perform contact management operations.

The project demonstrates the complete process of collecting user information, validating the input, storing data, retrieving records and modifying existing information.

---

## 💡 Problem Statement

Managing multiple phone contacts manually can become difficult when the number of contacts increases. Searching for a particular contact, updating an old phone number or removing unnecessary contact information can also become inconvenient.

The objective of this project is to develop a simple Python-based Contact Book that allows users to efficiently manage contact information.

The system should provide basic operations such as adding, viewing, searching, updating and deleting contacts. It should also store the information so that the records can be accessed again when required.

---

## 🎯 Objectives

The main objective of this project is to develop a simple contact management application using Python.

The specific objectives are:

- To create a digital contact management system.
- To add and store contact information.
- To display saved contacts.
- To search for contacts quickly.
- To update existing contact information.
- To delete unwanted contacts.
- To implement input validation.
- To understand file-based data storage using CSV.
- To understand database-based storage using SQLite.
- To improve Python programming and problem-solving skills.

---

## ✨ Features

### ➕ Add Contact

Allows the user to enter and save a new contact with details such as name, phone number and email address.

### 👀 View Contacts

Displays all the contacts currently stored in the system in an organized format.

### 🔍 Search Contact

Allows the user to search for a contact using information such as name or phone number.

### ✏️ Update Contact

Allows users to modify existing contact information when details change.

### 🗑️ Delete Contact

Allows users to remove a contact that is no longer required.

### 📞 Contact Information

The application can maintain important details such as:

- Name
- Phone Number
- Email Address

### 💾 CSV Storage

The CSV version stores contact information in a structured CSV file using Python file handling.

### 🗄️ SQLite Storage

The SQLite version stores contact records inside a local SQLite database.

### 🔄 Menu-Driven Interface

The application provides a simple menu that allows users to select the required operation.

### ✅ Input Validation

The application can validate user input to reduce invalid or incomplete contact records.

---

## 🛠️ Technologies Used

### 🐍 Python

Python is used as the primary programming language for implementing the complete contact management system.

### 📄 CSV

CSV is used in one version of the project for storing contact records in a structured file format.

### 🗄️ SQLite

SQLite is used in the database version to store and manage contact records using SQL operations.

### 💻 Command-Line Interface

The application uses the terminal or command prompt to accept user input and display contact information.

---

## 🧠 Programming Concepts Used

This project provides practical experience with several important Python concepts:

- Variables and data types
- User input
- Type conversion
- Conditional statements
- `if`, `elif` and `else`
- Loops
- Functions
- Lists and dictionaries
- String operations
- File handling
- CSV file handling
- Exception handling
- SQLite database operations
- SQL queries
- CRUD operations
- Input validation
- Program control flow

These concepts are combined to create a practical contact management application.

---

## ⚙️ How the System Works

When the program starts, the main menu is displayed to the user. The user selects an operation according to their requirement.

If the user chooses **Add Contact**, the application collects the required contact information and stores it.

If the user selects **View Contacts**, the program retrieves the stored records and displays them.

The **Search Contact** operation allows the user to find a specific contact using a suitable search value. The **Update Contact** operation modifies an existing record, while the **Delete Contact** operation removes a selected contact.

The process continues until the user selects the **Exit** option.

The overall process can be summarized as:

```text
Start
  ↓
Display Menu
  ↓
Select Operation
  ↓
Add / View / Search / Update / Delete
  ↓
Process Contact Data
  ↓
Store / Retrieve / Modify Data
  ↓
Display Result
  ↓
Return to Menu
  ↓
Exit
```

---

## 🔄 Contact Management Flow

The overall contact management flow can be summarized as follows:

```text
Start
  ↓
Display Menu
  ↓
Add Contact
  ↓
Save Contact
  ↓
View Contacts
  ↓
Search Contact
  ↓
Update Contact
  ↓
Delete Contact
  ↓
Display Result
  ↓
Return to Menu
  ↓
Exit
```

The flow demonstrates how different CRUD operations can be combined to create a complete contact management application.

---

## 📂 Project Structure

```text
Phone-Contact-Book/
│
├── contact_book_csv.py
├── contact_book_sqlite.py
├── phone-contact-book.png
└── README.md
```

### 📄 File Description

**`contact_book_csv.py`**

The Python program that implements the Phone Contact Book using **CSV file storage**. It handles adding, viewing, searching, updating and deleting contact records using CSV file operations.

**`contact_book_sqlite.py`**

The Python program that implements the Phone Contact Book using an **SQLite database**. It manages contact records using database operations and SQL queries.

**`phone-contact-book.png`**

The project banner image used in the README file to visually represent the Phone Contact Book project.

**`README.md`**

The documentation file containing detailed information about the project, objectives, features, technologies, programming concepts, working process, project structure, learning outcomes and usage instructions.

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

```bash
python --version
```

### Step 2: Open the Project Folder

Open the terminal or command prompt and navigate to the project directory:

```bash
cd Phone-Contact-Book
```

### Step 3: Run the CSV Version

Execute:

```bash
python contact_book_csv.py
```

The application will start and store contact information using CSV file storage.

### Step 4: Run the SQLite Version

Execute:

```bash
python contact_book_sqlite.py
```

The application will start and store contact information using an SQLite database.

---

## 💻 Example

```text
📱 Phone Contact Book

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 1

Enter Name: Rahul
Enter Phone Number: 9876543210
Enter Email: rahul@example.com

✅ Contact added successfully!
```

Example search operation:

```text
Enter your choice: 3

Enter name to search: Rahul

Contact Found!

Name  : Rahul
Phone : 9876543210
Email : rahul@example.com
```

The exact output and menu options may vary depending on the implementation.

---

## 🗃️ Data Management

The project demonstrates two different approaches to storing contact information.

### 📄 CSV Version

The CSV implementation stores contact records in a structured text file. Python's CSV functionality is used to read existing records, add new contacts and modify or remove records when required.

This approach is simple and suitable for understanding basic file-based data management.

### 🗄️ SQLite Version

The SQLite implementation stores contact records in a local database. SQL operations are used to insert, retrieve, update and delete contact information.

This approach provides practical experience with database management and CRUD operations.

---

## 📚 Learning Outcomes

Developing this project provided practical experience in creating a real-world data management application using Python.

The project helped me understand how user input can be collected, validated and converted into structured information. It also provided hands-on experience with CRUD operations and menu-driven application design.

The CSV implementation helped me understand file-based data storage, while the SQLite implementation provided practical knowledge of databases and SQL queries.

Through this project, I also learned how the same application concept can be implemented using different data storage techniques.

---

## 🔮 Future Enhancements

The current application focuses on basic contact management, but it can be extended with additional features.

Possible improvements include:

- 🔐 Password-protected contact book
- 👥 Contact groups
- ⭐ Favorite contacts
- 📱 Multiple phone numbers
- 🖼️ Contact profile pictures
- 📧 Email validation
- 📞 Phone number validation
- 🔍 Advanced search and filtering
- 📊 Contact statistics
- 📤 Import and export contacts
- 🌐 Web-based interface
- 🖥️ Graphical User Interface
- ☁️ Cloud database integration
- 🔄 Contact backup and restore

These enhancements can transform the basic command-line application into a more complete contact management system.

---

## 🎓 Project Purpose

This project was developed as part of my **Python Mini Projects** collection to strengthen programming fundamentals through practical implementation.

The Phone Contact Book demonstrates how Python can be used to build a useful application by combining user input, functions, file handling, database operations and CRUD functionality.

The project is primarily intended for **learning and educational purposes** and provides a foundation for developing more advanced data management applications.

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐.

Your support motivates me to continue learning, building and improving more Python projects.

---

<div align="center">

### 📱 Connect • Manage • Improve

*Made with ❤️ using Python*

</div>
