"""import statements"""
import re
from datetime import datetime
from Database.database import Database
from Entities.booking import Booking
from Entities.turf import Turf
from Entities.card_details import Card


class User:
    """User class to store and modify the details of customers of Turf"""

    def __init__(
        self,
        id,
        name,
        password,
        user_type="NORMAL",
        is_active=1,
        phone=None,
        email=None,
    ):
        self.id = id
        self.name = name
        self.password = password
        self.user_type = user_type
        self.is_active = is_active
        self.phone = phone
        self.email = email
        self.db = Database()

    def __str__(self):
        return f"ID:{self.id} Name:{self.name}"

    def login(self):
        """Function to authenticate user credentials"""
        response_list = self.db.login(self)
        if response_list == []:
            return None
        user_info = response_list[0]
        return User(user_info[0], user_info[1], user_info[2], user_info[3])

    def check_turf(self):
        """Function to print available turf in specified location"""
        location = input("Enter location to search: ")
        turfs = list(filter(lambda x: x.location == location, Turf.print_turfs()))
        if not turfs:
            print("no turfs in specified location")
            return None
        print("Turf details are:")    
        for turf in turfs:
            print(turf)
        return turfs

    @staticmethod
    def check_turf_available(turf_id, start_time, duration):
        """Function to check whether given turf is available at given time"""
        bookings = list(
            filter(
                lambda x: x.status == "APPROVED"
                and x.start_time[0:8] == start_time[0:8]
                and x.turf_id == turf_id,
                Booking.get_all_booking(),
            )
        )
        current_booking_hours = []
        for booking in bookings:
            start = int(booking.start_time[9:11])
            for i in range(start, start + booking.duration):
                current_booking_hours.append(i)
        required_booking_hours = []
        for i in range(int(start_time[9:11]), int(start_time[9:11]) + duration):
            required_booking_hours.append(i)
        result = set(required_booking_hours).intersection(set(current_booking_hours))
        return len(result) == 0

    def check_availability(self):
        """Function prompt customer for turf id and time and use check_turf_available function to check whether turf is available at that time"""
        turfs = self.check_turf()
        if turfs is None:
            return
        turf_id = int(input("Enter turf Id: "))
        turfs = [turf for turf in turfs if turf.id == turf_id]
        if not turfs:
            print("Entered turf doesn't exist")
            return
        start_time = input("Enter date and time in DD-MM-YY HH format: ")
        regex = r"\b[0-3][0-9]-[0-1][0-9]-[0-9]{2} [0-2][0-9]\b"
        while not re.fullmatch(regex, start_time):
            start_time = input(
                "invalid input. Enter date and time in DD-MM-YY HH format: "
            )
        user_date = datetime.strptime(start_time, "%d-%m-%y %H")
        if user_date < datetime.now():
            print("Invalid date. Entered date is in past")
        else:
            duration = int(input("Enter duration in hours: "))
            if User.check_turf_available(turf_id, start_time, duration):
                print("Turf available at given time")
            else:
                print("Turf not available at given time")

    def book_turf(self):
        """Function to book turf for customer"""
        cards = [card for card in Card.fetch_all_cards() if card.user_id == self.id]
        if cards == []:
            print("No cards found for payment. Add atleast one card to book turf")
            return
        turf_id = int(input("Enter turf Id: "))
        start_time = input("Enter date and time in DD-MM-YY HH format: ")
        regex = r"\b[0-3][0-9]-[0-1][0-9]-[0-9]{2} [0-2][0-9]\b"
        while not re.fullmatch(regex, start_time):
            start_time = input(
                "invalid input Enter date and time in DD-MM-YY HH format: "
            )
        user_date = datetime.strptime(start_time, "%d-%m-%y %H")
        if user_date < datetime.now():
            print("Invalid date. Entered date is in past")
            return
        duration = int(input("Enter No. of hours turf is needed: "))
        if User.check_turf_available(turf_id, start_time, duration):
            card_sel = 1
            print("Card details are:")
            for card in cards:
                print(
                    "Card  ID:" + f"{card_sel} XXXXXXXXXXXX{str(card.card_number)[12:]}"
                )
                card_sel = card_sel + 1
            card_sel = int(input("Enter card id to do payment: "))
            while card_sel > len(cards):
                card_sel = int(input("wrong input. Enter card id: "))
            card = cards[card_sel - 1]
            cvv = int(input("Enter cvv: "))
            if cvv != card.cvv:
                print("invalid cvv")
                return
            booking = Booking(0, turf_id, self.id, "PENDING", start_time, duration, 0)
            Booking.save(booking)
            print("Turf booked successfully:")
        else:
            print("Turf not available at given time")

    def booking_history(self):
        """Function to view the booking history for customer"""
        user_map = {user.id: user for user in User.get_all_users()}
        turf_map = {turf.id: turf for turf in Turf.print_turfs()}
        turf_list = [
            turf.id
            for turf in Turf.print_turfs()
            if turf.manager_id == self.id and self.user_type == "MANAGER"
        ]
        bookings = Booking.get_all_booking()
        if self.user_type == "MANAGER":
            bookings = list(
                filter(lambda booking: booking.turf_id in turf_list, bookings)
            )
        elif self.user_type == "NORMAL":
            bookings = list(
                filter(lambda booking: booking.user_id == self.id, bookings)
            )
            print("Your Booking History is:")
        for booking in bookings:
            result = f"BookingId:{booking.id} User:{user_map[booking.user_id].name} "
            result = (
                result
                + f"Status:{booking.status} TurfName:{turf_map[booking.turf_id].name}"
            )
            result = result + f"start_time:{booking.start_time} "
            result = result + f"Duration:{booking.duration}Hrs Cost:Rs.{booking.cost}"
            print(result)

    def add_to_database(self):
        """Function to add customer details to database"""
        self.db.add_user_to_database(self)

    @staticmethod
    def get_all_users():
        """Function to get details of all customer"""
        users_list = Database().get_all_users()
        users = []
        for user in users_list:
            users.append(User(user[0], user[1], None))
        return users

    def view_cards(self):
        """function to view the card details"""
        cards = [card for card in Card.fetch_all_cards() if card.user_id == self.id]
        if cards == []:
            print("No cards to display")
            return
        for card in cards:
            print("Card details are:")
            print(card)

    def add_card_details(self):
        """function to add card details"""
        regex = r"\b[0-9]{16}\b"
        card_no = input("Enter card number: ")
        while not re.fullmatch(regex, card_no):
            print("invalid card number")
            card_no = input("Enter card number: ")
        card_no = int(card_no)
        cards = [card for card in Card.fetch_all_cards() if card.user_id == self.id]
        for card in cards:
            if card.card_number == card_no:
                print("card already added")
                return
        regex = r"\b[0-9]{3}\b"
        cvv = input("Enter CVV: ")
        while not re.fullmatch(regex, cvv):
            print("invalid CVV")
            cvv = input("Enter CVV: ")
        cvv = int(cvv)
        card = Card(0, self.id, card_no, cvv)
        self.db.add_card_to_db(card)
        print("Card added successfully")

    def cancel_booking(self):
        """function to cancel the the turf booking"""
        bookings = Booking.get_all_booking()
        bookings = list(filter(lambda booking: booking.user_id == self.id, bookings))
        bookings = list(filter(lambda booking: booking.status != "CANCELLED", bookings))
        bookings = list(filter(lambda booking: booking.status != "REJECTED", bookings))
        cancelable_bookings = []
        for booking in bookings:
            user_date = datetime.strptime(booking.start_time, "%d-%m-%y %H")
            if user_date >= datetime.now():
                cancelable_bookings.append(booking)
        if not cancelable_bookings:
            print("no bookings left to cancel")
            return
        print("Your Bookings are:")
        for booking in cancelable_bookings:
            print(booking)
        booking_id = int(input("Enter booking id to cancel booking: "))
        cancelable_bookings = [
            booking for booking in cancelable_bookings if booking.id == booking_id
        ]
        if not cancelable_bookings:
            print("Booking not found")
            return
        cancelable_bookings[0].status = "CANCELLED"
        Booking.save(cancelable_bookings[0])
        print("Turf cancelled successfully")

    def print_menu(self):
        """Function to print menu for customer"""
        option = "1"
        while option != "8":
            print("\nMENU")
            print("1. Check turf")
            print("2. Check availability")
            print("3. Add card details")
            print("4. View cards")
            print("5. Book turf")
            print("6. View booking history")
            print("7. Cancel booking")
            print("8. Logout")
            option = input("Enter your choice: ")
            if option == "1":
                self.check_turf()
            elif option == "2":
                self.check_availability()
            elif option == "3":
                self.add_card_details()
            elif option == "4":
                self.view_cards()
            elif option == "5":
                self.book_turf()
            elif option == "6":
                self.booking_history()
            elif option == "7":
                self.cancel_booking()
            elif option != "8":
                print("invalid choice")
