import sqlite3
from Entities import User


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
        print(user.name)
        print(user.password)
        # conn.execute(query)
        conn.close()


if __name__ == "__main__":
    Database().initializeDatabase()
