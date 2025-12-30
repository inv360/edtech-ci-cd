def is_eligible(marks, test_completed):
    """
    Student is eligible if:
    - Test is completed
    - Marks >= 60
    """
    if test_completed and marks >= 60:
        return True
    return False

