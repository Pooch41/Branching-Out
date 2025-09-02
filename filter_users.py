import json
import sys


def load_users() -> list:
    with open("users.json", "r") as file:
        return json.load(file)


def filter_users_by_name(name: str) -> None:
    users = load_users()

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    if len(filtered_users) == 0:
        print(f"No users with name '{name}' found.")
    for user in filtered_users:
        print(user)


def filter_users_by_age(age_to_filter) -> None:
    users = load_users()

    filtered_users = [user for user in users if user["age"] >= age_to_filter]

    if len(filtered_users) == 0:
        print(f"No users {age_to_filter} years old or older found.")
    for user in filtered_users:
        print(user)


def quit_cli(argument_num: int) -> None:
    print("Exiting, bye!")
    sys.exit(argument_num)


if __name__ == "__main__":

    DISPATCH_MAP = {
        "name": filter_users_by_name,
        "age": filter_users_by_age,
        "quit": quit_cli
    }

    while True:

        filter_variable = ""
        filter_option = input("What would you like to filter by? "
                              "('name', 'age', 'quit' to quit): ").strip().lower()
        if filter_option in DISPATCH_MAP:
            if filter_option == "name":

                while True:
                    try:
                        filter_variable = input("Enter a name to filter users: ").strip()
                        if len(filter_variable) < 1:
                            raise ValueError
                        break
                    except ValueError:
                        print("Please enter a name.")

            elif filter_option == "age":

                while True:
                    try:
                        filter_variable = int(input("Enter lowest age to filter from (inclusive): "))
                        if filter_variable < 0:
                            raise ValueError
                        break
                    except ValueError:
                        print("Please enter valid age (Full numbers, 0 or above)")

            elif filter_option == "quit":
                filter_variable = 0

            DISPATCH_MAP[filter_option](filter_variable)
        else:
            print("Please enter valid option")
