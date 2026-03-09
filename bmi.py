def bmi_calculator(height: float, weight: float) -> float:
    if height <= 0 or weight <= 0:
        raise ValueError("Height and weight must be positive numbers")

    bmi = weight / (height**2)
    return round(bmi, 2)
