def validate_students(students: list[dict]) -> None:
    if not isinstance(students, list):
        raise ValueError("Students must be provided as a list")

    for student in students:
        if not isinstance(student, dict):
            raise ValueError("Each student must be a dictionary")

        if "name" not in student or "grade" not in student:
            raise ValueError("Each student must have name and grade")

        if not isinstance(student["name"], str) or not student["name"].strip():
            raise ValueError("Student name must be a non-empty string")

        if not isinstance(student["grade"], (int, float)):
            raise ValueError("Grade must be a number")

        if student["grade"] < 0 or student["grade"] > 100:
            raise ValueError("Grade must be between 0 and 100")


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
