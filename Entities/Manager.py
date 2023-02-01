from Entities.User import User
from Database.Database import Database
from Entities.Turf import Turf
from Entities.Booking import Booking
from Entities.BillingException import BillingException


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
        bookingId = int(input("Enter the booking id: "))
        try:
            bookings = list(
                filter(lambda x: x.id == bookingId, Booking.getAllBooking()))
            if(bookings == []):
                raise BillingException
            booking = bookings[0]
            userMap={}
            turfMap={}
            for user in User.getAllUsers():
                userMap[user.id] = user
            for turf in Turf.printTurfs():
                turfMap[turf.id] = turf
            file = open("Data/Bill-Booking-{}.txt".format(booking.id), "w")
            file.write("=================================================\n")
            file.write("Billing Detail for Booking ID:{}\n".format(booking.id))
            file.write("=================================================\n")
            file.write("User ID:{}     User Name:{}\n".format(
                booking.userId, userMap[booking.userId].name))
            file.write("Turf ID:{}     Turf Name:{}\n".format(
                booking.turfId, turfMap[booking.turfId].name))
            file.write("Booking Status :{}\n".format(booking.status))
            file.write("Start Time:{} Duration:{}Hrs. Cost:Rs.{}/-\n".format(
                booking.duration, booking.startTime, booking.cost))
            file.write("=================================================")
            file.close()
        except BillingException:
            print("Billing Id not found.")

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
