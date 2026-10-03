# 🎯 Number Guessing Game

### A Simple Python-Based Interactive Game

The **Number Guessing Game** is a simple Python mini project developed to practice fundamental programming concepts through an interactive game. The program generates a random number within a predefined range and asks the user to guess the number.

The player continues entering guesses until the correct number is identified. After every attempt, the program provides feedback indicating whether the entered number is higher or lower than the generated number. This makes the game interactive while also providing practical experience with conditions, loops, random number generation and user input.

---

## 📌 Project Overview

The Number Guessing Game is designed as a beginner-friendly Python application that demonstrates how basic programming concepts can be combined to create an interactive program.

When the game starts, the computer generates a random number. The user is then asked to enter a guess. The program compares the user's input with the generated number and provides an appropriate hint.

If the guess is lower than the generated number, the program informs the user to try a higher number. If the guess is higher, the program suggests trying a lower number. The process continues until the user successfully guesses the correct number.

The project provides a simple way to understand how programs can generate random values, accept user input, make decisions and repeatedly execute instructions until a particular condition is satisfied.

---

## 🎯 Objectives

The main objectives of this project are:

- To practice basic Python programming concepts.
- To understand random number generation.
- To accept and process user input.
- To use conditional statements for decision making.
- To understand loops and repeated execution.
- To provide meaningful feedback to the user.
- To improve logical thinking and problem-solving skills.
- To build a simple interactive Python application.

---

## ✨ Features

- 🎲 Generates a random number.
- ⌨️ Accepts guesses from the user.
- 🔼 Provides a hint when the guess is too low.
- 🔽 Provides a hint when the guess is too high.
- 🎯 Detects the correct guess.
- 🔄 Allows repeated attempts.
- 🧮 Can keep track of the number of attempts.
- 💻 Simple command-line interface.

---

## 🛠️ Technologies Used

- 🐍 **Python**
- 🎲 **Random Module**
- ⌨️ **Command-Line Interface**

---

## 🧠 Concepts Used

This project provides practical experience with:

- Variables
- Data types
- User input
- Conditional statements
- `if`, `elif` and `else`
- `while` loops
- Random number generation
- Comparison operators
- Counters
- Basic program logic

---

## ⚙️ How the Game Works

The game follows a simple sequence:

```text
Start
  ↓
Generate Random Number
  ↓
Ask User for a Guess
  ↓
Compare Guess with Number
  ↓
 ┌───────────────┐
 │               │
 ↓               ↓
Too Low       Too High
 │               │
 └───────┬───────┘
         ↓
    Try Again
         ↓
Correct Guess
         ↓
   Display Result
         ↓
        End
