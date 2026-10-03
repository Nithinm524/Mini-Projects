# 📱 Phone Contact Book

<div align="center">

<img src="phone-contact-book.png" alt="Phone Contact Book Python Mini Project" width="100%">

</div>
<br>
<br>


### A Python-Based Contact Management Application
---

The **Phone Contact Book** is a Python-based mini project designed to provide a simple, organized and efficient way to store and manage personal contact information. The application allows users to maintain important details such as contact names, phone numbers, and email addresses through a simple command-line interface.

In everyday situations, people may need to manage a large number of contacts and frequently perform operations such as adding a new contact, finding an existing contact, changing an outdated phone number, or removing a contact that is no longer required. A digital contact management system makes these operations easier by allowing information to be stored systematically and accessed whenever required.

This project demonstrates how fundamental Python programming concepts can be combined to develop a practical data management application. Instead of implementing only individual programming examples, the project combines **variables, functions, conditional statements, loops, user input, string processing, file handling, data validation, and database operations** into one complete application.

The project contains two different implementations for storing contact information. The **CSV-based implementation** uses a CSV file to store and retrieve contact records, while the **SQLite-based implementation** uses a local SQLite database and SQL queries to manage the same type of information. This provides practical experience in understanding the difference between simple file-based storage and structured database storage.

The Phone Contact Book is developed as part of my **Python Mini Projects** collection to strengthen programming fundamentals through practical implementation. It also provides a foundation for understanding how simple command-line applications can be gradually extended into more advanced contact management systems.


<br>
<br>

## 📌 Project Overview

The Phone Contact Book is a menu-driven Python application that allows users to manage contact information through a sequence of simple operations. The application is designed around the basic CRUD concept, which represents **Create, Read, Update, and Delete** operations.

When the application starts, the user is presented with a menu containing different options. The user can choose to add a new contact, display existing contacts, search for a particular contact, update an existing record, or delete a contact.

When a new contact is added, the application collects the required information from the user and stores it permanently. The stored information can later be retrieved using the view or search operations. If a contact's information changes, the update operation allows the existing record to be modified without creating a completely new contact.

The delete operation allows unnecessary records to be removed from the system. Together, these operations provide the basic functionality required for managing a digital contact list.

The project also demonstrates two different approaches to data persistence. In the CSV version, contact information is maintained using a structured CSV file. In the SQLite version, contact records are maintained inside a local relational database. Both implementations perform similar contact management operations but use different storage techniques.

The project therefore serves two purposes: it provides a useful contact management application and demonstrates how Python applications can interact with different types of data storage systems.

<br>
<br>

## 💡 Problem Statement

Maintaining contact information manually can become inconvenient when the number of contacts increases. Important information such as phone numbers and email addresses may need to be updated regularly, and finding a specific contact manually can take unnecessary time.

A simple contact management application can solve this problem by providing a centralized place to store and manage contact information. Instead of maintaining separate handwritten records or repeatedly entering the same information, users can store contact details once and retrieve them whenever necessary.

The objective of this project is to develop a Python-based application that provides basic contact management functionality through a simple command-line interface.

The system should allow users to:

- Add new contacts.
- Store contact information permanently.
- Display all saved contacts.
- Search for specific contacts.
- Modify existing contact details.
- Delete unwanted contacts.
- Validate important user inputs.
- Maintain records using CSV or SQLite storage.

The project focuses on implementing these operations in a simple and understandable manner while demonstrating practical Python programming techniques.

<br>
<br>

## 🎯 Objectives

The primary objective of this project is to develop a functional contact management application using Python and understand how different programming concepts can be combined to solve a practical problem.

The major objectives are:

- To develop a simple digital contact management application.
- To allow users to create and store new contact records.
- To retrieve and display previously stored contact information.
- To provide a search facility for finding specific contacts.
- To allow users to modify existing contact information.
- To provide an option for deleting unwanted contacts.
- To implement proper input validation for contact details.
- To understand how Python can work with CSV files.
- To understand how Python can interact with an SQLite database.
- To implement basic CRUD operations.
- To understand data persistence in Python applications.
- To improve logical thinking and problem-solving skills.
- To gain practical experience in developing menu-driven applications.
- To understand how a simple project can be implemented using different storage mechanisms.

