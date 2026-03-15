def validate_students(students: list[dict]) -> None:
    if not isinstance(students, list):
        raise ValueError("Students must be provided as a list")

    for index, student in enumerate(students, start=1):

        if not isinstance(student, dict):
            raise ValueError(f"Student #{index} must be a dictionary")

        if not all(key in student for key in ("name", "grade")):
            raise ValueError(f"Student #{index} must have name and grade")

        name = student["name"]
        grade = student["grade"]

        if not isinstance(name, str) or not name.strip():
            raise ValueError(f"Student #{index} name must be a non-empty string")

        if not isinstance(grade, (int, float)):
            raise ValueError(f"Student #{index} grade must be a number")

        if not 0 <= grade <= 100:
            raise ValueError(f"Student #{index} grade must be between 0 and 100")


def get_top_3_students(students: list[dict]) -> list[dict]:
    validate_students(students)
    return sorted(students, key=lambda student: student["grade"], reverse=True)[:3]


def get_pass_fail_results(students: list[dict]) -> list[dict]:
    validate_students(students)
    return [
        {
            "name": student["name"],
            "grade": student["grade"],
            "status": "Pass" if student["grade"] >= 60 else "Fail",
        }
        for student in students
    ]
