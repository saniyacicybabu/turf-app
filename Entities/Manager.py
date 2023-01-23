from Entities.User import User
from Database.Database import Database
from Entities.Turf import Turf


class Manager(User):

    def checkRates(self):
        for turf in Turf.printTurfs():
            if(turf.managerId == self.id):
                print(turf)

    def viewRequest(self):
        pass

    def confirmBooking(self):
        pass

    def generateBill(self):
        pass

    def bookingsHistory(self):
        pass

    @staticmethod
    def printManagers():
        managerList = Database().getAllManagers()
        managers = []
        for manager in managerList:
            managers.append(Manager(manager[0], manager[1], None))
        return managers

    def printMenu(self):
        option = 1
        while option != 6:
            print("\nMENU")
            print("1. Check rates")
            print("2. View requests")
            print("3. Confirm booking")
            print("4. Generate Bill")
            print("5. View booking history")
            print("6. Exit")
            option = int(input("Enter your choice: "))
            if(option == 1):
                self.checkRates()
            elif(option == 2):
                self.viewRequest()
            elif(option == 3):
                self.confirmBooking()
            elif(option == 4):
                self.generateBill()
            elif(option == 5):
                self.bookingsHistory()
