import pytest

from gpa_calculator.server.calculator import Course, GPACalculator


# Test Course class
def test_course_init():
    course = Course("Math", 3)
    assert course.name == "Math"
    assert course.credit == 3
    assert course.is_elective is False
    assert course.grade is None
    assert course.took_elective is False


def test_course_set_grade():
    course = Course("Science", 4)
    course.set_grade("A")
    assert course.grade == "A"


def test_course_get_grade_point():
    course = Course("History", 2)
    course.set_grade("B+")
    assert course.get_grade_point() == 3.5


# Test GPACalculator class
def test_gpa_calculator_init():
    calculator = GPACalculator()
    assert calculator.courses == []


def test_gpa_calculator_add_course():
    calculator = GPACalculator()
    course1 = Course("English", 3)
    course2 = Course("Art", 2, is_elective=True)

    calculator.add_course(course1)
    calculator.add_course(course2)

    assert len(calculator.courses) == 2
    assert calculator.courses[0] == course1
    assert calculator.courses[1] == course2


def test_gpa_calculator_calculate_gpa():
    calculator = GPACalculator()

    math_course = Course("Math", 4)
    math_course.set_grade("B+")

    science_course = Course("Science", 3, is_elective=True)
    science_course.set_grade("A")
    science_course.took_elective = True

    english_course = Course("English", 3)
    english_course.set_grade("C")

    calculator.add_course(math_course)
    calculator.add_course(science_course)
    calculator.add_course(english_course)

    assert calculator.calculate_gpa() == 3.2