<br>
<br>

## ✨ Features

### ➕ Add Contact

The **Add Contact** feature allows the user to create a new contact record. The application collects information such as the contact's name, phone number and email address.

Before storing the information, the program can perform basic validation to ensure that required fields are not empty and that important values follow the expected format.

Once the information is accepted, the contact is stored in the selected storage system. In the CSV version, the information is written into the CSV file, while the SQLite version inserts the record into the database.

This feature represents the **Create** operation in CRUD.

<br>
<br>

### 👀 View Contacts

The **View Contacts** feature retrieves the contact records currently stored in the system and displays them to the user.

The application reads the available records and presents the information in an organized format so that users can easily understand the stored data.

This operation is useful when users want to review their complete contact list instead of searching for one particular person.

In the CSV implementation, the program reads the records from the CSV file. In the SQLite implementation, the application retrieves records using SQL queries.

This feature represents the **Read** operation in CRUD.

<br>
<br>

### 🔍 Search Contact

The **Search Contact** feature allows users to find a particular contact without displaying the entire contact list.

The user can provide a search value such as a name or phone number. The application compares the entered value with the stored records and displays the matching contact information.

This feature demonstrates how stored data can be filtered based on user requirements. It also improves the usability of the application when a large number of contacts are present.

<br>
<br>

### ✏️ Update Contact

The **Update Contact** feature allows users to modify existing contact information.

For example, if a contact changes their phone number or email address, the user does not need to delete the entire contact and create it again. Instead, the existing record can be located and updated.

The application identifies the appropriate contact, accepts the new information and saves the modified record.

This feature represents the **Update** operation in CRUD.

<br>
<br>

### 🗑️ Delete Contact

The **Delete Contact** feature allows users to remove a contact from the system.

When the user selects this operation, the application identifies the required contact and removes its record from the storage system.

In the CSV implementation, the required records can be read and rewritten without the deleted contact. In the SQLite implementation, an SQL `DELETE` operation can be used to remove the selected database record.

This feature represents the **Delete** operation in CRUD.

<br>
<br>

### 📞 Contact Information

The application can maintain important information associated with each contact, including:

- Name
- Phone Number
- Email Address

These fields provide a basic structure for maintaining useful contact information while keeping the project simple enough for learning and experimentation.

<br>
<br>

### 💾 CSV Data Storage

The CSV version provides a simple file-based method of storing contact information.

CSV stands for **Comma-Separated Values** and is commonly used to store structured tabular information in a text file.

The Python program can read existing records from the CSV file, add new records and modify the stored information when required.

This implementation helps demonstrate how applications can maintain data even after the program is closed.

<br>
<br>

### 🗄️ SQLite Database Storage

The SQLite version uses a local relational database to store contact records.

SQLite provides a structured way of storing information using tables, columns and rows. Python can communicate with the SQLite database using SQL commands.

Operations such as inserting a contact, retrieving records, updating information and deleting contacts can be performed using SQL queries.

This implementation provides practical experience with database-based application development.

<br>
<br>

### 🔄 Menu-Driven Interface

The application uses a menu-driven interface to make interaction simple.

The user is shown a list of available operations and selects the required option. After completing the selected operation, the program can return to the main menu so that another operation can be performed.

This structure makes the application easy to understand and demonstrates how loops can be used to maintain continuous program execution.

<br>
<br>

### ✅ Input Validation

Input validation helps prevent incorrect or incomplete data from being stored.

For example, the program can check whether the contact name is empty, whether a phone number contains the expected number of digits and whether an email address follows a basic format.

Validation improves the reliability of the stored information and demonstrates how programs can handle incorrect user input.

<br>
<br>

## 🛠️ Technologies Used

### 🐍 Python

