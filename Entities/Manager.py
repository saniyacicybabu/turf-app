from Entities.User import User
from Database.Database import Database
from Entities.Turf import Turf
from Entities.Booking import Booking


class Manager(User):
    def checkRates(self):
        for turf in Turf.printTurfs():
            if(turf.managerId == self.id):
                print(turf)

    def viewRequest(self):
        turfList = []
        for turf in Turf.printTurfs():
            if(turf.managerId == self.id):
                turfList.append(turf.id)
        bookings = list(filter(lambda booking: booking.status ==
                        "PENDING" and booking.turfId in turfList, Booking.getAllBooking()))
        if(bookings == []):
            print("No requests pending to be viewed")
        else:
            for booking in bookings:
                print(booking)

    def confirmBooking(self):
        bookings = list(filter(lambda booking: booking.status ==
                        "PENDING", Booking.getAllBooking()))
        bookingId = int(input("Enter booking Id: "))
        booking = list(
            filter(lambda booking: booking.id == bookingId, bookings))
        if(booking == []):
            print("Entered id doesn't exist.")
        else:
            option = int(input("Choose an option 1.Approve 2.Reject: "))
            booking[0].status = "APPROVED" if option == 1 else "REJECTED"
            Booking.save(booking[0])

    def generateBill(self):
        pass

    def bookingsHistory(self):
        self.bookingHistory()

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
            print("3. Confirm/Reject booking")
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
