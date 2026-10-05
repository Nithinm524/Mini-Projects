# 🔐 Password Generator and Manager


<div align="center">

<img  src="password-generator-manager.png" alt="Password Generator and Manager Python Mini Project" width="100%">

</div>

<br>
<br>

### A Python-Based Password Generation and Secure Credential Management Application
---
The **Password Generator and Manager** is a Python-based mini project developed to generate strong passwords and organize saved credentials in a simple and structured manner. The application combines password generation with basic password management functionality, allowing users to create random passwords, store account information, search saved credentials, update existing records, and delete credentials that are no longer required.

Managing multiple online accounts often requires users to remember different passwords for different services. Reusing the same password across multiple accounts can create security risks, while remembering many different passwords can become difficult. This project provides a simple educational solution by generating unique passwords and allowing users to maintain their account credentials in one application.

The project demonstrates how Python programming concepts can be combined to develop a practical credential management application. It makes use of **random password generation, strings, user input, functions, conditional statements, loops, file handling, data validation, and database operations**.

The project contains two implementations using different storage techniques. The **CSV version** stores credential information in a CSV file, while the **SQLite version** stores records inside a local SQLite database. Both versions provide similar password management functionality while demonstrating different approaches to persistent data storage.

This project was developed as part of my **Python Mini Projects** collection to strengthen programming fundamentals through practical implementation and to understand how password generation and credential management systems can be designed using Python.

> ⚠️ **Educational Notice:** This project is intended for learning and demonstration purposes. It should not be considered a production-ready password manager or a replacement for professionally audited password-management software.


<br>
<br>




<br>
<br>


## 📌 Project Overview

The Password Generator and Manager is a menu-driven Python application designed to help users generate strong random passwords and manage stored account credentials.

When the application starts, the user is presented with a menu containing different operations. The user can generate a new password, add a credential, view saved credentials, search for a specific account, update existing information, or delete an unwanted record.

The password generator creates passwords using a combination of characters such as uppercase letters, lowercase letters, numbers and special characters. The user can specify the required password length, allowing the application to generate passwords suitable for different requirements.

After generating a password, the user can associate it with an account or website and store the related information in the application. The stored information can later be searched or updated when required.

The project follows the basic **CRUD concept — Create, Read, Update, and Delete**. This makes the application similar to many real-world data management systems where information needs to be continuously created, retrieved, modified, and removed.

The project provides two different storage implementations. The CSV version demonstrates file-based credential storage, while the SQLite version demonstrates database-based credential storage using SQL operations.

The project therefore provides practical experience in both Python programming and basic data management while demonstrating how a simple password utility can be structured as a complete application.


<br>
<br>


## 💡 Problem Statement

Users often maintain multiple accounts across websites, applications, and online services. Each account may require a different password, making password management difficult.

Using simple or repeated passwords can reduce account security, while creating complex passwords manually can be inconvenient and time-consuming.

The objective of this project is to develop a Python-based application that can automatically generate random passwords and provide basic functionality for managing account credentials.

The system should allow users to:

- Generate random passwords.
- Specify password length.
- Include different character types.
- Add account credentials.
- View stored credentials.
- Search for specific accounts.
- Update existing credential information.
- Delete unwanted records.
- Store information using CSV or SQLite.
- Validate user input.
- Manage records through a simple menu-driven interface.

The project focuses on demonstrating password generation and data management concepts in an educational environment.


<br>
<br>


## 🎯 Objectives

The main objective of this project is to develop a Python-based password generation and credential management application.

The specific objectives are:

- To generate random and customizable passwords.
- To allow users to select password length.
- To use uppercase and lowercase characters.
- To include numbers and special characters in generated passwords.
- To provide a simple credential management system.
- To store account names and related credentials.
- To search stored account information.
- To update existing credential records.
- To delete unwanted credential records.
- To implement CRUD operations.
- To understand CSV-based data storage.
- To understand SQLite database storage.
- To implement input validation.
- To improve Python programming and problem-solving skills.
- To understand how a practical password utility can be structured.


<br>
<br>


## ✨ Features

### 🔑 Password Generation
---
The main feature of the application is its ability to generate random passwords automatically.

Instead of requiring the user to manually create a password, the program can generate a combination of different character types.

A generated password may contain:

```text
Uppercase Letters
Lowercase Letters
Numbers
Special Characters
```

The user can specify the required password length, allowing the program to generate passwords according to the selected requirement.


<br>
<br>


### 🎚️ Custom Password Length
---
The application allows users to specify how many characters should be included in the generated password.

For example:

```text
Enter password length: 16
```

The program then generates a password containing the requested number of characters.

A longer password can provide a larger search space than a short password, although password security also depends on other factors such as randomness and how the credential is stored.