Python is the primary programming language used to develop the Phone Contact Book.

It provides the programming structures required for user input, conditional logic, loops, functions, file operations, exception handling and database connectivity.

Python's simple syntax also makes it suitable for developing and understanding beginner-friendly applications.

<br>
<br>

### 📄 CSV

CSV is used as the storage mechanism for the file-based implementation.

The CSV format organizes information into rows and columns, making it suitable for storing simple structured contact records.

Python's CSV functionality allows the program to read and write contact information without requiring an external database server.

<br>
<br>


### 🗄️ SQLite

SQLite is used as the storage mechanism for the database implementation.

It provides a lightweight relational database that can be stored locally as a database file. The application can use SQL queries to insert, retrieve, update and delete contact records.

SQLite is useful for learning database concepts because it does not require a separate database server.

<br>
<br>

### 💻 Command-Line Interface

The application uses the terminal or command prompt as its user interface.

The command-line approach keeps the project simple and allows the main focus to remain on programming logic, data management and storage operations.

<br>
<br>


## 🧠 Programming Concepts Used

This project combines several important Python programming concepts into one practical application.

### Variables and Data Types

Variables are used to temporarily store values such as contact names, phone numbers, email addresses and menu choices.

Different data types are used depending on the information being processed.

### User Input

The `input()` function is used to collect information entered by the user.

This allows the application to interact dynamically with the person using the program.

### Conditional Statements

`if`, `elif,` and `else` statements are used to determine which operation should be performed based on the user's menu selection.

### Loops

Loops are used to repeatedly display the menu and allow users to perform multiple operations without restarting the program after every action.

### Functions

Functions can be used to divide the application into smaller logical components such as:

- Add Contact
- View Contacts
- Search Contact
- Update Contact
- Delete Contact

This makes the program easier to understand, maintain, and modify.

### File Handling

The CSV implementation uses file handling concepts to open, read, and write contact information.

### CSV Processing

Python's CSV functionality is used to process structured contact records stored in CSV format.

### SQLite Database Operations

The SQLite implementation demonstrates how Python can connect to a database and execute SQL commands.

### CRUD Operations

The project provides a practical implementation of:

```text
Create → Add Contact
Read   → View/Search Contact
Update → Modify Contact
Delete → Remove Contact
```

### Exception Handling

Exception handling can be used to prevent the program from terminating unexpectedly when invalid input or an unexpected operation occurs.

### Input Validation

Validation ensures that the information entered by the user satisfies basic requirements before being stored.

<br>
<br>


## ⚙️ How the System Works

The application begins by initializing the required storage system. For the CSV implementation, the program checks or creates the required CSV file. For the SQLite implementation, the program connects to the database and ensures that the required contact table is available.

After initialization, the main menu is displayed.

The user selects an operation from the available options. Depending on the selected option, the application performs the corresponding operation.

For example, when the user chooses **Add Contact**, the program asks for the contact information and stores it.

When the user chooses **View Contacts**, the program retrieves all available records and displays them.

When **Search Contact** is selected, the application compares the search value against stored information and displays matching records.

For **Update Contact**, the application identifies the required record, accepts new information and saves the modified data.

For **Delete Contact**, the selected record is removed from the storage system.

After completing an operation, the program can return to the main menu. This allows the user to perform multiple contact management operations during the same execution.

The application continues this process until the user selects the **Exit** option.

<br>
<br>

## 🔄 Contact Management Flow

The overall contact management flow can be summarized as follows:

