"""
Quick tests for the grade calculator.
Run with:  python test_grade_calculator.py
No extra libraries needed - just plain assert statements.
"""

from grade_calculator import calculate_average, get_grade, find_topper


def test_average():
    assert calculate_average({"Maths": 90, "Physics": 80}) == 85
    assert calculate_average({"Maths": 100}) == 100
    assert calculate_average({"A": 0, "B": 0, "C": 0}) == 0


def test_grades():
    assert get_grade(95) == "A+"
    assert get_grade(90) == "A+"     # boundary
    assert get_grade(89.99) == "A"
    assert get_grade(75) == "B"
    assert get_grade(60) == "C"
    assert get_grade(50) == "D"
    assert get_grade(49.9) == "F"


def test_topper():
    results = {
        "Asha": {"average": 85.0},
        "Ravi": {"average": 65.0},
        "Meena": {"average": 91.5},
    }
    assert find_topper(results) == ("Meena", 91.5)


if __name__ == "__main__":
    test_average()
    test_grades()
    test_topper()
    print("All tests passed!")
