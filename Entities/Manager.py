from Entities.User import User
from Database.Database import Database
from Entities.Turf import Turf
from Entities.Booking import Booking
from Entities.BillingException import BillingException


class Manager(User):
    """Manager class to add, modify and delete the manager details"""
    def check_rates(self):
        for turf in Turf.print_turfs():
            if(turf.manager_id == self.id):
                print(turf)

    def view_request(self):
        """To view request"""
        turf_list = []
        for turf in Turf.print_turfs():
            if(turf.manager_id == self.id):
                turf_list.append(turf.id)
        bookings = list(filter(lambda booking: booking.status ==
                        "PENDING" and booking.turf_id in turf_list, Booking.getAllBooking()))
        if(bookings == []):
            print("No requests pending to be viewed")
        else:
            for booking in bookings:
                print(booking)

    def confirm_booking(self):
        """To confirm booking"""
        bookings = list(filter(lambda booking: booking.status ==
                        "PENDING", Booking.getAllBooking()))
        booking_id = int(input("Enter booking Id: "))
        booking = list(
            filter(lambda booking: booking.id == booking_id, bookings))
        if(booking == []):
            print("Entered id doesn't exist.")
        else:
            option = int(input("Choose an option 1.Approve 2.Reject: "))
            booking[0].status = "APPROVED" if option == 1 else "REJECTED"
            Booking.save(booking[0])

    def generate_bill(self):
        """To generate Bill"""
        booking_id = int(input("Enter the booking id: "))
        try:
            bookings = list(
                filter(lambda x: x.id == booking_id, Booking.getAllBooking()))
            if(bookings == []):
                raise BillingException
            booking = bookings[0]
            user_map={}
            turf_map={}
            for user in User.get_all_users():
                user_map[user.id] = user
            for turf in Turf.print_turfs():
                turf_map[turf.id] = turf
            file = open("Data/Bill-Booking-{}.txt".format(booking.id), "w")
            file.write("=================================================\n")
            file.write("Billing Detail for Booking ID:{}\n".format(booking.id))
            file.write("=================================================\n")
            file.write("User ID:{}     User Name:{}\n".format(
                booking.userId, user_map[booking.userId].name))
            file.write("Turf ID:{}     Turf Name:{}\n".format(
                booking.turf_id, turf_map[booking.turf_id].name))
            file.write("Booking Status :{}\n".format(booking.status))
            file.write("Start Time:{} Duration:{}Hrs. Cost:Rs.{}/-\n".format(
                booking.duration, booking.start_time, booking.cost))
            file.write("=================================================")
            file.close()
        except BillingException:
            print("Billing Id not found.")

    def booking_history(self):
        self.booking_history()

    @staticmethod
    def print_managers():
        """To print manager details"""
        manager_list = Database().getAllManagers()
        managers = []
        for manager in manager_list:
            managers.append(Manager(manager[0], manager[1], None))
        return managers

    def print_menu(self):
        """Print menu for manager options"""
        option = 1
        while option != 6:
            print("\nMENU")
            print("1. Check rates")
            print("2. View requests")
            print("3. Confirm/Reject booking")
            print("4. Generate Bill")
            print("5. View booking history")
            print("6. Exit")
            option = int(input("Enter your choice: "))
            if(option == 1):
                self.check_rates()
            elif(option == 2):
                self.view_request()
            elif(option == 3):
                self.confirm_booking()
            elif(option == 4):
                self.generate_bill()
            elif(option == 5):
                self.booking_history()
