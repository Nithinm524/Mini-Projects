# 🧠 Quiz Application

<div align="center">

<img src="quiz.png" alt="Quiz Python Mini Project" width="100%">

</div>

### A Python-Based Interactive Quiz and Leaderboard System
---

The **Quiz Application** is a Python-based mini project developed to provide an interactive question-and-answer experience through a simple command-line interface. The application presents a set of multiple-choice questions to the user, accepts answers, evaluates them immediately, and calculates the final score after all questions have been attempted.

The project is designed around a simple but practical quiz workflow. When the application starts, the user can choose to take the quiz, view the leaderboard, or exit the application. During the quiz, the user is asked to enter their name and answer a series of multiple-choice questions. Each question contains four options, and the user selects an answer by entering the corresponding option number.

After every question, the application checks whether the selected answer is correct. If the answer is correct, the score is increased, and a confirmation message is displayed. If the answer is incorrect, the application displays the correct answer. Once all questions have been completed, the final score is calculated and displayed to the player.

The project contains **two implementations with different storage mechanisms**. The **CSV version** stores quiz scores in a CSV file, while the **SQLite version** stores scores in a SQLite database. Both versions provide the same core quiz functionality while demonstrating two different approaches to persistent data storage.

The application also includes a **leaderboard system** that retrieves previously recorded quiz attempts and displays players according to their scores. This makes the project more interactive because users can compare their performance with previous attempts.

This project was developed as part of my **Python Mini Projects** collection to strengthen programming fundamentals through practical implementation and to understand how user interaction, conditional logic, loops, collections, file handling, and databases can be combined to create a complete quiz application.



<br>
<br>


## 📌 Project Overview

The Quiz Application is a menu-driven educational application that allows users to participate in a multiple-choice quiz and record their results.

The application currently contains five questions covering general knowledge and computer science concepts. Each question contains four possible answers, with one option identified as the correct answer.

When the user selects **Take Quiz**, the application asks for the player's name. The quiz then begins and presents the questions one by one.

For each question, all four available options are displayed. The user enters an answer from 1 to 4. The program validates the entered choice and compares it with the predefined correct answer.

If the selected option matches the correct answer, the program displays:

```text
Correct!
```

and increases the player's score.

If the selected option is incorrect, the application displays a message containing the correct answer.

After all five questions have been answered, the application displays the player's final score in the following format:

```text
Quiz Over! Player, you scored 4/5
```

The score is then stored permanently using either CSV or SQLite storage.

The user can subsequently select **View Leaderboard** from the main menu to see previously recorded attempts arranged according to score.

<br>
<br>


## 💡 Problem Statement

Traditional paper-based quizzes require manual evaluation and make it difficult to maintain a record of previous results.

A simple digital quiz system can automate the process of displaying questions, accepting answers, checking correctness and calculating scores.

The objective of this project is to develop a Python-based quiz application that can provide an interactive multiple-choice quiz while maintaining a record of player scores.

The system should:

- Accept the player's name.
- Display multiple-choice questions.
- Provide four options for each question.
- Accept the user's answer.
- Validate the selected option.
- Check whether the answer is correct.
- Calculate the player's score.
- Display the correct answer for incorrect responses.
- Store completed quiz results.
- Display previous results through a leaderboard.
- Provide both CSV and SQLite storage implementations.

The project demonstrates how a simple problem can be converted into a complete interactive application using Python.

<br>
<br>


## 🎯 Objectives

The main objective of this project is to develop an interactive quiz application using Python.

The specific objectives are:

- To create a simple multiple-choice quiz system.
- To accept and process player information.
- To display questions and answer options.
- To validate user-selected answers.
- To identify correct and incorrect responses.
- To calculate the final quiz score.
- To provide immediate feedback after each question.
- To store player results permanently.
- To implement a leaderboard.
- To understand CSV-based data storage.
- To understand SQLite database storage.
- To practice loops and conditional statements.
- To use Python dictionaries and lists for structured quiz data.
- To implement a menu-driven application.
- To improve logical thinking and problem-solving skills.

<br>
<br>


## ✨ Features

### 🧑 Player Name

Before starting the quiz, the application asks the user to enter their name.

The program also checks whether the name is empty. If no name is entered, the application displays an error message and does not start the quiz.

Example:

```text
Enter Your Name: Nithin
```

This name is later stored along with the player's score.

---

### ❓ Multiple-Choice Questions

The application contains a collection of predefined questions.

Each question contains:

- Question text
- Four answer options
- Correct answer

The questions are stored using Python dictionaries inside a list, making the quiz data structured and easy to manage.

A simplified structure is:

```python
{
    "question": "What does CPU stand for?",
    "options": [
        "Central Process Unit",
        "Central Processing Unit",
        "Computer Personal Unit",
        "Central Processor Utility"
    ],
    "answer": 2
}
```

---

### 🔢 Four Answer Options

Every question provides four possible choices.

The user selects an answer by entering a number from **1 to 4**.

Example:

```text
1. Central Process Unit
2. Central Processing Unit
3. Computer Personal Unit
4. Central Processor Utility

Your Answer (1-4): 2
```

---

### ✅ Answer Validation

The application checks the user's answer against the predefined correct answer.

If the selected option is correct:

```text
Correct!
```

The score is increased by one.

If the answer is incorrect, the program identifies and displays the correct option.

Example:

```text
Wrong! Correct answer: Central Processing Unit
```

This provides immediate feedback to the user.

---

### 📊 Score Calculation

The application maintains a score counter during the quiz.

Initially:

```text
score = 0
```

Whenever the player selects the correct answer, the score is increased:

```text
score += 1
```

After all questions have been completed, the final score is displayed.

For example:

```text
Quiz Over! Nithin, you scored 4/5
```

---

### 🏆 Leaderboard

The application provides a leaderboard that displays previously recorded quiz attempts.

The leaderboard contains:

```text
Rank
Player
Score
```

Example:

```text
----------- LEADERBOARD -----------

Rank  Player               Score
1     Nithin               5/5
2     Rahul                4/5
3     Priya                3/5
```

The leaderboard allows players to compare their performance with previous attempts.

---

### 💾 CSV Score Storage

The CSV version stores quiz results in a file named:

```text
quiz_scores.csv
```

The file contains:

```text
Player, Score, Total
```

Each completed quiz adds a new record to the file.

---

### 🗄️ SQLite Score Storage

The SQLite version stores quiz results in:

```text
quiz.db
```

The database contains a `scores` table with fields for:

- ID
- Player
- Score
- Total

This allows quiz attempts to be stored in a structured relational database.

---

### 🔄 Menu-Driven Interface

The application provides a simple main menu:

```text
========== QUIZ APP ==========

1. Take Quiz
2. View Leaderboard
3. Exit
```

The user can repeatedly select different operations until the Exit option is selected.

---

### 🚪 Exit Option

The user can terminate the application by selecting:

```text
3. Exit
```

The program then displays:

```text
Thank You!
```

and stops execution.

<br>
<br>

## 🛠️ Technologies Used

### 🐍 Python

Python is the primary programming language used to develop the complete quiz application.

Python is used for:

- Quiz logic
- User input
- Question processing
- Answer validation
- Score calculation
- Menu management
- Data storage

---

### 📄 CSV

The CSV version uses Python's built-in `csv` module to store player scores in a structured file.

CSV provides a simple way to maintain persistent quiz results without requiring a database.

---

### 🗄️ SQLite

The SQLite version uses Python's built-in `sqlite3` module to create and manage a local database.

SQLite is used to store player names and quiz scores in a structured table.

---

### 💻 Command-Line Interface

The application uses the terminal or command prompt for all user interaction.

The CLI displays questions, options, feedback, scores and leaderboard information.

<br>
<br>


## 🧠 Programming Concepts Used

The project combines several fundamental Python concepts into a complete application.

### Lists

A list is used to store multiple quiz questions.

```python
QUESTIONS = [
    {...},
    {...},
    {...}
]
```

This allows the program to process each question sequentially.

---

### Dictionaries

Each quiz question is represented using a dictionary containing:

```text
question
options
answer
```

This provides a structured way to represent individual questions.

---

### Functions

The application divides its functionality into separate functions.

Examples include:

```text
create_connection()
create_table()
create_file()
take_quiz()
view_leaderboard()
main()
```

Functions make the program easier to organize and maintain.

---

### Loops

A `for` loop is used to process every question in the quiz.

A `while` loop is used to continuously display the main menu until the user selects Exit.

---

### Conditional Statements

`if`, `elif`, and `else` statements are used for:

- Checking the menu choice.
- Validating the player name.
- Checking whether an answer is correct.
- Handling invalid choices.
- Displaying appropriate messages.

---

### Input Validation

The program checks whether the entered player name is empty.

It also checks whether the answer entered by the user is a numeric value before comparing it with the correct answer.

Example:

```python
if choice.isdigit() and int(choice) == q["answer"]:
```

---

### Enumeration

The `enumerate()` function is used to number questions and answer options.

For example:

```python
for i, q in enumerate(QUESTIONS, start=1):
```

This allows questions to be displayed as:

```text
Q1
Q2
Q3
Q4
Q5
```

---