```text
Start
  ↓
Initialize Storage
  ↓
Display Menu
  ↓
Select Operation
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

The actual operation performed depends on the option selected by the user. After completing an operation, the system returns to the menu so that the user can continue managing contacts.

This flow demonstrates how **input, decision-making, data processing, storage and repetition** work together in a practical Python application.

<br>
<br>

## 📂 Project Structure

```text
Phone-Contact-Book/
│
├── contact_book_csv.py
├── contact_book_sqlite.py
└── README.md
```
<br>
<br>

### 📄 File Description
---

**`contact_book_csv.py`**

This file contains the complete implementation of the Phone Contact Book using **CSV-based storage**. It is responsible for accepting contact information from the user, validating the input, performing contact operations and maintaining the records inside a CSV file.

The program demonstrates how Python can be used to perform data management operations without requiring a database system.

<br>
<br>

**`contact_book_sqlite.py`**

This file contains the complete implementation of the Phone Contact Book using an **SQLite database**.

The program creates or connects to the local SQLite database and performs operations such as inserting new contacts, retrieving records, searching for contacts, updating existing information and deleting records.

This version demonstrates how Python applications can use SQL and relational database concepts for structured data management.

<br>
<br>

**`phone-contact-book.png`**

This image is the visual banner used in the README file to represent the Phone Contact Book project.

It provides a visual introduction to the project and makes the GitHub documentation more attractive and professional.

<br>
<br>


**`README.md`**

This file contains the complete documentation of the Phone Contact Book project.

It explains the project overview, problem statement, objectives, features, technologies, programming concepts, working process, flow, project structure, file descriptions, execution instructions, learning outcomes and possible future improvements.

<br>
<br>


## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installed version using:

```bash
python --version
```

If Python is installed correctly, the terminal will display the installed Python version.

<br>
<br>

### Step 2: Open the Project Folder

Open a terminal or command prompt and navigate to the Phone Contact Book directory.

```bash
cd Phone-Contact-Book
```

<br>
<br>

### Step 3: Run the CSV Version

To execute the CSV-based implementation:

```bash
python contact_book_csv.py
```

The program will start in the terminal and use CSV file storage for maintaining contact records.

<br>
<br>

### Step 4: Run the SQLite Version

To execute the SQLite-based implementation:

```bash
python contact_book_sqlite.py
```

The program will start and use the SQLite database for storing contact information.

<br>
<br>

## 💻 Example Usage

When the program starts, a menu similar to the following can be displayed:

```text
📱 Phone Contact Book

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit

Enter your choice: 1
```
<br>
<br>

### Adding a Contact
---
```text
Enter Name: Rahul
Enter Phone Number: 9876543210
Enter Email: rahul@example.com

✅ Contact added successfully!
```

The entered information is then stored in the selected storage system.

<br>
<br>

### Viewing Contacts
---
```text
Enter your choice: 2

Name: Rahul
Phone: 9876543210
Email: rahul@example.com

Name: Priya
Phone: 9123456780
Email: priya@example.com
```

The application retrieves and displays the available contact records.

<br>
<br>

### Searching for a Contact
---
```text
Enter your choice: 3

Enter name to search: Rahul

🔍 Contact Found

Name : Rahul
Phone: 9876543210
Email: rahul@example.com
```

The program searches the stored records and displays the matching contact.

<br>
<br>

### Updating a Contact
---
```text
Enter your choice: 4

Enter name to update: Rahul

Enter New Phone Number: 9988776655
Enter New Email: rahul_new@example.com

✅ Contact updated successfully!
```

The existing contact information is replaced with the updated information.

<br>
<br>

### Deleting a Contact
---
```text
Enter your choice: 5

Enter name to delete: Rahul

