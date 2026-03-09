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
pytest
```

Expected output:

```
4 passed
```

---

# Project Structure

```
python-training
│
├── profile.py
├── bmi.py
├── tests
│   └── test_bmi_calculator.py
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
pytest
```
