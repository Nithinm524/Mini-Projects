# 🎯 Number Guessing Game

### A Python-Based Interactive Number Guessing Application

The **Number Guessing Game** is a Python-based mini project developed to demonstrate how fundamental programming concepts can be combined to create a simple, interactive and engaging application. The game generates a random number within a predefined range and challenges the user to identify the number by entering guesses through the command-line interface.

The application provides feedback after every attempt so that the user can gradually reach the correct answer. When the entered number is lower than the generated number, the program indicates that the user should try a higher number. Similarly, when the entered number is greater than the generated number, the program provides a hint to try a lower number. The game continues until the user successfully identifies the generated number.

Although the application is simple, it provides practical experience with several important Python programming concepts. It demonstrates how **random number generation, user input, conditional statements, loops, comparison operators, and counters** can work together to create a complete program.

The project was developed as part of my Python Mini Projects collection to strengthen programming fundamentals through hands-on implementation. It also provides a foundation for understanding how simple logic can be extended into more advanced games and interactive applications.

<br>
<br>

## 📌 Project Overview

The Number Guessing Game is designed as a beginner-friendly interactive application where the computer selects a random number and the player attempts to identify it.

When the program starts, it generates a random number within a specified range. The user is then prompted to enter a number as their guess. The application compares the entered value with the randomly generated number and determines whether the guess is correct, too low, or too high.

If the user's guess is lower than the target number, the program displays a message asking the user to try a higher number. If the guess is higher than the target number, the program provides the opposite hint. The user can continue making guesses until the correct number is identified.

The application can also keep track of the number of attempts made by the player. This makes the program more interactive and provides an opportunity to understand how counters and repeated operations can be implemented in Python.

The project focuses on simplicity while demonstrating the complete flow of an interactive application, starting from generating data and accepting user input to processing the input, providing feedback, and terminating the game when the correct answer is found.

<br>
<br>

## 💡 Problem Statement

A simple number guessing game requires the program to generate an unpredictable number and provide the player with enough information to reach the correct answer through repeated attempts.

The objective of this project is to develop a Python application that can automatically generate a random number and allow the user to interact with the program by entering guesses.

The system must compare each guess with the generated number and provide appropriate feedback. It should continue accepting guesses until the user finds the correct number.

This project provides a simple example of how a computer program can make decisions based on user input and repeatedly execute a particular operation until a required condition is satisfied.

<br>
<br>

## 🎯 Objectives

The main objective of this project is to develop an interactive Python game while gaining practical experience with fundamental programming concepts.

The specific objectives are:

- To develop a simple interactive application using Python.
- To understand random number generation.
- To accept and process input provided by the user.
- To compare user input with a randomly generated value.
- To implement conditional statements for decision-making.
- To use loops for repeated execution.
- To provide useful hints based on the user's input.
- To count and track the number of attempts.
- To improve logical thinking and problem-solving skills.
- To understand how basic programming concepts can be combined into a complete application.

<br>
<br>

## ✨ Features

### 🎲 Random Number Generation

The program generates a random number within a predefined range, ensuring that the target number is not known to the player before the game begins.

### ⌨️ User Input

The player can enter a number through the command-line interface. The entered value is processed by the program and compared with the generated number.

### 🔼 Higher or Lower Hints

The program provides useful feedback after each incorrect attempt. It indicates whether the player should try a higher or lower number.

### 🎯 Correct Guess Detection

The program continuously compares the user's guesses with the target number and identifies when the correct number has been entered.

### 🔄 Multiple Attempts

The player can make multiple guesses until the correct number is found. This demonstrates the practical use of loops and repeated execution.

### 🧮 Attempt Tracking

The program can maintain a count of the number of guesses made by the player, providing additional information about the game.

### 💻 Simple Command-Line Interface

The application uses a straightforward command-line interface, making it easy to run and interact with the program without requiring additional software or graphical components.

<br>
<br>


## 🛠️ Technologies Used

### 🐍 Python

Python is used as the primary programming language for implementing the game logic, processing user input, and controlling the overall flow of the application.

### 🎲 Random Module

Python's built-in `random` module is used to generate the target number for the game.

### ⌨️ Command-Line Interface

The application uses the terminal or command prompt to receive user input and display game instructions, hints, and results.

<br>
<br>

## 🧠 Programming Concepts Used

This project provides practical experience with several fundamental Python concepts:

- Variables and data types
- User input
- Type conversion
- Conditional statements
- `if`, `elif,`, and `else`
- `while` loops
- Comparison operators
- Random number generation
- Counters
- Boolean conditions
- Program control flow
- Basic error handling
- Logical problem solving

These concepts are combined to create a complete program rather than being used as isolated coding examples.