### File Handling

The CSV implementation uses Python file handling to create, read and append quiz results.

---

### CSV Processing

The `csv` module is used to write player results into the score file and read them when generating the leaderboard.

---

### SQLite Database Operations

The SQLite implementation uses:

```python
sqlite3.connect()
```

to establish a database connection.

SQL commands are used to create the table, insert scores and retrieve leaderboard records.

---

### Sorting

The CSV implementation sorts leaderboard records based on the player's score.

```python
rows.sort(key=lambda r: int(r[1]), reverse=True)
```

The highest score therefore appears first.

<br>
<br>

## ⚙️ How the Quiz Works

When the application starts, it initializes the required storage system.

For the CSV version, the program checks whether `quiz_scores.csv` exists. If the file does not exist, it creates the file and adds the required header.

For the SQLite version, the program establishes a connection to `quiz.db` and creates the `scores` table if it does not already exist.

After initialization, the main menu is displayed.

The user can choose:

```text
1. Take Quiz
2. View Leaderboard
3. Exit
```

When **Take Quiz** is selected, the application asks for the player's name.

The program then processes each question one by one.

For every question, four options are displayed. The player enters an answer between 1 and 4.

The application compares the selected answer with the predefined correct answer.

If the answer is correct, the score is increased.

If the answer is incorrect, the correct answer is displayed.

After all questions are completed, the final score is shown.

The score is then stored using either CSV or SQLite.

The user can return to the main menu and view the leaderboard.

The application continues running until the user chooses Exit.

<br>
<br>

## 🔄 Quiz Flow

The overall quiz flow can be summarized as:

```text
Start
  ↓
Initialize Storage
  ↓
Display Menu
  ↓
Take Quiz
  ↓
Enter Player Name
  ↓
Display Question
  ↓
Display Options
  ↓
Enter Answer
  ↓
Check Answer
  ↓
Correct / Wrong
  ↓
Update Score
  ↓
Next Question
  ↓
All Questions Completed
  ↓
Display Final Score
  ↓
Save Result
  ↓
Return to Menu
  ↓
View Leaderboard
  ↓
Exit
```

The application uses repetition to process all questions and decision-making to determine whether each selected answer is correct.

<br>
<br>

## 📂 Project Structure

```text
Quiz/
│
├── quiz_csv.py
├── quiz_sqlite.py
└── README.md
```

### 📄 File Description

**`quiz_csv.py`**

This file contains the complete Quiz Application implementation using **CSV-based score storage**.

It contains the predefined quiz questions, accepts the player's name, displays questions and options, checks answers, calculates the final score and stores completed attempts in `quiz_scores.csv`.

It also reads the stored results and generates the leaderboard by sorting players according to their scores.

---

**`quiz_sqlite.py`**

This file contains the complete Quiz Application implementation using an **SQLite database**.

It creates the `scores` table when required, accepts quiz attempts, calculates scores and stores the player's result in `quiz.db`.

It also retrieves previously stored scores from the database and displays them through the leaderboard.

---


**`README.md`**

This file contains the complete documentation for the Quiz Application.

It explains the project overview, problem statement, objectives, features, technologies, programming concepts, working process, quiz flow, project structure, file descriptions, execution instructions, learning outcomes and future enhancements.

<br>
<br>

## ▶️ How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

```bash
python --version
```

---

### Step 2: Open the Project Folder

Open a terminal or command prompt and navigate to the project directory:

```bash
cd Quiz
```

---

### Step 3: Run the CSV Version

Execute:

```bash
python quiz_csv.py
```

The program will use:

```text
quiz_scores.csv
```

to store quiz results.

---

### Step 4: Run the SQLite Version

Execute:

```bash
python quiz_sqlite.py
```

The program will use:

```text
quiz.db
```

to store quiz results.

No external SQLite installation is required because Python provides the `sqlite3` module.

<br>
<br>


## 💻 Example Quiz

When the application starts:

```text
========== QUIZ APP ==========

1. Take Quiz
2. View Leaderboard
3. Exit

Enter your choice: 1
```

The player enters their name:

```text
Enter Your Name: Nithin
```

The first question is then displayed:

```text
Q1. What is the capital of France?

  1. Berlin
  2. Madrid
  3. Paris
  4. Rome

Your Answer (1-4): 3

Correct!
```

The application continues with the remaining questions.

<br>
<br>


## 📊 Example Final Result

After all five questions:

```text
Quiz Over! Nithin, you scored 4/5
```

The result is then stored permanently.

<br>
<br>


## 🏆 Example Leaderboard

Selecting **View Leaderboard** displays:

```text
----------- LEADERBOARD -----------

Rank  Player               Score
1     Nithin               5/5
2     Rahul                4/5
3     Priya                3/5
```

The highest-scoring player appears first.

In the SQLite version, the ordering is determined by:

```sql
ORDER BY score DESC, id ASC
```

This means higher scores are displayed first, while earlier attempts are preferred when scores are equal.

<br>
<br>


## 🗃️ Data Storage

The project demonstrates two different methods of storing quiz results.

### 📄 CSV Storage

The CSV version uses a file named:

```text
quiz_scores.csv
```

The file begins with:

```text
Player, Score, Total
```

After players complete quizzes, records are added:

```text
Player, Score, Total
Nithin,5,5
Rahul,4,5
Priya,3,5
```

This approach is simple and suitable for understanding basic file-based data persistence.

---

### 🗄️ SQLite Storage

The SQLite version stores results in:

```text
quiz.db
```

The application creates a table named:

```text
scores
```

with the following fields:

```text
id
player
score
total
```

A simplified representation is:

```text
scores
-----------------------------------
ID | Player | Score | Total
-----------------------------------
1  | Nithin | 5     | 5
2  | Rahul  | 4     | 5
3  | Priya  | 3     | 5
```

The database implementation demonstrates how quiz results can be stored and retrieved using SQL.

<br>
<br>

## 📚 Current Quiz Questions

The current application contains five predefined questions.

### Question 1

**What is the capital of France?**

Correct answer:

```text
Paris
```

### Question 2

**Which language is Python named after?**

Correct answer:

```text
Monty Python
```

### Question 3

**What does CPU stand for?**

Correct answer:

```text
Central Processing Unit
```

### Question 4

**Which data structure uses FIFO?**

Correct answer:

```text
Queue
```

### Question 5

**What is 2 to the power of 10?**

Correct answer:

```text
1024
```

The questions are currently stored directly inside the Python programs using the `QUESTIONS` list.

<br>
<br>

## 📚 Learning Outcomes

Developing this project provided practical experience in designing and implementing an interactive quiz application using Python.

The project helped me understand how structured information can be represented using **lists and dictionaries**. Each question contains multiple pieces of information, including the question text, available options and correct answer.

The application also provided practical experience with **loops and conditional statements**. A loop is used to process multiple questions, while conditional logic determines whether a selected answer is correct.

Another important learning outcome was understanding how user input can be validated and processed. The application checks the player's name and verifies whether the entered answer is a valid numeric choice.

The project provided hands-on experience with **score calculation and result tracking**. A score counter is updated whenever the player provides a correct answer.

The CSV implementation introduced file-based persistence and demonstrated how quiz results can be stored and retrieved using Python's `csv` module.

The SQLite implementation provided practical experience with database connectivity, table creation, SQL insertion and SQL queries.

The leaderboard feature further demonstrated how stored data can be retrieved, sorted and presented in a meaningful way.

Overall, this project strengthened my understanding of **Python programming, lists, dictionaries, functions, loops, conditional statements, input validation, file handling, CSV processing, SQLite databases, SQL queries, sorting and menu-driven application design**.

<br>
<br>

## 🔮 Future Enhancements

The current application provides a simple quiz experience, but several features can be added in future versions.

Possible enhancements include:

- 📚 Multiple quiz categories.
- 🎯 Different difficulty levels.
- ⏱️ Time limit for each question.
- 🏆 Advanced scoring system.
- 📊 Detailed performance reports.
- 🔀 Randomized question order.
- 🔀 Randomized option order.
- 👤 User profiles.
- 🥇 Improved leaderboard system.
- 💾 Larger question database.
- ➕ Admin option to add questions.
- ✏️ Update and delete questions.
- 🖥️ Graphical User Interface.
- 🌐 Web-based quiz application.
- 📱 Mobile application.
- 🎨 Custom quiz themes.
- 🔊 Sound effects.
- ❤️ Lifelines and hints.
- 📈 Player performance history.

These improvements could transform the basic command-line quiz into a complete educational quiz platform.

<br>
<br>

## 🎓 Project Purpose

This project was developed as part of my **Python Mini Projects** collection to strengthen programming fundamentals through practical implementation.

The Quiz Application demonstrates how a simple question-and-answer concept can be converted into a complete interactive software application.

The project combines structured quiz data, user input, answer validation, score calculation, persistent storage and leaderboard functionality.

The two implementations also provide practical experience with both **file-based and database-based storage**. The CSV version demonstrates simple data persistence using files, while the SQLite version demonstrates structured storage using a relational database.

The project is primarily intended for **learning and educational purposes** and provides a foundation for developing more advanced quiz, examination and assessment systems.


</div>