<br>
<br>


### 🔤 Character Selection
---
The password generator can use different categories of characters.

These can include:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Combining different character categories helps create passwords that are more complex than simple words or predictable patterns.


<br>
<br>


### ➕ Add Credential
---
The **Add Credential** feature allows users to create a new credential record.

The application can collect information such as:

```text
Website / Application
Username
Password
```

The generated password can then be associated with the selected account and stored as a credential record.

This represents the **Create** operation in CRUD.


<br>
<br>


### 👀 View Credentials
---
The **View Credentials** feature displays the credential records stored in the application.

The application retrieves the available records and presents the relevant account information in an organized format.

For a real password manager, sensitive passwords should not be displayed openly. This educational project can be extended with authentication and protected display mechanisms in future versions.

This represents the **Read** operation in CRUD.


<br>
<br>


### 🔍 Search Credential
---
The **Search Credential** feature allows users to find a particular account without manually checking every stored record.

The user can enter a website or application name, and the program searches the stored records for matching information.

This feature becomes especially useful when the number of stored credentials increases.


<br>
<br>


### ✏️ Update Credential
---
The **Update Credential** feature allows users to modify an existing credential.

For example, if the password for an account has been changed, the user can update the stored password instead of creating a new record.

This represents the **Update** operation in CRUD.


<br>
<br>


### 🗑️ Delete Credential
---
The **Delete Credential** feature allows users to remove a credential record that is no longer required.

The application identifies the selected account and removes its stored record.

This represents the **Delete** operation in CRUD.


<br>
<br>


### 💾 CSV Storage
---
The CSV implementation stores credential information in a structured CSV file.

It demonstrates how Python file handling can be used to maintain application records without requiring a database.

This implementation is useful for understanding simple persistent data storage.


<br>
<br>


### 🗄️ SQLite Storage
---
The SQLite implementation stores credential records inside a local SQLite database.

The application can use SQL operations to insert, retrieve, update, and delete records.

This implementation provides practical experience with database-based data management.


<br>
<br>


### 🔄 Menu-Driven Interface
---
The application provides a simple menu through which users can select the required operation.

For example:

```text
1. Generate Password
2. Add Credential
3. View Credentials
4. Search Credential
5. Update Credential
6. Delete Credential
7. Exit
```

The menu-driven design allows users to perform multiple operations during a single execution.


<br>
<br>


### ✅ Input Validation
---
The application can validate important inputs before processing them.

For example, the program can check whether the password length is valid and whether required credential fields have been entered.

Input validation reduces incorrect or incomplete records.


<br>
<br>


## 🛠️ Technologies Used
---
<br>
<br>

### 🐍 Python
---
Python is the primary programming language used to develop the complete application.

It provides the required programming structures for password generation, user input, conditional logic, loops, functions, file handling, and database operations.


<br>
<br>


### 🔐 Random Password Generation
---
Python's built-in randomization functionality can be used to select characters and construct generated passwords.

The character pool can contain letters, numbers, and special characters.


<br>
<br>


### 📄 CSV
---
CSV is used for the file-based credential management implementation.

It allows account records to be stored in rows and columns and provides a simple method for maintaining persistent data.

<br>
<br>

### 🗄️ SQLite
---
SQLite is used for the database-based implementation.

It provides a lightweight local relational database that can store credential records without requiring a separate database server.

<br>
<br>

### 💻 Command-Line Interface
---
The application uses the terminal or command prompt as its user interface.

The command-line approach keeps the project simple while allowing the main focus to remain on Python logic and data management.

<br>
<br>

## 🧠 Programming Concepts Used
---
This project combines several important Python concepts into one practical application.
<br>
<br>

### Variables and Data Types
---
Variables are used to store values such as usernames, website names, passwords, password lengths, and menu choices.

### User Input
---
The `input()` function is used to collect information from the user.

### Conditional Statements
---
`if`, `elif`, and `else` statements control which operation is executed based on the user's selection.

### Loops
---
Loops allow the menu to remain active and enable users to perform multiple operations without restarting the application.

### Functions
---
The application can be divided into functions such as:

- Generate Password
- Add Credential
- View Credentials
- Search Credential
- Update Credential
- Delete Credential

These functions improve the organization and maintainability of the program.

### String Operations
---
String operations are used to construct passwords and process account information.

### Randomization
---
Random character selection is used to create generated passwords.

### File Handling
---
The CSV version uses file operations to read and write credential information.

### CSV Processing
---
Python's CSV functionality is used to manage structured credential records.

### SQLite Operations
---
The SQLite version demonstrates database connectivity and SQL queries.

### CRUD Operations
---
The application implements:

