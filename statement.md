# Problem Statement

## The Problem

In most classes, marks are collected subject by subject, and then someone has to add them up, find the average, decide the grade and figure out who came first. Doing this by hand for even 30 students takes a while, and small mistakes are easy to make. Finding the topper means scanning the whole list again.

I wanted a simple program that takes the marks once and does all of this correctly and instantly.

## Official Project Description

Develop a program that stores the marks of N students across multiple subjects using a dictionary and calculates each student's average, letter grade and the class topper.

## Scope of the Project

**What it covers**

- Taking the number of students and subjects from the user
- Storing every student's subject-wise marks in a dictionary
- Calculating each student's average and assigning a letter grade
- Finding the class topper
- Showing a formatted report in the terminal
- Showing the class average and the grade distribution
- Validating input so wrong values don't crash the program

**What it doesn't cover (on purpose, to keep it beginner-friendly)**

- No graphical interface, it only runs in the terminal
- No saving to a file or database, so data is gone once the program closes
- No handling of ties for topper (the first student with the highest average is shown)
- No weighted subjects or credits (that would be the GPA Calculator project)

## Target Users

- Teachers or teaching assistants who want a quick way to grade a small class
- Students who want to check their own averages and grades
- Beginners who want a clear example of how dictionaries, loops, conditionals and functions work together in Python

## High-Level Features

1. **Marks entry** - subject names and marks are entered by the user, with validation (0 to 100 only)
2. **Average calculation** - done with a function that loops through a student's marks dictionary
3. **Grade assignment** - a function using an if/elif ladder on the average
4. **Topper detection** - a function that loops through all students and tracks the highest average
5. **Report table** - a formatted table showing all marks, averages and grades
6. **Class summary** - class average and a count of each grade

## Python Concepts Used

| Concept | Where it shows up |
|---------|-------------------|
| Dictionary | Storing marks, results and grade counts |
| Loops | Reading input, calculating averages, printing the table |
| Conditional statements | Grade ladder, input checks |
| Functions | `get_number`, `calculate_average`, `get_grade`, `find_topper`, `print_report` |
