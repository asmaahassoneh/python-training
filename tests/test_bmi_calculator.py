import pytest
from bmi import bmi_calculator


def test_bmi_normal():
    assert bmi_calculator(1.75, 70) == 22.86


def test_bmi_overweight():
    assert bmi_calculator(1.80, 90) == 27.78


def test_invalid_height():
    with pytest.raises(ValueError):
        bmi_calculator(0, 70)


def test_invalid_weight():
    with pytest.raises(ValueError):
        bmi_calculator(1.75, -5)