```text
Create → Add Credential
Read   → View/Search Credential
Update → Modify Credential
Delete → Remove Credential
```

### Input Validation
---
Validation helps prevent invalid or incomplete information from being stored.

### Exception Handling
---
Exception handling can be used to prevent unexpected input or file/database errors from terminating the application.

<br>
<br>

## ⚙️ How the System Works
---
When the application starts, the required storage system is initialized.

For the CSV version, the program checks whether the required CSV file exists and prepares it for storing credential records.

For the SQLite version, the program connects to the local database and ensures that the required table is available.

After initialization, the main menu is displayed.

The user can choose to generate a password or manage existing credentials.

If the user selects **Generate Password**, the application asks for the desired password length and creates a random password using the available character sets.

If the user selects **Add Credential**, the application collects account information and stores it.

The **View Credentials** operation retrieves stored records.

The **Search Credential** operation finds a particular account based on the entered search value.

The **Update Credential** operation modifies an existing record.

The **Delete Credential** operation removes an unwanted credential.

After every operation, the application can return to the main menu so that the user can continue managing credentials.

The program continues until the user selects **Exit**.

<br>
<br>

## 🔄 Password Management Flow
---
The overall application flow can be summarized as follows:

```text
Start
  ↓
Initialize Storage
  ↓
Display Menu
  ↓
Select Operation
  ↓
Generate Password
  ↓
Add Credential
  ↓
Save Credential
  ↓
View / Search Credentials
  ↓
Update Credential
  ↓
Delete Credential
  ↓
Display Result
  ↓
Return to Menu
  ↓
Exit
```

The actual operation depends on the option selected by the user.

The application demonstrates how **password generation, user input, decision-making, data processing, storage, and repeated operations** can work together in a single Python application.

<br>
<br>

## 📂 Project Structure

```text
Password-Generator-Manager/
│
├── password_generator_csv.py
├── password_generator_sqlite.py
└── README.md
```

### 📄 File Description

**`password_generator_csv.py`**

This file contains the Password Generator and Manager implementation using **CSV-based storage**.

It handles password generation, adding credentials, viewing records, searching accounts, updating credentials and deleting records using CSV file operations.

This version demonstrates how Python can maintain credential information using a simple file-based storage approach.

<br>
<br>

**`password_generator_sqlite.py`**

This file contains the Password Generator and Manager implementation using an **SQLite database**.

It manages credential records using database operations and SQL queries.

The program can insert new credentials, retrieve records, search accounts, update stored information and delete credentials.

This version provides practical experience with relational databases and CRUD operations.

<br>
<br>


**`README.md`**

This file contains the complete documentation of the Password Generator and Manager project.

It explains the project overview, problem statement, objectives, features, technologies, programming concepts, working process, application flow, project structure, file descriptions, execution instructions, learning outcomes and future enhancements.

<br>
<br>

## ▶️ How to Run

<br>
<br>
### Step 1: Install Python
---
Make sure Python is installed on your computer.

Check the installation using:

```bash
python --version
```

<br>
<br>

### Step 2: Open the Project Folder
---
Open a terminal or command prompt and navigate to the project directory:

```bash
cd Password-Generator-Manager
```

<br>
<br>

### Step 3: Run the CSV Version
---
Execute:

```bash
python password_generator_csv.py
```

The application will start in the terminal and use CSV storage for maintaining credential records.

<br>
<br>

### Step 4: Run the SQLite Version
---
Execute:

```bash
python password_generator_sqlite.py
```

The application will start and use an SQLite database for storing credential information.

<br>
<br>

## 💻 Example Usage

When the program starts, a menu similar to the following can be displayed:

```text
🔐 Password Generator and Manager

1. Generate Password
2. Add Credential
3. View Credentials
4. Search Credential
5. Update Credential
6. Delete Credential
7. Exit

Enter your choice: 1
```

<br>
<br>

### Generating a Password
---
```text
Enter password length: 16

Generated Password:
X7@pL9#qT2$mN8!k
```

The generated password contains a combination of different character types.

<br>
<br>

### Adding a Credential
---
```text
Enter your choice: 2

Enter Website: example.com
Enter Username: user@example.com
Enter Password: X7@pL9#qT2$mN8!k

✅ Credential added successfully!
```

The credential is then stored using the selected storage method.

<br>
<br>

### Searching for a Credential
---
```text
Enter your choice: 4

Enter Website to search: example.com

🔍 Credential Found

Website: example.com
Username: user@example.com
```

For security reasons, a production password manager should avoid displaying stored passwords openly.

<br>
<br>

### Updating a Credential
---
```text
Enter your choice: 5

Enter Website to update: example.com

Enter New Password: R8#kP2!mX7@qL5$n

✅ Credential updated successfully!
```

