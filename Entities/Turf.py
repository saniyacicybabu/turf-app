"""import statements"""
from Database.database import Database


class Turf:
    """Turf Class to store and modify the details of Turf"""

    def __init__(self, id, name, location, booking_rate=0, manager_id=None):
        self.id = id
        self.name = name
        self.location = location
        self.booking_rate = booking_rate
        self.manager_id = manager_id
        self.db = Database()

    def __str__(self):
        """doc"""
        rtestr = f"ID:{self.id} Name:{self.name} "
        return rtestr + f"Location:{self.location} booking_rate:{self.booking_rate}"

    def add_to_database(self):
        """Function to add details to database"""
        self.db.add_turf_to_database(self)

    @staticmethod
    def print_turfs():
        """Function to display all turf details"""
        turf_list = Database().get_all_turfs()
        turfs = []
        for turf in turf_list:
            turfs.append(Turf(turf[0], turf[1], turf[2], turf[3], turf[4]))
        return turfs

    @staticmethod
    def save(turf):
        """Function to update turf details in database"""
        return Database().update_turf_to_database(turf)
