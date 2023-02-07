from Database.Database import Database


class Turf:
    """Turf Class to store and modify the details of Turf"""
    def __init__(self, id, name, location, bookingRate=0, manager_id=None):
        """Constructor intialise the turf details"""
        self.id = id
        self.name = name
        self.location = location
        self.bookingRate = bookingRate
        self.manager_id = manager_id
        self.db= Database()

    def __str__(self):
        return "ID:{} Name:{} Location:{} BookingRate:{}".format(self.id, self.name, self.location, self.bookingRate)

    def add_to_db(self):
        """Function to add details to database"""
        self.db.add_turf_to_db(self)

    @staticmethod
    def print_turfs():
        """Function to display all turf details """
        turf_list = Database().get_all_turfs()
        turfs = []
        for turf in turf_list:
            turfs.append(Turf(turf[0], turf[1], turf[2], turf[3], turf[4]))
        return turfs

    @staticmethod
    def save(turf):
        """Function to update turf details in database """
        return Database().update_turf_to_db(turf)
