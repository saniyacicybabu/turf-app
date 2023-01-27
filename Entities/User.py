from Database.Database import Database
from Entities.Turf import Turf
from Entities.Booking import Booking


class User:

    def __init__(self, id, name, password, userType="NORMAL"):
        self.id = id
        self.name = name
        self.password = password
        self.userType = userType

    def __str__(self):
        return "ID:{} Name:{}".format(self.id, self.name)

    def login(self):
        responseList = Database().login(self)
        if(responseList == []):
            return None
        userInfo = responseList[0]
        return User(userInfo[0], userInfo[1], userInfo[2], userInfo[3])

    def checkTurf(self):
        location = input("Enter location to search: ")
        turfs = list(filter(lambda x: x.location ==
                     location, Turf.printTurfs()))
        if(turfs == []):
            print("no turfs is specified location")
        else:
            for turf in turfs:
                print(turf)

    def checkTurfavailable(self, turfId, startTime):
        bookings = list(filter(lambda x: x.status ==
                        "APPROVED" and x.startTime[0:8] == startTime[0:8], Booking.getAllBooking()))
        currentBookingHours = []
        for booking in bookings:
            start = int(booking.startTime[9:11])
            for i in range(start, start+booking.duration):
                currentBookingHours.append(i)
        # TODO modify to include duration also
        return not int(startTime[9:11]) in currentBookingHours

    def checkAvailability(self):
        self.checkTurf()
        turfId = int(input("Enter turf Id: "))
        startTime = input("Enter date and time in DD-MM-YY HH format: ")
        if(self.checkTurfavailable(turfId, startTime)):
            print("Turf available at given time")
        else:
            print("Turf not available at given time")

    def bookTurf(self):
        turfId = int(input("Enter turf Id: "))
        startTime = input("Enter date and time in DD-MM-YY HH format: ")
        duration = input("Enter No. of hours turf is needed: ")
        if(self.checkTurfavailable(turfId, startTime)):
            # TODO create booking object and save to db
            booking = Booking(0, turfId, self.id, "PENDING",
                              startTime, duration, 0)
            Booking.save(booking)
        else:
            print("Turf not available at given time")

    def bookingHistory(self):
        userMap = {}
        turfMap = {}
        turfList = []
        for user in User.getAllUsers():
            userMap[user.id] = user
        for turf in Turf.printTurfs():
            turfMap[turf.id] = turf
            if(turf.managerId == self.id and self.userType == "MANAGER"):
                turfList.append(turf.id)
        bookings = Booking.getAllBooking()
        if(self.userType == "MANAGER"):
            bookings = list(
                filter(lambda booking: booking.turfId in turfList, bookings))
        elif(self.userType == "NORMAL"):
            bookings = list(
                filter(lambda booking: booking.userId == self.id, bookings))
        for booking in bookings:
            print("BookingId:{} User:{} Status:{} TurfName:{} StartTime:{} Duration:{}Hrs Cost:Rs.{}".format(
                booking.id, userMap[booking.userId].name, booking.status, turfMap[booking.turfId].name, booking.startTime, booking.duration, booking.cost))

    def addToDatabase(self):
        Database().addUserToDataBase(self)

    @staticmethod
    def getAllUsers():
        usersList = Database().getAllUsers()
        users = []
        for user in usersList:
            users.append(User(user[0], user[1], None))
        return users

    def printMenu(self):
        option = 1
        while option != 5:
            print("\nMENU")
            print("1. Check turf")
            print("2. Check availability")
            print("3. Book turf")
            print("4. View booking history")
            print("5. Exit")
            option = int(input("Enter your choice: "))
            if(option == 1):
                self.checkTurf()
            elif(option == 2):
                self.checkAvailability()
            elif(option == 3):
                self.bookTurf()
            elif(option == 4):
                self.bookingHistory()
