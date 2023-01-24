from Entities.User import User
from Entities.Turf import Turf
from Entities.Manager import Manager


class Admin(User):

    def setManager(self):
        turfs = Turf.printTurfs()
        for turf in turfs:
            print(turf)
        turfId = int(input("Enter turf id to assign manager: "))
        try:
            turf = list(filter(lambda x: (x.id == turfId), turfs))[0]
        except:
            print("Provided turf id doesnot exist")
            return
        managers = Manager.printManagers()
        for manager in managers:
            print(manager)
        managerId = int(input("Enter new manager's id: "))
        try:
            manager = list(filter(lambda x: (x.id == managerId), managers))[0]
        except:
            print("Provided manager id doesnot exist")
            return
        turf.managerId = managerId
        if(Turf.save(turf) > 0):
            print("Updated Successfully")
        else:
            print("Update failed")

    def setPriceList(self):
        turfs = Turf.printTurfs()
        for turf in turfs:
            print(turf)
        turfId = int(input("Enter turf id to assign manager: "))
        try:
            turf = list(filter(lambda x: (x.id == turfId), turfs))[0]
        except:
            print("Provided turf id doesnot exist")
            return
        turf.bookingRate = float((input("Enter new price: ")))
        if(Turf.save(turf) > 0):
            print("Updated Successfully")
        else:
            print("Update failed")

    def addTurf(self):
        name = input("Enter turf name: ")
        location = input("Enter turf location: ")
        turf = Turf(0, name, location)
        turf.addToDatabase()

    def viewBookings(self):
        pass

    def addUser(self):
        name = input("Enter username: ")
        password = input("Enter password: ")
        userType = input("Enter user type - 1.Manager 2.Normal: ")
        user = None
        if(userType == "1"):
            user = User(0, name, password, "MANAGER")
        else:
            user = User(0, name, password)
        user.addToDatabase()

    def printMenu(self):
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
                self.addUser()
            elif(option == 2):
                self.addTurf()
            elif(option == 3):
                self.setManager()
            elif(option == 4):
                self.setPriceList()
            elif(option == 5):
                self.viewBookings()
