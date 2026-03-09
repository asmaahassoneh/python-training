import pytest
from grades import get_pass_fail_results, get_top_3_students


def test_get_top_3_students_returns_highest_grades():
    students = [
        {"name": "Asmaa", "grade": 88},
        {"name": "Ali", "grade": 95},
        {"name": "Lina", "grade": 72},
        {"name": "Omar", "grade": 99},
        {"name": "Sara", "grade": 81},
    ]

    result = get_top_3_students(students)

    assert result == [
        {"name": "Omar", "grade": 99},
        {"name": "Ali", "grade": 95},
        {"name": "Asmaa", "grade": 88},
    ]


def test_get_top_3_students_with_less_than_3_students():
    students = [
        {"name": "Asmaa", "grade": 88},
        {"name": "Ali", "grade": 95},
    ]

    result = get_top_3_students(students)

    assert result == [
        {"name": "Ali", "grade": 95},
        {"name": "Asmaa", "grade": 88},
    ]


def test_get_pass_fail_results():
    students = [
        {"name": "Asmaa", "grade": 88},
        {"name": "Ali", "grade": 45},
        {"name": "Lina", "grade": 60},
    ]

    result = get_pass_fail_results(students)

    assert result == [
        {"name": "Asmaa", "grade": 88, "status": "Pass"},
        {"name": "Ali", "grade": 45, "status": "Fail"},
        {"name": "Lina", "grade": 60, "status": "Pass"},
    ]


def test_invalid_grade_above_100():
    students = [{"name": "Asmaa", "grade": 105}]

    with pytest.raises(ValueError):
        get_top_3_students(students)


def test_invalid_grade_below_0():
    students = [{"name": "Ali", "grade": -10}]

    with pytest.raises(ValueError):
        get_pass_fail_results(students)


def test_missing_name_or_grade():
    students = [{"name": "Asmaa"}]

    with pytest.raises(ValueError):
        get_top_3_students(students)


def test_empty_name():
    students = [{"name": "", "grade": 70}]

    with pytest.raises(ValueError):
        get_pass_fail_results(students)


def test_grade_must_be_number():
    students = [{"name": "Sara", "grade": "A"}]

    with pytest.raises(ValueError):
        get_top_3_students(students)
