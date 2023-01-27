from Database.Database import Database


class Booking:

    def __init__(self, id, turfId, userId, status, startTime, duration, cost):
        self.id = id
        self.turfId = turfId
        self.userId = userId
        self.status = status
        self.startTime = startTime
        self.duration = duration
        self.cost = cost

    def __str__(self):
        return "Booking id:{} Turf Id:{} User id:{} Status:{} Start time:{} Duration:{} Hours Cost:Rs.{}".format(self.id, self.turfId, self.userId, self.status, self.startTime, self.duration, self.cost)

    @staticmethod
    def getAllBooking():
        response = Database().getAllBookings()
        bookings = []
        for elem in response:
            bookings.append(Booking(elem[0], elem[1], elem[2],
                            elem[3], elem[4], elem[5], elem[6]))
        return bookings

    @staticmethod
    def save(booking):
        Database().saveBooking(booking)
