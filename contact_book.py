import sys

from contacts.manager import (
    add_contact,
    delete_contact,
    list_contacts,
    search_by_name,
    search_by_phone,
)
from contacts.utils import WeakPasswordError


def print_contact(contact: dict) -> None:
    print("------ CONTACT ------")
    print(f"Name  : {contact['name']}")
    print(f"Phone : {contact['phone']}")
    print(f"Email : {contact['email']}")
    print("---------------------")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage:")
        print("python contact_book.py list")
        print("python contact_book.py search-name <name>")
        print("python contact_book.py search-phone <phone>")
        print("python contact_book.py add <name> <phone> <email> <password>")
        print("python contact_book.py delete <name>")
        sys.exit(1)

    command = sys.argv[1]

    try:
        if command == "list":
            contacts = list_contacts()
            if not contacts:
                print("No contacts found")
            else:
                for contact in contacts:
                    print_contact(contact)

        elif command == "search-name":
            if len(sys.argv) != 3:
                print("Usage: python contact_book.py search-name <name>")
                sys.exit(1)

            result = search_by_name(sys.argv[2])
            if result is None:
                print("Contact not found")
            else:
                print_contact(result)

        elif command == "search-phone":
            if len(sys.argv) != 3:
                print("Usage: python contact_book.py search-phone <phone>")
                sys.exit(1)

            result = search_by_phone(sys.argv[2])
            if result is None:
                print("Contact not found")
            else:
                print_contact(result)

        elif command == "add":
            if len(sys.argv) != 6:
                print(
                    "Usage: python contact_book.py add <name> <phone> <email> <password>"
                )
                sys.exit(1)

            add_contact(
                name=sys.argv[2],
                phone=sys.argv[3],
                email=sys.argv[4],
                password=sys.argv[5],
            )
            print("Contact added successfully")

        elif command == "delete":
            if len(sys.argv) != 3:
                print("Usage: python contact_book.py delete <name>")
                sys.exit(1)

            delete_contact(sys.argv[2])
            print("Contact deleted successfully")

        else:
            print("Invalid command")
            sys.exit(1)

    except WeakPasswordError as error:
        print(f"Weak password: {error}")
        sys.exit(1)
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
