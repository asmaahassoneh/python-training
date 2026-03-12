# Python Training

This repository contains exercises and experiments from my Python training.

---

# Exercise 1 – Profile CLI Script

The script `profile.py` reads command-line arguments using `sys.argv` and prints a formatted profile card.

## Example

Run the script from the terminal:

```bash
python profile.py Asmaa 22 ComputerEngineering Palestine
```

Example output:

```
----------- PROFILE CARD -----------
Name    : Asmaa
Age     : 22
Major   : ComputerEngineering
Country : Palestine
------------------------------------
```

---

# Exercise 2 – BMI Calculator

The file `bmi.py` contains a function that calculates Body Mass Index (BMI).

## BMI Formula

```
BMI = weight / (height ** 2)
```

Where:

* **height** is in meters
* **weight** is in kilograms

Example:

```python
from bmi import bmi_calculator

print(bmi_calculator(1.75, 70))
```

Output:

```
22.86
```

The function also validates inputs and raises an error if height or weight are invalid.

---

# Testing with Pytest

Unit tests are implemented using **pytest**.

Test files are located in the `tests/` directory.

Example test:

```python
from bmi import bmi_calculator

def test_bmi_normal():
    assert bmi_calculator(1.75, 70) == 22.86
```

## Run tests

```bash
python -m pytest 
```

Expected output:

```
4 passed
```

---
---

# Exercise 3 – Grades Processing

The file `grades.py` stores students and their grades and provides utilities to analyze them.

## Features

* Return the **top 3 students** based on their grades using `sorted` with `lambda`.
* Convert grades into **Pass/Fail results** using **list comprehensions**.
* Validate student data (name must exist and grade must be between 0 and 100).

A grade is considered **Pass if it is 60 or higher**, otherwise **Fail**.

## Example

```python
from grades import get_top_3_students, get_pass_fail_results

students = [
    {"name": "Asmaa", "grade": 88},
    {"name": "Ali", "grade": 95},
    {"name": "Lina", "grade": 72},
    {"name": "Omar", "grade": 99},
]

print(get_top_3_students(students))
```

Example output:

```
[
  {"name": "Omar", "grade": 99},
  {"name": "Ali", "grade": 95},
  {"name": "Asmaa", "grade": 88}
]
```

### Pass / Fail Results

```python
from grades import get_pass_fail_results

students = [
    {"name": "Asmaa", "grade": 88},
    {"name": "Ali", "grade": 45},
    {"name": "Lina", "grade": 60},
]

print(get_pass_fail_results(students))
```

Output:

```
[
  {"name": "Asmaa", "grade": 88, "status": "Pass"},
  {"name": "Ali", "grade": 45, "status": "Fail"},
  {"name": "Lina", "grade": 60, "status": "Pass"}
]
```

## Testing

Unit tests for this exercise are implemented with **pytest** in:

```
tests/test_grades.py
```

Run tests with:

```bash
python -m pytest 
```

Expected output:

```
tests/test_grades.py ..... 
8 passed

```
---
# Exercise 4 – Contact Book with JSON Storage and Modules

The contact book project was extended to store data permanently in a `contacts.json` file and reorganized into modules inside a `contacts/` package.

## Project Modules

- `contact_book.py` → command-line entry point
- `contacts/manager.py` → contact management logic
- `contacts/utils.py` → password validation and custom exceptions
- `contacts.json` → persistent contact storage

## Features

- Store contacts in `contacts.json`
- Search for contacts **by name**
- Search for contacts **by phone number**
- Add a new contact
- Delete a contact
- Display all contacts in the terminal
- Validate passwords using `strong_password(password: str)`
- Raise `WeakPasswordError` for invalid passwords
- Organize code using modules and packages

## Example JSON Structure

```json
{
    "Asmaa": {
        "phone": "0594022621",
        "email": "asmaa.hassoneh04@gmail.com",
        "password": "StrongPass1"
    },
    "Ali": {
        "phone": "0594000111",
        "email": "ali.g1994@outlook.com",
        "password": "AliPass123"
    }
}
```
---

## Run the Contact Book

List all contacts:
```bash
python contact_book.py list
```

Search by **name**:

```bash
python contact_book.py search-name Asmaa
```

Example output:

```
------ CONTACT ------
Name  : Asmaa
Phone : 0594022621
Email : asmaa.hassoneh04@gmail.com
---------------------
```

Search by **phone number**:

```bash
python contact_book.py search-phone 0594000111
```

Example output:

```
------ CONTACT ------
Name  : Ali
Phone : 0594000111
Email : ali.g1994@outlook.com
---------------------
```
Add a new contact:
```bash
python contact_book.py add Lina 0594000333 lina@gmail.com LinaPass9
```
Delete a contact:
```bash
python contact_book.py delete Ali
```
---
## Password Validation
The function `strong_password(password: str)` checks that the password:
- is at least 8 characters long
- contains at least one uppercase letter
- contains at least one lowercase letter
- contains at least one digit
- does not start or end with spaces

If the password is invalid, the program raises:
```python
WeakPasswordError
```
---
## Testing

Unit tests for this exercise are implemented in:

```
tests/test_contacts.py
```

Run tests with:

```bash
python -m pytest 
```

Expected output:

```
tests\test_contacts.py ...............
15 passed

```
---

## Time Complexity Discussion

Different operations in the contact book have different time complexities.

### Search by name → O(1)

Looking up a contact by name uses a dictionary key:

```python
contacts.get(name)
```

Dictionary lookups are **O(1) on average**, meaning the lookup time does not increase significantly as the number of contacts grows.

### Search by phone → O(1)

Searching by phone number requires iterating through all contacts until a matching phone number is found:
```python
for name, info in contacts.items():
    if info["phone"] == phone:
```
In the worst case, the program may need to check every contact.
If there are **n contacts**, the time complexity is **O(n)**.
### Add contact → O(n)
Adding a contact requires:

- loading the JSON file
- building the phone index
- validating duplicates
- saving the updated JSON file

So the full operation is effectively **O(n)**.

### Delete contact → O(n)
Deleting a contact also requires:

- loading contacts from JSON
- removing the entry
- saving the updated data

So it is also **O(n)** overall.


### List all contacts → O(n log n)
Listing contacts sorts the names first:
```python
sorted(contacts.items())
```
---

# Project Structure

```
python-training
│
├── profile.py
├── bmi.py
├── grades.py
├── contact_book.py
│
├── tests
│   ├── test_bmi_calculator.py
│   └── test_grades.py
│
├── .gitignore
└── README.md
```
---

# Tools Used

* Python 3
* Virtual Environment (`venv`)
* flake8 (linting)
* black (code formatting)
* pytest (unit testing)

---

# Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install required tools:

```bash
pip install flake8 black pytest
```

Run linting and formatting:

```bash
flake8 profile.py
black .
```

Run tests:

```bash
python -m pytest 
```
