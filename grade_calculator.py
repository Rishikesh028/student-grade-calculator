"""
Student Grade Calculator
CSE1021 - Problem Solving and Object-Oriented Programming

Takes marks for N students, works out each student's average and grade,
and tells you who the class topper is.
"""


def get_number(prompt, low, high):
    """Ask again and again until the user types a whole number in [low, high]."""
    while True:
        text = input(prompt).strip()
        if text.isdigit():
            number = int(text)
            if low <= number <= high:
                return number
        print(f"  That doesn't look right. Please enter a number from {low} to {high}.")


def calculate_average(marks):
    """marks is a dictionary like {"Maths": 90, "Physics": 80}."""
    total = 0
    for subject in marks:
        total += marks[subject]
    return total / len(marks)


def get_grade(average):
    """Turn an average into a letter grade."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def find_topper(results):
    """Go through everyone and return (name, average) of the highest scorer."""
    topper_name = None
    highest = -1
    for name in results:
        if results[name]["average"] > highest:
            highest = results[name]["average"]
            topper_name = name
    return topper_name, highest


def print_report(results, subjects):
    """Print a simple table with everyone's marks, average and grade."""
    line = "-" * (14 + 10 * len(subjects) + 20)

    print("\n" + line)
    header = f"{'Name':<14}"
    for subject in subjects:
        header += f"{subject:<10}"
    header += f"{'Average':<10}{'Grade':<10}"
    print(header)
    print(line)

    for name in results:
        row = f"{name:<14}"
        for subject in subjects:
            row += f"{results[name]['marks'][subject]:<10}"
        row += f"{results[name]['average']:<10.2f}{results[name]['grade']:<10}"
        print(row)

    print(line)


def main():
    print("=" * 45)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 45)

    n = get_number("How many students? (1-50): ", 1, 50)
    s = get_number("How many subjects? (1-8): ", 1, 8)

    subjects = []
    for i in range(s):
        subject = input(f"  Name of subject {i + 1}: ").strip()
        subjects.append(subject)

    # students looks like: {"Asha": {"Maths": 90, "Physics": 80}, ...}
    students = {}
    for i in range(n):
        print(f"\n--- Student {i + 1} ---")
        name = input("  Name: ").strip()

        # two students with the same name would overwrite each other
        while name in students or name == "":
            name = input("  Name is empty or already taken. Try another: ").strip()

        marks = {}
        for subject in subjects:
            marks[subject] = get_number(f"  Marks in {subject} (0-100): ", 0, 100)
        students[name] = marks

    # results looks like: {"Asha": {"marks": {...}, "average": 85.0, "grade": "A"}}
    results = {}
    for name in students:
        average = calculate_average(students[name])
        results[name] = {
            "marks": students[name],
            "average": average,
            "grade": get_grade(average),
        }

    print_report(results, subjects)

    topper, top_avg = find_topper(results)
    print(f"\nClass topper: {topper} (average {top_avg:.2f})")

    # extra: class average + how many students got each grade
    class_total = 0
    grade_count = {}
    for name in results:
        class_total += results[name]["average"]
        g = results[name]["grade"]
        grade_count[g] = grade_count.get(g, 0) + 1

    print(f"Class average: {class_total / n:.2f}")
    print("Grades:", grade_count)


if __name__ == "__main__":
    main()
