import sys


def main():
    if len(sys.argv) < 5:
        print("Usage: python profile.py <name> <age> <major> <country>")
        sys.exit(1)

    name = sys.argv[1]
    age = sys.argv[2]
    major = sys.argv[3]
    country = sys.argv[4]

    print("----------- PROFILE CARD -----------")
    print(f"Name    : {name}")
    print(f"Age     : {age}")
    print(f"Major   : {major}")
    print(f"Country : {country}")
    print("------------------------------------")


if __name__ == "__main__":
    main()
