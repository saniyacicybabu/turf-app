from Entities.User import User


def printMenu():
    print("MENU")
    print("1. Add user")
    print("2. Exit")
    option = int(input("Enter your choice"))
    if(option == 1):
        addUser()


def addUser():
    name = input("Enter username")
    password = input("Enter password")
    user = User(0, name, password)
    user.addToDatabase()


if(__name__ == "__main__"):
    printMenu()
