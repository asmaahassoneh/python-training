import json
from pathlib import Path

from contacts.utils import strong_password

DEFAULT_CONTACTS = {
    "Asmaa": {
        "phone": "0594022621",
        "email": "asmaa.hassoneh04@gmail.com",
        "password": "StrongPass1",
    },
    "Ali": {
        "phone": "0594000111",
        "email": "ali.g1994@outlook.com",
        "password": "AliPass123",
    },
}


def build_phone_index(contacts: dict) -> dict:
    return {info["phone"]: name for name, info in contacts.items()}


def load_contacts(file_path: str = "contacts.json") -> dict:
    path = Path(file_path)

    if not path.exists():
        save_contacts(DEFAULT_CONTACTS, file_path)
        return DEFAULT_CONTACTS.copy()

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_contacts(contacts: dict, file_path: str = "contacts.json") -> None:
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def search_by_name(name: str, file_path: str = "contacts.json") -> dict | None:
    contacts = load_contacts(file_path)
    info = contacts.get(name)

    if info is None:
        return None

    return {
        "name": name,
        "phone": info["phone"],
        "email": info["email"],
    }


def search_by_phone(phone: str, file_path: str = "contacts.json") -> dict | None:
    contacts = load_contacts(file_path)
    phone_index = build_phone_index(contacts)

    name = phone_index.get(phone)
    if name is None:
        return None

    info = contacts[name]
    return {
        "name": name,
        "phone": info["phone"],
        "email": info["email"],
    }


def add_contact(
    name: str,
    phone: str,
    email: str,
    password: str,
    file_path: str = "contacts.json",
) -> None:
    if not name.strip():
        raise ValueError("Name cannot be empty")

    if not phone.strip():
        raise ValueError("Phone cannot be empty")

    if not email.strip():
        raise ValueError("Email cannot be empty")

    strong_password(password)

    contacts = load_contacts(file_path)

    if name in contacts:
        raise ValueError("A contact with this name already exists")

    for info in contacts.values():
        if info["phone"] == phone:
            raise ValueError("A contact with this phone number already exists")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "password": password,
    }

    save_contacts(contacts, file_path)


def delete_contact(name: str, file_path: str = "contacts.json") -> None:
    contacts = load_contacts(file_path)

    if name not in contacts:
        raise ValueError("Contact not found")

    del contacts[name]
    save_contacts(contacts, file_path)


def list_contacts(file_path: str = "contacts.json") -> list[dict]:
    contacts = load_contacts(file_path)

    return [
        {
            "name": name,
            "phone": info["phone"],
            "email": info["email"],
        }
        for name, info in sorted(contacts.items())
    ]
