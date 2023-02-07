from Database.Database import Database


class Booking:
    """Booking Class to store and modify the detils of turf booking """

    def __init__(self, id, turf_id, userId, status, start_time, duration, cost):
        """constructor to intialize the booking details"""
        self.id = id
        self.turf_id = turf_id
        self.userId = userId
        self.status = status
        self.start_time = start_time
        self.duration = duration
        self.cost = cost

    def __str__(self):
        return "Booking id:{} Turf Id:{} User id:{} Status:{} Start time:{} Duration:{} Hours Cost:Rs.{}".format(self.id, self.turf_id, self.userId, self.status, self.start_time, self.duration, self.cost)

    @staticmethod
    def get_all_booking():
        """Function to retreive all booking details of turf """
        response = Database().get_all_bookings()
        bookings = []
        for elem in response:
            bookings.append(Booking(elem[0], elem[1], elem[2],
                            elem[3], elem[4], elem[5], elem[6]))
        return bookings

    @staticmethod
    def save(booking):
        """Function to add the booking details of Turf"""
        Database().save_booking(booking)
