
import sqlite3


class Database:
    def initializeDatabase(self):
        conn = sqlite3.connect('Data/PlayGround_Booking_System.db')
        file = open("Database/DDL_Scripts.sql", "r")
        queries = file.readlines()
        file.close()
        for query in queries:
            conn.execute(query)
        conn.close()

    def addUserToDataBase(self, user):
        conn = sqlite3.connect('Data/PlayGround_Booking_System.db')
        query = "INSERT INTO USER (NAME, PASSWORD, USER_TYPE, IS_ACTIVE) VALUES ('{}','{}','{}',1)".format(
            user.name, user.password, user.userType)
        conn.execute(query)
        conn.commit()
        conn.close()

    def saveBooking(self, booking):
        conn = sqlite3.connect('Data/PlayGround_Booking_System.db')
        if(booking.id == 0):
            query = "INSERT INTO BOOKING (TURF_ID, USER_ID, STATUS, START_TIME, DURATION, COST) VALUES({},{},'{}','{}',{},{}*(SELECT BOOKING_RATE FROM TURF WHERE ID={}))".format(
                booking.turfId, booking.userId, booking.status, booking.startTime, booking.duration, booking.duration, booking.turfId)
        else:
            query = "UPDATE BOOKING SET STATUS='{}' WHERE ID = {}".format(
                booking.status, booking.id)
        conn.execute(query)
        conn.commit()
        conn.close()

    def addTurfToDataBase(self, turf):
        conn = sqlite3.connect('Data/PlayGround_Booking_System.db')
        query = "INSERT INTO TURF (NAME, LOCATION, IS_ACTIVE) VALUES ('{}','{}',1)".format(
            turf.name, turf.location, turf.bookingRate)
        conn.execute(query)
        conn.commit()
        conn.close()

    def getAllTurfs(self):
        conn = sqlite3.connect('Data/PlayGround_Booking_System.db')
        cursor = conn.cursor()
        query = "SELECT * FROM TURF WHERE IS_ACTIVE=1"
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output

    def getAllBookings(self):
        conn = sqlite3.connect('Data/PlayGround_Booking_System.db')
        cursor = conn.cursor()
        query = "SELECT * FROM BOOKING"
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output

    def getAllManagers(self):
        conn = sqlite3.connect('Data/PlayGround_Booking_System.db')
        cursor = conn.cursor()
        query = "SELECT * FROM USER WHERE USER_TYPE='MANAGER' AND IS_ACTIVE=1"
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output

    def updateTurfToDataBase(self, turf):
        conn = sqlite3.connect('Data/PlayGround_Booking_System.db')
        cursor = conn.cursor()
        query = "UPDATE TURF SET BOOKING_RATE={},MANAGER_ID={} WHERE ID={}".format(
            turf.bookingRate if turf.bookingRate != None else 'NULL', turf.managerId if turf.managerId != None else 'NULL', turf.id)
        cursor.execute(query)
        success = cursor.rowcount
        conn.commit()
        conn.close()
        return success

    def login(self, user):
        conn = sqlite3.connect('Data/PlayGround_Booking_System.db')
        cursor = conn.cursor()
        query = "SELECT * FROM USER WHERE NAME='{}' AND PASSWORD='{}' AND IS_ACTIVE=1".format(
            user.name, user.password)
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output

    def getAllUsers(self):
        conn = sqlite3.connect('Data/PlayGround_Booking_System.db')
        cursor = conn.cursor()
        query = "SELECT * FROM USER WHERE USER_TYPE='NORMAL'"
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output



if __name__ == "__main__":
    Database().initializeDatabase()
