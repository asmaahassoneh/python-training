import json

import pytest

from contacts.manager import (
    add_contact,
    delete_contact,
    list_contacts,
    load_contacts,
    search_by_name,
    search_by_phone,
)
from contacts.utils import WeakPasswordError, strong_password


@pytest.fixture
def temp_contacts_file(tmp_path):
    file_path = tmp_path / "contacts.json"
    sample_data = {
        "Asmaa": {
            "phone": "0594022621",
            "email": "asmaa.hassoneh04@gmail.com",
            "password": "StrongPass1!",
        },
        "Ali": {
            "phone": "0594000111",
            "email": "ali.g1994@outlook.com",
            "password": "AliPass123!",
        },
    }

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(sample_data, file, indent=4)

    return str(file_path)


def test_search_by_name_found(temp_contacts_file):
    result = search_by_name("Asmaa", temp_contacts_file)

    assert result == {
        "name": "Asmaa",
        "phone": "0594022621",
        "email": "asmaa.hassoneh04@gmail.com",
    }


def test_search_by_name_not_found(temp_contacts_file):
    assert search_by_name("Lina", temp_contacts_file) is None


def test_search_by_phone_found(temp_contacts_file):
    result = search_by_phone("0594000111", temp_contacts_file)

    assert result == {
        "name": "Ali",
        "phone": "0594000111",
        "email": "ali.g1994@outlook.com",
    }


def test_add_contact_success(temp_contacts_file):
    add_contact(
        name="Lina",
        phone="0594000333",
        email="lina@gmail.com",
        password="LinaPass9!",
        file_path=temp_contacts_file,
    )

    contacts = load_contacts(temp_contacts_file)

    assert "Lina" in contacts
    assert contacts["Lina"]["phone"] == "0594000333"


def test_delete_contact_success(temp_contacts_file):
    delete_contact("Ali", temp_contacts_file)

    contacts = load_contacts(temp_contacts_file)

    assert "Ali" not in contacts


def test_delete_contact_not_found(temp_contacts_file):
    with pytest.raises(ValueError):
        delete_contact("Lina", temp_contacts_file)


def test_duplicate_name_raises_error(temp_contacts_file):
    with pytest.raises(ValueError):
        add_contact(
            name="Asmaa",
            phone="0594555555",
            email="new@gmail.com",
            password="NewPass123!",
            file_path=temp_contacts_file,
        )


def test_duplicate_phone_raises_error(temp_contacts_file):
    with pytest.raises(ValueError):
        add_contact(
            name="NewUser",
            phone="0594022621",
            email="new@gmail.com",
            password="NewPass123!",
            file_path=temp_contacts_file,
        )


def test_duplicate_email_raises_error(temp_contacts_file):
    with pytest.raises(ValueError):
        add_contact(
            name="NewUser",
            phone="0594999999",
            email="asmaa.hassoneh04@gmail.com",
            password="NewPass123!",
            file_path=temp_contacts_file,
        )


def test_empty_name_raises_error(temp_contacts_file):
    with pytest.raises(ValueError):
        add_contact(
            name="",
            phone="0594000999",
            email="test@gmail.com",
            password="ValidPass1!",
            file_path=temp_contacts_file,
        )


def test_empty_phone_raises_error(temp_contacts_file):
    with pytest.raises(ValueError):
        add_contact(
            name="Lina",
            phone="",
            email="lina@gmail.com",
            password="ValidPass1!",
            file_path=temp_contacts_file,
        )


def test_empty_email_raises_error(temp_contacts_file):
    with pytest.raises(ValueError):
        add_contact(
            name="Lina",
            phone="0594000888",
            email="",
            password="ValidPass1!",
            file_path=temp_contacts_file,
        )


def test_weak_password_short():
    with pytest.raises(WeakPasswordError):
        strong_password("Ab1!")


def test_weak_password_no_uppercase():
    with pytest.raises(WeakPasswordError):
        strong_password("password1!")


def test_weak_password_no_lowercase():
    with pytest.raises(WeakPasswordError):
        strong_password("PASSWORD1!")


def test_weak_password_no_digit():
    with pytest.raises(WeakPasswordError):
        strong_password("Password!")


def test_weak_password_no_special_char():
    with pytest.raises(WeakPasswordError):
        strong_password("Password1")


def test_weak_password_with_spaces_edges():
    with pytest.raises(WeakPasswordError):
        strong_password(" Password1!")


def test_valid_password():
    assert strong_password("StrongPass1!") is True


def test_list_contacts_returns_sorted_names(temp_contacts_file):
    results = list_contacts(temp_contacts_file)

    assert [contact["name"] for contact in results] == ["Ali", "Asmaa"]
