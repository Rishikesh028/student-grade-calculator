# Student Grade Calculator

A small Python program that takes marks for a class of students, works out everyone's average and letter grade, and tells you who the topper is. I made it for my CSE1021 (Problem Solving and Object-Oriented Programming) project.

## Overview

Teachers usually do this on paper or in a spreadsheet, and it's easy to slip up when you're adding up marks for a whole class. This program does the boring part for you. You type in the marks once, and it prints a clean report with grades, the class topper, the class average, and how many students got each grade.

Everything runs in the terminal, and there's nothing to install.

## Features

- Works for any number of students (1 to 50) and subjects (1 to 8)
- Stores each student's marks in a dictionary
- Works out each student's average and letter grade (A+, A, B, C, D or F)
- Finds the class topper
- Prints a neat table of all marks, averages and grades
- Shows the class average and a grade count (for example, how many A's, how many B's)
- Checks your input: marks must be whole numbers from 0 to 100, and duplicate or empty names are not allowed

## Technologies / Tools Used

- Python 3 (tested on 3.8 and above)
- No external libraries, only built-in Python
- Concepts used: dictionaries, loops, conditional statements, functions

## How to Install and Run

1. Make sure Python 3 is installed. You can check with:
   ```
   python --version
   ```
2. Download or clone this repository:
   ```
   git clone https://github.com/<your-username>/student-grade-calculator.git
   cd student-grade-calculator
   ```
3. Run the program:
   ```
   python grade_calculator.py
   ```
4. Answer the questions it asks: number of students, number of subjects, subject names, and then each student's name and marks.

(On some systems you may need to type `python3` instead of `python`.)

## How to Test

There's a small test file included. It checks the average calculation, the grade boundaries (like exactly 90 and 49.9), and the topper finder.

```
python test_grade_calculator.py
```

If everything is fine you'll see:

```
All tests passed!
```

You can also test it by hand. Try typing a mark like `105`, `-5` or `abc` and see whether the program asks you again. It should.

## Sample Output

Input: 3 students, 3 subjects (Maths, Physics, Chemistry)

```
----------------------------------------------------------------
Name          Maths     Physics   Chemistry Average   Grade
----------------------------------------------------------------
Asha          90        85        95        90.00     A+
Ravi          70        60        65        65.00     C
Meena         55        48        52        51.67     D
----------------------------------------------------------------

Class topper: Asha (average 90.00)
Class average: 68.89
Grades: {'A+': 1, 'C': 1, 'D': 1}
```

## Screenshots

Run the program on your own machine and save a screenshot of the terminal in the `screenshots/` folder, then link it here:

```
![Sample run](screenshots/sample_run.png)
```

## Project Structure

```
student-grade-calculator/
├── README.md                   <- you are here
├── statement.md                <- problem statement and scope
├── grade_calculator.py         <- the main program
├── test_grade_calculator.py    <- simple tests
└── screenshots/                <- terminal screenshots go here
```

## Grading Scale

| Average | Grade |
|---------|-------|
| 90 and above | A+ |
| 80 to 89.99 | A |
| 70 to 79.99 | B |
| 60 to 69.99 | C |
| 50 to 59.99 | D |
| Below 50 | F |

## Things I Might Add Later

- Save and load records using the `json` module
- A menu so you can add or search students after the first run
- A pass/fail check for each subject
