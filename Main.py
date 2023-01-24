from Entities.User import User
from Entities.Admin import Admin
from Entities.Manager import Manager


def printMenu():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = User(0, username, password)
    user = user.login()
    if(user is None):
        print("login failed. user not found")
    elif(user.userType == "ADMIN"):
        print("admin logged in successully")
        Admin(user.id, user.name, user.password, user.userType).printMenu()
    elif(user.userType == "MANAGER"):
        print("manager logged in successfully")
        Manager(user.id, user.name, user.password, user.userType).printMenu()
    elif(user.userType == "NORMAL"):
        print("normal user logged in successfully")
        user.printMenu()
    else:
        print("login failed due to unknown error.")


if(__name__ == "__main__"):
    printMenu()
