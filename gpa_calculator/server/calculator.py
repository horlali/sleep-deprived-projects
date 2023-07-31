from typing import List

GRADE_POINTS = {"A": 4.0, "B+": 3.5, "B": 3.0, "C": 2.0, "D": 1.5, "F": 1.0}


class Course:
    def __init__(self, name: str, credit: int, is_elective: bool = False):
        self.name = name
        self.credit = credit
        self.is_elective = is_elective
        self.grade = None
        self.took_elective = False

    def set_grade(self, grade):
        self.grade = grade

    def get_grade_point(self):
        return GRADE_POINTS.get(self.grade, 0.0)


class GPACalculator:
    def __init__(self):
        self.courses: List[Course] = []

    def add_course(self, course: Course):
        self.courses.append(course)

    def calculate_gpa(self):
        total_credit_points = 0.0
        total_credits = 0

        for course in self.courses:
            if not course.is_elective or (
                course.is_elective and course.grade is not None and course.took_elective
            ):
                total_credit_points += course.get_grade_point() * course.credit
                total_credits += course.credit

        gpa = total_credit_points / total_credits

        return gpa
