from Entities.User import User
from Entities.Turf import Turf
from Entities.Manager import Manager
from Entities.Booking import Booking
from getpass import getpass

class Admin(User):
    """Admin Class to store and modify Admin details"""

    def set_manager(self):
        """Function to enter the details of Admin"""
        turfs = Turf.print_turfs()
        print("\n Available Turfs are:")
        for turf in turfs:
            print(turf)
        turf_id = int(input("Enter turf id to assign manager: "))
        try:
            turf = list(filter(lambda x: (x.id == turf_id), turfs))[0]
            print("\n Available Managers are:")
        except:
            print("Provided turf id doesnot exist")
            return
        managers = Manager.print_managers()
        for manager in managers:
            print(manager)
        manager_id = int(input("Enter new manager's id: "))
        try:
            manager = list(filter(lambda x: (x.id == manager_id), managers))[0]
        except:
            print("Provided manager id doesnot exist")
            return
        turf.manager_id = manager_id
        if(Turf.save(turf) > 0):
            print("Updated Successfully")
        else:
            print("Update failed")

    def set_price_list(self):
        """Function to set the price list of turf"""
        print("\n Available Turfs are:")
        turfs = Turf.print_turfs()
        for turf in turfs:
            print(turf)
        turf_id = int(input("Enter turf id to set price: "))
        try:
            turf = list(filter(lambda x: (x.id == turf_id), turfs))[0]
        except:
            print("Provided turf id doesnot exist")
            return
        turf.bookingRate = float((input("Enter new price: ")))
        if(Turf.save(turf) > 0):
            print("Updated Successfully")
        else:
            print("Update failed")

    def add_turf(self):
        """Function to add turf """
        name = input("Enter turf name: ")
        location = input("Enter turf location: ")
        turf = Turf(0, name, location)
        print("\n Turf details added successfully")
        turf.add_to_db()

    def view_bookings(self):
        """Function to view the booking history of turf"""
        print("\n Bookings done are:")
        self.booking_history()

    def add_user(self):
        """Function to add Manager and customer"""
        name = input("Enter user_name: ")
        password = getpass()
        user_type = input("Enter user type - 1.Manager 2.Normal: ")
        phone = int(input("Enter user phone number: "))
        email = input("Enter user email id: ")
        user = None
        if(user_type == "1"):
            user = User(0, name, password, "MANAGER", 1, phone, email)
            print("\n New Manager registered successfully")
        else:
            user = User(0, name, password, "NORMAL", 1, phone, email)
            print("\n New User registered successfully")
        user.add_to_db()

    def print_menu(self):
        """Function to print available menu for Admin"""
        option = 1
        while option != 6:
            print("\nMENU")
            print("1. Add user")
            print("2. Add turf")
            print("3. Assign manager")
            print("4. Set price")
            print("5. View bookings")
            print("6. Exit")
            option = int(input("Enter your choice: "))
            if(option == 1):
                self.add_user()
            elif(option == 2):
                self.add_turf()
            elif(option == 3):
                self.set_manager()
            elif(option == 4):
                self.set_price_list()
            elif(option == 5):
                self.view_bookings()
