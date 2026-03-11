import sys

contacts = {
    "Asmaa": {
        "phone": "0594022621",
        "email": "asmaa.hassoneh04@gmail.com",
    },
    "Ali": {
        "phone": "0594000111",
        "email": "ali.g1994@outlook.com",
    },
    "Sara": {
        "phone": "0594000222",
        "email": "sara@gmail.com",
    },
}

phone_index = {info["phone"]: name for name, info in contacts.items()}


def search_by_name(name: str) -> dict | None:
    info = contacts.get(name)
    if info is None:
        return None

    return {
        "name": name,
        "phone": info["phone"],
        "email": info["email"],
    }


def search_by_phone(phone: str) -> dict | None:
    name = phone_index.get(phone)
    if name is None:
        return None

    info = contacts[name]
    return {
        "name": name,
        "phone": info["phone"],
        "email": info["email"],
    }


def add_contact(name: str, phone: str, email: str) -> None:
    if not name.strip():
        raise ValueError("Name cannot be empty")

    if not phone.strip():
        raise ValueError("Phone cannot be empty")

    if name in contacts:
        raise ValueError("A contact with this name already exists")

    if phone in phone_index:
        raise ValueError("A contact with this phone number already exists")

    contacts[name] = {
        "phone": phone,
        "email": email,
    }
    phone_index[phone] = name


def delete_contact(name: str) -> None:
    info = contacts.get(name)
    if info is None:
        raise ValueError("Contact not found")

    phone = info["phone"]
    del contacts[name]
    del phone_index[phone]


def print_contact(contact: dict) -> None:
    print("------ CONTACT ------")
    print(f"Name  : {contact['name']}")
    print(f"Phone : {contact['phone']}")
    print(f"Email : {contact['email']}")
    print("---------------------")


def print_all_contacts() -> None:
    if not contacts:
        print("No contacts found")
        return

    for name in sorted(contacts):
        contact = search_by_name(name)
        if contact is not None:
            print_contact(contact)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage:")
        print("python contact_book.py list")
        print("python contact_book.py search-name <name>")
        print("python contact_book.py search-phone <phone>")
        print("python contact_book.py add <name> <phone> <email>")
        print("python contact_book.py delete <name>")
        sys.exit(1)

    command = sys.argv[1]

    try:
        if command == "list":
            print_all_contacts()

        elif command == "search-name":
            if len(sys.argv) != 3:
                print("Usage: python contact_book.py search-name <name>")
                sys.exit(1)

            name = sys.argv[2]
            result = search_by_name(name)

            if result is None:
                print("Contact not found")
            else:
                print_contact(result)

        elif command == "search-phone":
            if len(sys.argv) != 3:
                print("Usage: python contact_book.py search-phone <phone>")
                sys.exit(1)

            phone = sys.argv[2]
            result = search_by_phone(phone)

            if result is None:
                print("Contact not found")
            else:
                print_contact(result)

        elif command == "add":
            if len(sys.argv) != 5:
                print("Usage: python contact_book.py add <name> <phone> <email>")
                sys.exit(1)

            name = sys.argv[2]
            phone = sys.argv[3]
            email = sys.argv[4]

            add_contact(name, phone, email)
            print("Contact added successfully")

        elif command == "delete":
            if len(sys.argv) != 3:
                print("Usage: python contact_book.py delete <name>")
                sys.exit(1)

            name = sys.argv[2]
            delete_contact(name)
            print("Contact deleted successfully")

        else:
            print("Invalid command")
            sys.exit(1)

    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
