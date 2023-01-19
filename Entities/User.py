from Database.Database import Database


class User:

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    def CheckTurf(self):
        pass

    def CheckAvailability(self):
        pass

    def BookTurf(self):
        pass

    def BookingHistory(self):
        pass

    def addToDatabase(self):
        Database().addUserToDataBase(self)
