# Python Training

This repository contains exercises and experiments from my Python training.

## Exercise: Profile CLI Script

The script `profile.py` reads command-line arguments using `sys.argv` and prints a formatted profile card.

### Example

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

## Tools Used

* Python 3
* Virtual Environment (`venv`)
* flake8 for linting
* black for code formatting

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install required tools:

```bash
pip install flake8 black
```

Run linting and formatting:

```bash
flake8 profile.py
black profile.py
```
