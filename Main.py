"""import statements"""
from getpass import getpass
from Entities.admin import Admin
from Entities.manager import Manager
from Entities.user import User


def print_menu():
    """Function to display the main menu of Turf""" ""
    username = input("Enter username: ")
    password = getpass()
    user = User(0, username, password)
    user = user.login()
    if user is None:
        print("login failed. user not found")
    elif user.user_type == "ADMIN":
        print("admin logged in successully")
        Admin(user.id, user.name, user.password, user.user_type).print_menu()
    elif user.user_type == "MANAGER":
        print("manager logged in successfully")
        Manager(user.id, user.name, user.password, user.user_type).print_menu()
    elif user.user_type == "NORMAL":
        print("normal user logged in successfully")
        user.print_menu()
    else:
        print("login failed due to unknown error.")


if __name__ == "__main__":
    OPTION = "1"
    while OPTION != "2":
        print("MENU")
        print("1. Login")
        print("2. Exit")
        OPTION = input("Enter your choice: ")
        if OPTION == "1":
            print_menu()
        elif OPTION != "2":
            print("Invalid Choice")
