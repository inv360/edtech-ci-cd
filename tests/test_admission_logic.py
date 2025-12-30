from app.eligibility import is_eligible
from app.grading import calculate_grade

def test_eligible_student():
    assert is_eligible(75, True) == True

def test_ineligible_due_to_marks():
    assert is_eligible(50, True) == False

def test_ineligible_due_to_test():
    assert is_eligible(80, False) == False

def test_grade_A():
    assert calculate_grade(90) == "A"

def test_grade_B():
    assert calculate_grade(75) == "B"

def test_grade_fail():
    assert calculate_grade(40) == "Fail"

