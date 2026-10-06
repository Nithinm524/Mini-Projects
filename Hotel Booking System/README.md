# 🏨 Hotel Booking System

### A Python-Based Hotel Reservation and Booking Management Application

The **Hotel Booking System** is a Python-based mini project developed to demonstrate how a simple hotel reservation process can be converted into an interactive and structured software application. The system allows users to browse available rooms, enter guest information, make reservations, view booking details, search for existing bookings, update reservation information and cancel bookings when required.

Hotel reservation systems need to maintain important information such as guest details, room numbers, room types, booking dates, room availability and reservation status. Managing this information manually can become difficult as the number of guests and reservations increases. This project provides a simple computerized approach for organizing hotel booking information and performing common reservation operations through a menu-driven interface.

The application is designed around the fundamental concepts of **Create, Read, Update and Delete (CRUD)**. Users can create new bookings, view existing reservations, search for specific bookings, update reservation details and cancel bookings. These operations provide practical experience in designing applications that manage structured records.

The project can also be implemented using different storage mechanisms such as **CSV and SQLite**, similar to the other projects in this Python Mini Projects collection. The CSV approach demonstrates file-based data storage, while SQLite provides a structured relational database approach for maintaining reservation records.

The project focuses on applying Python programming concepts to a realistic problem. It combines user input, functions, conditional statements, loops, data validation, file handling, database operations and record management into one complete application.

This project was developed as part of my **Python Mini Projects** collection to strengthen programming fundamentals through practical implementation and to understand how real-world reservation systems can be designed using Python.

> ⚠️ **Educational Notice:** This project is intended for learning and demonstration purposes. It is not a production-ready hotel reservation platform.

---

<div align="center">

<img 
  src="hotel-booking.png"
  alt="Hotel Booking System Python Mini Project"
  width="100%"
>

</div>

---

## 📌 Project Overview

The Hotel Booking System is a menu-driven application designed to simplify basic hotel reservation management.

When the application starts, the user is presented with a menu containing different hotel management operations. Depending on the implementation, the user can view available rooms, make a booking, view reservations, search for a booking, update reservation details, cancel a booking and exit the application.

The booking process begins when a guest provides the required information. This may include the guest name, contact information, room type, check-in date, check-out date and other required details.

The system then processes the information and creates a reservation record. The booking record can be stored using a CSV file or an SQLite database depending on the implementation.

The system also helps prevent basic booking conflicts by maintaining information about room availability and reservation status.

Existing bookings can be retrieved whenever required. Users can search for a reservation using relevant information such as a booking ID, guest name or contact number.

If a guest needs to modify their reservation, the system can update the existing booking instead of creating a duplicate record. Similarly, cancelled reservations can be removed or marked as cancelled.

The project therefore demonstrates the complete lifecycle of a basic hotel reservation, from creating a booking to managing and cancelling it.

---

## 💡 Problem Statement

Hotels need to maintain information about rooms, guests and reservations. Managing these records manually can become difficult when the number of bookings increases.

A computerized hotel booking system can simplify the reservation process by maintaining guest information, room availability and booking records in a structured manner.

The objective of this project is to develop a Python-based Hotel Booking System that allows users to perform common hotel reservation operations through a simple interface.

The system should provide functionality for:

- Viewing available rooms.
- Making new reservations.
- Recording guest information.
- Storing booking details.
- Viewing existing reservations.
- Searching for bookings.
- Updating reservation information.
- Cancelling bookings.
- Maintaining room availability.
- Storing reservation records.
- Validating user input.
- Managing records efficiently.

The project demonstrates how Python can be used to develop a practical record-management application based on a real-world hotel reservation scenario.

---

## 🎯 Objectives

The main objective of this project is to develop a simple and interactive hotel reservation management application using Python.

The specific objectives are:

- To create a computerized hotel booking system.
- To display available hotel rooms.
- To allow guests to make reservations.
- To collect and store guest information.
- To assign rooms to reservations.
- To maintain booking records.
- To search for existing reservations.
- To update booking information.
- To cancel reservations.
- To maintain room availability.
- To implement CRUD operations.
- To practice file-based data storage.
- To understand database-based reservation management.
- To implement input validation.
- To improve Python programming and problem-solving skills.

---

## ✨ Features

### 🏨 Room Availability

The system can display the rooms that are currently available for booking.

Room information may include:

```text
Room Number
Room Type
Price
Availability
