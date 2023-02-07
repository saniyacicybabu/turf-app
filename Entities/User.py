from Database.Database import Database
from Entities.Turf import Turf
from Entities.Booking import Booking
from datetime import datetime


class User:
    """User class to store and modify the details of customers of Turf"""

    def __init__(self, id, name, password, user_type="NORMAL", isActive=1, phone=None, email=None):
        """Constructor to intialise user details"""
        self.id = id
        self.name = name
        self.password = password
        self.user_type = user_type
        self.isActive = isActive
        self.phone = phone
        self.email = email
        self.db = Database()

    def __str__(self):
        return "ID:{} Name:{}".format(self.id, self.name)

    def login(self):
        """Function to authenticate user credentials"""
        response_list = self.db.login(self)
        if(response_list == []):
            return None
        userInfo = response_list[0]
        return User(userInfo[0], userInfo[1], userInfo[2], userInfo[3])

    def check_turf(self):
        """Function to print available turf in specified location"""
        location = input("Enter location to search: ")
        turfs = list(filter(lambda x: x.location ==
                     location, Turf.print_turfs()))
        if(turfs == []):
            print("no turfs in specified location")
            return None
        else:
            for turf in turfs:
                print(turf)
            return True

    def check_turf_available(self, turf_id, start_time):
        """Function to check whether given turf is available at given time """
        bookings = list(filter(lambda x: x.status ==
                        "APPROVED" and x.start_time[0:8] == start_time[0:8], Booking.get_all_booking()))
        current_booking_hours = []
        for booking in bookings:
            start = int(booking.start_time[9:11])
            for i in range(start, start+booking.duration):
                current_booking_hours.append(i)
        # TODO modify to include duration also
        return not int(start_time[9:11]) in current_booking_hours

    def check_availibility(self):
        """Function prompt customer for turf id and time and use check_turf_available function to check whether turf is available at that time"""
        if (self.check_turf() == None):
            return
        turf_id = int(input("Enter turf Id: "))
        start_time = input("Enter date and time in DD-MM-YY HH format: ")
        user_date = datetime.strptime(start_time, '%d-%m-%y %H')
        if(user_date < datetime.now()):
            print("Invalid date. Entered date is in past")
        elif(self.check_turf_available(turf_id, start_time)):
            print("Turf available at given time")
        else:
            print("Turf not available at given time")

    def book_turf(self):
        """Function to book turf for customer """
        turf_id = int(input("Enter turf Id: "))
        start_time = input("Enter date and time in DD-MM-YY HH format: ")
        duration = input("Enter No. of hours turf is needed: ")
        if(self.check_turf_available(turf_id, start_time)):
            booking = Booking(0, turf_id, self.id, "PENDING",
                              start_time, duration, 0)
            Booking.save(booking)
        else:
            print("Turf not available at given time")

    def booking_history(self):
        """Function to view the booking history for customer"""
        user_map = {}
        turf_map = {}
        turf_list = []
        for user in User.get_all_users():
            user_map[user.id] = user
        for turf in Turf.print_turfs():
            turf_map[turf.id] = turf
            if(turf.manager_id == self.id and self.user_type == "MANAGER"):
                turf_list.append(turf.id)
        bookings = Booking.get_all_booking()
        if(self.user_type == "MANAGER"):
            bookings = list(
                filter(lambda booking: booking.turf_id in turf_list, bookings))
        elif(self.user_type == "NORMAL"):
            bookings = list(
                filter(lambda booking: booking.userId == self.id, bookings))
        for booking in bookings:
            print("booking_id:{} User:{} Status:{} TurfName:{} start_time:{} Duration:{}Hrs Cost:Rs.{}".format(
                booking.id, user_map[booking.userId].name, booking.status, turf_map[booking.turf_id].name, booking.start_time, booking.duration, booking.cost))

    def add_to_db(self):
        """Function to add customer details to database"""
        self.db.add_user_to_db(self)

    @staticmethod
    def get_all_users():
        """Function to get details of all customer"""
        users_list = Database().get_all_users()
        users = []
        for user in users_list:
            users.append(User(user[0], user[1], None))
        return users

    def print_menu(self):
        """Function to print menu for customer """
        option = 1
        while option != 5:
            print("\nMENU")
            print("1. Check turf")
            print("2. Check availability")
            print("3. Book turf")
            print("4. View booking history")
            print("5. Exit")
            option = int(input("Enter your choice: "))
            if(option == 1):
                self.check_turf()
            elif(option == 2):
                self.check_availibility()
            elif(option == 3):
                self.book_turf()
            elif(option == 4):
                self.booking_history()
