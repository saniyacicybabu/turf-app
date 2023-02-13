"""import statements"""
from Database.database import Database


class Booking:
    """Booking Class to store and modify the detils of turf booking"""

    def __init__(self, id, turf_id, user_id, status, start_time, duration, cost):
        self.id = id
        self.turf_id = turf_id
        self.user_id = user_id
        self.status = status
        self.start_time = start_time
        self.duration = duration
        self.cost = cost

    def __str__(self):
        result = f"Booking id:{self.id} Turf Id:{self.turf_id} User id:{self.user_id} "
        result = f"{result} Status:{self.status} Start time:{self.start_time} "
        return result + f"Duration:{self.duration} Hours Cost:Rs.{self.cost}"

    @staticmethod
    def get_all_booking():
        """Function to retreive all booking details of turf"""
        response = Database().get_all_bookings()
        bookings = []
        for elem in response:
            bookings.append(
                Booking(elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6])
            )
        return bookings

    @staticmethod
    def save(booking):
        """Function to add the booking details of Turf"""
        Database().save_booking(booking)