<br>
<br>

## ⚙️ How the Game Works

The game follows a simple but structured process.

When the program starts, a random number is generated within the selected range. The program then asks the player to enter a guess. After receiving the input, the program compares the guess with the target number.

If the entered number is smaller than the target number, the application displays a message indicating that the player should try a higher number. If the entered number is larger, the application suggests trying a lower number.

The process continues through a loop, allowing the player to make additional attempts. Once the entered number matches the generated number, the program displays a success message and the game ends.

A simplified workflow is:

```text
                 ┌───────────────────┐
                 │       Start       │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Generate Random   │
                 │      Number       │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │   Ask for Guess   │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │ Compare Guess     │
                 │ with Target       │
                 └─────────┬─────────┘
                           ↓
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
          Too Low       Correct        Too High
             ↓             ↓             ↓
       Try Higher       Success      Try Lower
             ↓             ↓             ↓
             └─────────────┬─────────────┘
                           ↓
                    Continue Guessing
                           ↓
                     Correct Guess
                           ↓
                 ┌───────────────────┐
                 │  Display Result   │
                 └─────────┬─────────┘
                           ↓
                 ┌───────────────────┐
                 │       End         │
                 └───────────────────┘
```

<br>
<br>

## 🔄 Game Flow

The overall game flow can be summarized as follows:

```text
Generate Number
       ↓
Accept Guess
       ↓
Compare Guess
       ↓
Provide Hint
       ↓
Repeat
       ↓
Correct Guess
       ↓
Display Result
```

This simple flow demonstrates how decision-making and repetition are used together in an interactive program.

<br>
<br>

## 📂 Project Structure

```text
Number-Guessing/
│
├── guessing_game_csv.py
├── guessing_game_sqlite.py
└── README.md
```
<br>
<br>

## 📄 File Description

**`guessing_game_csv.py`**

The Python program that implements the Number Guessing Game using **CSV file storage**. It handles random number generation, user guesses, hints, attempt tracking, and stores game information in a CSV file.

**`guessing_game_sqlite.py`**

The Python program that implements the Number Guessing Game using an **SQLite database**. It manages game records and stores information such as guesses, attempts, and results using SQLite database operations.

**`README.md`**

The documentation file containing detailed information about the project, objectives, features, technologies, programming concepts, working process, project structure, learning outcomes, and usage instructions.
<br>
<br>

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
cd Number-Guessing
```

### Step 3: Run the Program

Execute the Python file using:

```bash
python number_guessing.py
```

The game will start in the terminal and display the instructions for entering guesses.

<br>
<br>

## 💻 Example Gameplay

```text
🎯 Number Guessing Game

Guess a number between 1 and 100: 40

🔼 Too low! Try a higher number.

Guess a number between 1 and 100: 75

🔽 Too high! Try a lower number.

Guess a number between 1 and 100: 62

🎉 Congratulations!
You guessed the correct number.

Number of attempts: 3
```

The exact messages and range may vary depending on the implementation of the Python program.

<br>
<br>

## 📚 Learning Outcomes

Developing this project provided practical experience in building an interactive Python application from basic programming concepts.

The project helped me understand how random values can be generated and how user input can be processed and compared against a target value. It also provided hands-on practice with conditional statements, loops, comparison operators, and counters.

Another important learning outcome was understanding how program flow can be controlled based on different conditions. Instead of executing instructions only once, the application repeatedly accepts input, evaluates the result, and provides feedback until a specific condition is satisfied.

Through this project, I also gained experience in designing a simple user interaction flow and converting a problem statement into a logical sequence of programming steps.

<br>
<br>

## 🔮 Future Enhancements

The current implementation focuses on the basic number guessing mechanism, but the project can be extended with additional features to make the game more engaging and challenging.

Possible improvements include:

- 🎚️ Multiple difficulty levels
- ❤️ Limited number of attempts
- ⏱️ Time-based challenges
- 🏆 Score calculation
- 🥇 High-score tracking
- 🔁 Play-again functionality
- 📊 Game statistics
- 👥 Two-player mode
- 🎨 Graphical User Interface
- 🌐 Web-based version
- 🔊 Sound effects
- 📈 Difficulty-based scoring system

These improvements could transform the basic command-line game into a more complete interactive gaming application.

<br>
<br>

## 🎓 Project Purpose

This project was developed as part of my **Python Mini Projects** collection to strengthen programming fundamentals through practical implementation.

The Number Guessing Game demonstrates how a relatively small problem can be converted into a complete working application by combining random number generation, user input, conditional logic, loops, and program control flow.

The project is primarily intended for **learning and educational purposes** and serves as a foundation for developing more advanced Python applications and interactive games.

<br>
<br>



</div>
