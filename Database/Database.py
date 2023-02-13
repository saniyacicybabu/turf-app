"""doc"""
import sqlite3


class Database:
    """doc"""

    def initialize_database(self):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        file = open("Database/DDL_Scripts.sql", mode="r", encoding="utf-8")
        queries = file.readlines()
        file.close()
        for query in queries:
            conn.execute(query)
        conn.close()

    def add_user_to_database(self, user):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        query = "INSERT INTO USER (NAME, PASSWORD, USER_TYPE, IS_ACTIVE, PHONE, EMAIL) VALUES "
        query = query + f"('{user.name}', '{user.password}', '{user.user_type}', 1, "
        query = query + f"{user.phone}, '{user.email}')"
        conn.execute(query)
        conn.commit()
        conn.close()

    def save_booking(self, booking):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        if booking.id == 0:
            query = "INSERT INTO BOOKING (TURF_ID, USER_ID, STATUS, START_TIME, DURATION, COST)"
            query = (
                query
                + f" VALUES({booking.turf_id},{booking.user_id},'{booking.status}',"
            )
            query = (
                query + f"'{booking.start_time}',{booking.duration},{booking.duration}*"
            )
            query = (
                query + f"(SELECT BOOKING_RATE FROM TURF WHERE ID={booking.turf_id}))"
            )
        else:
            query = (
                f"UPDATE BOOKING SET STATUS='{booking.status}' WHERE ID = {booking.id}"
            )
        conn.execute(query)
        conn.commit()
        conn.close()

    def add_turf_to_database(self, turf):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        query = f"INSERT INTO TURF (NAME, LOCATION, IS_ACTIVE) VALUES ('{turf.name}','{turf.location}',1)"
        conn.execute(query)
        conn.commit()
        conn.close()

    def get_all_turfs(self):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        cursor = conn.cursor()
        query = "SELECT * FROM TURF WHERE IS_ACTIVE=1"
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output

    def get_all_bookings(self):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        cursor = conn.cursor()
        query = "SELECT * FROM BOOKING"
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output

    def get_all_managers(self):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        cursor = conn.cursor()
        query = "SELECT * FROM USER WHERE USER_TYPE='MANAGER' AND IS_ACTIVE=1"
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output

    def update_turf_to_database(self, turf):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        cursor = conn.cursor()
        if turf.booking_rate is None:
            turf.booking_rate = "NULL"
        if turf.manager_id is None:
            turf.manager_id = "NULL"
        query = f"UPDATE TURF SET BOOKING_RATE={turf.booking_rate},MANAGER_ID={turf.manager_id} WHERE ID={turf.id}"
        cursor.execute(query)
        success = cursor.rowcount
        conn.commit()
        conn.close()
        return success

    def login(self, user):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM USER WHERE NAME='{user.name}' AND "
        query = query + f"PASSWORD='{user.password}' AND IS_ACTIVE=1"
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output

    def get_all_users(self):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        cursor = conn.cursor()
        query = "SELECT * FROM USER WHERE USER_TYPE='NORMAL'"
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output

    def add_card_to_db(self, card):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        query = f"INSERT INTO CARD_DETAIL (USER_ID, CARD_NUMBER, CVV) VALUES ({card.user_id},{card.card_number},{card.cvv})"
        conn.execute(query)
        conn.commit()
        conn.close()

    def fetch_all_cards(self):
        """doc"""
        conn = sqlite3.connect("Data/PlayGround_Booking_System.db")
        cursor = conn.cursor()
        query = "SELECT * FROM CARD_DETAIL"
        cursor.execute(query)
        output = cursor.fetchall()
        conn.commit()
        conn.close()
        return output


if __name__ == "__main__":
    Database().initialize_database()
