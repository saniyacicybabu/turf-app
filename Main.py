from Entities.User import User
from Entities.Admin import Admin
from Entities.Manager import Manager


def print_menu():
    """Function to display the main menu of Turf"""""
    user_name = input("Enter user_name: ")
    password = input("Enter password: ")
    user = User(0, user_name, password)
    user = user.login()
    if(user is None):
        print("login failed. user not found")
    elif(user.user_type == "ADMIN"):
        print("admin logged in successully")
        Admin(user.id, user.name, user.password, user.user_type).print_menu()
    elif(user.user_type == "MANAGER"):
        print("manager logged in successfully")
        Manager(user.id, user.name, user.password, user.user_type).print_menu()
    elif(user.user_type == "NORMAL"):
        print("normal user logged in successfully")
        user.print_menu()
    else:
        print("login failed due to unknown error.")


if(__name__ == "__main__"):
    print_menu()
