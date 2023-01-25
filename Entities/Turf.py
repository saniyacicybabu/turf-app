from Database.Database import Database


class Turf:

    def __init__(self, id, name, location, bookingRate=0, managerId=None):
        self.id = id
        self.name = name
        self.location = location
        self.bookingRate = bookingRate
        self.managerId = managerId

    def __str__(self):
        return "ID:{} Name:{} Location:{} BookingRate:{}".format(self.id, self.name, self.location, self.bookingRate)

    def addToDatabase(self):
        Database().addTurfToDataBase(self)

    @staticmethod
    def printTurfs():
        turfList = Database().getAllTurfs()
        turfs = []
        for turf in turfList:
            turfs.append(Turf(turf[0], turf[1], turf[2], turf[3], turf[4]))
        return turfs

    @staticmethod
    def save(turf):
        return Database().updateTurfToDataBase(turf)