✅ Contact deleted successfully!
```

The selected contact is removed from the storage system.

<br>
<br>

### 🗃️ Data Management
---

One of the important aspects of this project is understanding how application data can be stored and maintained.

The project uses two different storage approaches: **CSV-based storage** and **SQLite-based storage**.
<br>
<br>


### 📄 CSV-Based Storage
---
The CSV implementation stores contact information in a file containing structured rows and columns.

Each row represents a contact, while the columns represent individual attributes such as name, phone number and email.

A simplified structure can be represented as:

```text
Name, Phone, Email
Rahul,9876543210,rahul@example.com
Priya,9123456780,priya@example.com
```

When a new contact is added, a new record is written to the CSV file.

When contacts need to be displayed or searched, the program reads the stored records.

For updating or deleting records, the program can read the existing information, modify the required record and write the updated information back to the file.

This approach is simple and useful for learning basic data persistence and file handling.

<br>
<br>

### 🗄️ SQLite-Based Storage
---
The SQLite implementation uses a relational database structure.

Contact records are stored in a table where each row represents one contact and each column represents a particular attribute.

A simplified database structure can be represented as:

```text
Contacts
------------------------------------------------
ID | Name  | Phone       | Email
------------------------------------------------
1  | Rahul | 9876543210  | rahul@example.com
2  | Priya | 9123456780  | priya@example.com
```

The application can use SQL commands to perform different operations.

For example:

```text
INSERT → Add a new contact
SELECT → View or search contacts
UPDATE → Modify contact information
DELETE → Remove a contact
```

This approach provides practical experience with relational databases and SQL-based data management.

<br>
<br>

## 🔐 Data Validation

Data validation is an important part of a contact management application because incorrect information can reduce the usefulness of the stored records.

The program can check whether required fields have been entered before saving a contact.

For example, the contact name should not be empty and the phone number should follow a suitable format.

Basic validation can also be applied to email addresses to ensure that the user enters a reasonable value.

Validation helps prevent incomplete records and improves the overall reliability of the application.

<br>
<br>

## 📚 Learning Outcomes

Developing the Phone Contact Book provided practical experience in designing and implementing a complete Python application rather than working with isolated programming examples.

The project helped me understand how a real-world problem can be divided into smaller operations and implemented using functions and structured program logic.

I gained practical experience in handling user input, validating information and controlling program execution using conditional statements and loops.

The project also helped me understand **CRUD operations**, which are fundamental to many data management applications. Implementing Create, Read, Update and Delete operations provided a practical understanding of how information is added, retrieved, modified and removed.

The CSV implementation provided hands-on experience with file-based storage and demonstrated how information can remain available even after the Python program is closed.

The SQLite implementation provided additional experience with relational databases and SQL queries. It helped demonstrate how structured data can be stored and managed more efficiently using a database.

Another important learning outcome was understanding that the same application functionality can be implemented using different storage mechanisms while keeping the main application concept similar.

Overall, the project strengthened my understanding of Python programming, data management, CRUD operations, file handling and database connectivity.

<br>
<br>

## 🔮 Future Enhancements

The current version focuses on basic contact management, but the project can be expanded into a more complete contact management system.

Possible future enhancements include:

- 🔐 Password-protected contact management.
- 👥 Contact groups and categories.
- ⭐ Favorite or frequently used contacts.
- 📱 Support for multiple phone numbers.
- 📧 Improved email validation.
- 📞 Advanced phone number validation.
- 🖼️ Contact profile pictures.
- 🔍 Advanced search and filtering.
- 🔤 Sorting contacts alphabetically.
- 📊 Contact statistics and summaries.
- 📤 Import contacts from external files.
- 📥 Export contacts to different formats.
- 💾 Backup and restore functionality.
- 🖥️ Graphical User Interface using Tkinter.
- 🌐 Web-based contact management system.
- ☁️ Cloud database integration.
- 🔄 Synchronization between devices.
- 👤 User accounts and authentication.

These enhancements can gradually transform the basic command-line application into a complete contact management platform.

<br>
<br>

## 🎓 Project Purpose

This project was developed as part of my **Python Mini Projects** collection with the purpose of improving programming skills through practical application development.

The Phone Contact Book demonstrates how fundamental Python concepts can be combined to solve a common data management problem.

Rather than focusing only on displaying information, the project demonstrates the complete lifecycle of data. Information is entered by the user, validated, stored, retrieved, searched, modified and eventually deleted when it is no longer required.

The two implementations also provide an opportunity to understand the difference between file-based and database-based storage. The CSV version demonstrates a simple approach to persistent data storage, while the SQLite version introduces relational database concepts and SQL operations.

The project is primarily intended for **learning and educational purposes** and can serve as a foundation for developing more advanced Python applications involving file handling, databases and user interfaces.

<br>
<br>



</div>
