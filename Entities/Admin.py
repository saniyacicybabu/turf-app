"""import statements"""
from getpass import getpass
import re
from Entities.manager import Manager
from Entities.turf import Turf
from Entities.user import User
from Entities.turf_exception import TurfException


class Admin(User):
    """Admin Class to store and modify Admin details"""

    def set_manager(self):
        """Function to enter the details of Admin"""
        print("Turf locations are:")
        turfs = Turf.print_turfs()
        for turf in turfs:
            print(turf)
        turf_id = int(input("Enter turf id to assign manager: "))
        try:
            turf = list(filter(lambda x: (x.id == turf_id), turfs))
            if not turf:
                raise TurfException()
        except TurfException:
            print("Provided turf id doesnot exist")
            return
        turf = turf[0]
        managers = Manager.print_managers()
        for manager in managers:
            print(manager)
        manager_id = int(input("Enter new manager's id: "))
        try:
            manager = list(filter(lambda x: (x.id == manager_id), managers))
            if not manager:
                raise TurfException()
        except TurfException:
            print("Provided manager id doesnot exist")
            return
        turf.manager_id = manager_id
        if Turf.save(turf) > 0:
            print("Updated Successfully")
        else:
            print("Update failed")

    def set_price_list(self):
        """Function to set the price list of turf"""
        print("Turf details")
        turfs = Turf.print_turfs()
        for turf in turfs:
            print(turf)
        turf_id = int(input("Enter turf id to set price: "))
        try:
            turf = list(filter(lambda x: (x.id == turf_id), turfs))
            if not turf:
                raise TurfException()
        except TurfException:
            print("Provided turf id doesnot exist")
            return
        turf = turf[0]
        turf.booking_rate = float((input("Enter new price: ")))
        if Turf.save(turf) > 0:
            print("Updated Successfully")
        else:
            print("Update failed")

    def add_turf(self):
        """Function to add turf"""
        name = input("Enter turf name: ")
        location = input("Enter turf location: ")
        turf = Turf(0, name, location)
        turf.add_to_database()
        print("Turf added Successfully")

    def view_bookings(self):
        """Function to view the booking history of turf"""
        print("Your Booking History is:")
        self.booking_history()

    def add_user(self):
        """Function to add Manager and customer"""
        user_type = input("Enter user type - 1.Manager 2.Normal: ")
        while user_type not in ["1", "2"]:
            print("invalid input")
            user_type = input("Enter user type - 1.Manager 2.Normal: ")
        name = input("Enter username: ")
        password = ""
        password_not_confirmed = 1
        chars = set("!@#$%^&*()_+")
        while password_not_confirmed == 1:
            password = getpass()
            while len(password) < 8 or not any((c in chars) for c in password):
                print("criteria not met")
                print("Minimum 8 characters required")
                password = getpass()
            print("Re-enter to confirm password")
            password_confirm = getpass()
            if password == password_confirm:
                password_not_confirmed = 0
            else:
                print("re-entered password is incorrect. try again")
        regex = r"\b[0-9]{10}\b"
        phone = input("Enter user phone number: ")
        while not re.fullmatch(regex, phone):
            print("invalid phone number")
            phone = input("Enter user phone number: ")
        phone = int(phone)
        email = input("Enter user email id: ")
        regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
        while not re.fullmatch(regex, email):
            print("invalid email id")
            email = input("Enter user email id: ")
        user = None
        if user_type == "1":
            user_type = "MANAGER"

        else:
            user_type = "NORMAL"
        user = User(0, name, password, user_type, 1, phone, email)
        print("Added successfully")
        user.add_to_database()

    def print_menu(self):
        """Function to print available menu for Admin"""
        option = "1"
        while option != "6":
            print("\nMENU")
            print("1. Add user")
            print("2. Add turf")
            print("3. Assign manager")
            print("4. Set price")
            print("5. View bookings")
            print("6. Logout")
            option = input("Enter your choice: ")
            if option == "1":
                self.add_user()
            elif option == "2":
                self.add_turf()
            elif option == "3":
                self.set_manager()
            elif option == "4":
                self.set_price_list()
            elif option == "5":
                self.view_bookings()
            elif option != "6":
                print("Invalid Choice")