<br>
<br>


### Deleting a Credential
---
```text
Enter your choice: 6

Enter Website to delete: example.com

✅ Credential deleted successfully!
```

The selected credential is removed from the storage system.

<br>
<br>

## 🗃️ Data Management

The project demonstrates two different approaches to storing credential information.
<br>
<br>


### 📄 CSV-Based Storage
---
The CSV version stores account records in a structured file.

A simplified representation can be:

```text
Website, Username, Password
example.com,user@example.com,X7@pL9#qT2$mN8!k
github.com,developer@example.com,R8#kP2!mX7@qL5$n
```

Each row represents a credential record, while the columns represent different pieces of account information.

When a new credential is added, a new record is stored.

When records are viewed or searched, the program reads the stored information.

For updates or deletions, the existing records are processed, and the modified information is saved again.

<br>
<br>

### 🗄️ SQLite-Based Storage
---
The SQLite version stores credential information in a relational database table.

A simplified structure can be represented as:

```text
Credentials
--------------------------------------------------------
ID | Website | Username | Password
--------------------------------------------------------
1  | GitHub  | developer@example.com | ********
2  | Gmail   | user@example.com      | ********
```

SQL operations can then be used to manage the records:

```text
INSERT → Add Credential
SELECT → View/Search Credential
UPDATE → Modify Credential
DELETE → Remove Credential
```

This implementation provides practical experience with a database-driven application.


<br>
<br>

## 🔐 Security Considerations

Password management involves sensitive information, so security is an important consideration when designing such an application.

This educational project demonstrates the basic concepts of password generation and credential storage, but storing passwords as plain text is **not appropriate for a production password manager**.

A production-level application should consider stronger security mechanisms such as:

- Encryption for stored credentials.
- Secure key management.
- Strong authentication.
- Master-password protection.
- Secure password derivation.
- Protected database access.
- Secure memory handling.
- Automatic session locking.
- Clipboard protection.
- Security auditing.

The project should therefore be treated as a **learning implementation**, not as a secure replacement for professional password-management software.

<br>
<br>

## 📚 Learning Outcomes

Developing the Password Generator and Manager provided practical experience in building an application that combines random data generation with persistent data management.

The project helped me understand how password generation can be implemented using character sets and random selection. It also demonstrated how user-defined password length can be used to control the generated output.

The project provided practical experience with **CRUD operations** by allowing credentials to be created, retrieved, searched, updated, and deleted.

The CSV implementation helped me understand file-based data persistence and how Python applications can maintain structured information using files.

The SQLite implementation provided hands-on experience with relational databases and SQL operations. It demonstrated how the same application concept can be implemented using a structured database instead of a simple file.

The project also increased my understanding of input validation, functions, loops, conditional statements, and exception handling.

Most importantly, the project helped me understand that applications dealing with sensitive information require additional security considerations beyond basic functionality.

Overall, this project strengthened my knowledge of **Python programming, randomization, string processing, file handling, CSV processing, SQLite databases, SQL queries, CRUD operations, and basic security concepts**.

<br>
<br>

## 🔮 Future Enhancements

The current implementation focuses on password generation and basic credential management, but it can be extended into a more complete password-management application.

Possible future enhancements include:

- 🔐 Master password authentication.
- 🔒 Encryption of stored credentials.
- 🛡️ Secure password hashing where appropriate.
- 🎯 Password strength evaluation.
- 📊 Password security reports.
- 🔄 Password update reminders.
- 🔍 Advanced credential search.
- 🏷️ Account categories.
- ⭐ Favorite accounts.
- 📋 Secure clipboard copying.
- ⏱️ Automatic session locking.
- 💾 Encrypted backup and restore.
- 🖥️ Graphical User Interface.
- 🌐 Web-based password manager.
- 📱 Mobile application.
- ☁️ Secure cloud synchronization.
- 🔑 Multi-factor authentication.
- 🚨 Weak or reused password detection.

These enhancements could transform the basic educational application into a more sophisticated credential-management system.

<br>
<br>

## 🎓 Project Purpose

I developed this project as part of my **Python Mini Projects** collection to strengthen my programming fundamentals through practical implementation.

The Password Generator and Manager demonstrates how a common problem—creating and organizing passwords—can be converted into a functional Python application.

The project combines password generation, user interaction, data validation, file handling, database operations, and CRUD functionality into a single application.

The two implementations also provide an opportunity to compare file-based and database-based data storage.

The project is primarily intended for **learning and educational purposes**. It provides a foundation for understanding how to design applications that handle sensitive information and why additional security mechanisms are necessary when developing production-ready systems.



</div>
