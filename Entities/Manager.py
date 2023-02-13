"""import statements"""
from Database.database import Database
from Entities.billing_exception import BillingException
from Entities.booking import Booking
from Entities.turf import Turf
from Entities.user import User


class Manager(User):
    """Manager class to add, modify and delete the manager details"""

    def check_rates(self):
        """doc"""
        for turf in Turf.print_turfs():
            if turf.manager_id == self.id:
                print("Turf details are:")
                print(turf)

    def view_request(self):
        """To view request"""
        turf_list = []
        for turf in Turf.print_turfs():
            if turf.manager_id == self.id:
                turf_list.append(turf.id)
        bookings = list(
            filter(
                lambda booking: booking.status == "PENDING"
                and booking.turf_id in turf_list,
                Booking.get_all_booking(),
            )
        )
        if not bookings:
            print("No requests pending to be viewed")
        else:
            print("Pending requests are:")
            for booking in bookings:
                print(booking)

    def confirm_booking(self):
        """To confirm booking"""
        turf_list = []
        for turf in Turf.print_turfs():
            if turf.manager_id == self.id:
                turf_list.append(turf.id)
        bookings = list(
            filter(
                lambda booking: booking.status == "PENDING"
                and booking.turf_id in turf_list,
                Booking.get_all_booking(),
            )
        )
        if not bookings:
            print("No bookings left to approve/reject")
            return
        booking_id = int(input("Enter booking Id: "))
        booking = list(filter(lambda booking: booking.id == booking_id, bookings))
        if not booking:
            print("Entered id doesn't exist.")
        else:
            booking = booking[0]
            option = int(input("Choose an option 1.Approve 2.Reject: "))
            bookable = User.check_turf_available(
                booking.turf_id, booking.start_time, booking.duration
            )
            if option == 1 and not bookable:
                print("Turf already booked at provided time. cannot approve")
                return
            # booking.status = "APPROVED"
            if option == 1:
                booking.status = "APPROVED"
                print("Booking approved")

            else:
                "REJECTED"
                print("Booking Rejected")
                Booking.save(booking)

    def generate_bill(self):
        """To generate Bill"""
        booking_id = int(input("Enter the booking id: "))
        try:
            bookings = list(
                filter(lambda x: x.id == booking_id, Booking.get_all_booking())
            )
            if not bookings:
                raise BillingException
            booking = bookings[0]
            user_map = {}
            turf_map = {}
            for user in User.get_all_users():
                user_map[user.id] = user
            for turf in Turf.print_turfs():
                turf_map[turf.id] = turf
            file = open(
                f"Data/Bill-Booking-{booking.id}.txt", mode="w", encoding="utf-8"
            )
            file.write("=================================================\n")
            file.write(f"Billing Detail for Booking ID:{booking.id}\n")
            file.write("=================================================\n")
            file.write(
                f"User ID:{booking.user_id}     User Name:{user_map[booking.user_id].name}\n"
            )
            file.write(
                f"Turf ID:{booking.turf_id}     Turf Name:{turf_map[booking.turf_id].name}\n"
            )
            file.write(f"Booking Status :{booking.status}\n")
            file.write(
                f"Start Time:{booking.start_time} Duration:{booking.duration}Hrs. "
            )
            file.write(f"Cost:Rs.{booking.cost}/-\n")
            file.write("=================================================")
            file.close()
            print("Bill generated for Booking" + str(booking.id))
        except BillingException:
            print("Billing Id not found.")

    def bookings_history(self):
        """To view booking history"""
        print("Your Booking History is:")
        self.booking_history()

    @staticmethod
    def print_managers():
        """To print manager details"""
        manager_list = Database().get_all_managers()
        managers = []
        for manager in manager_list:
            managers.append(Manager(manager[0], manager[1], None))
        return managers

    def print_menu(self):
        """Print menu for manager options"""
        option = "1"
        while option != "6":
            print("\nMENU")
            print("1. Check rates")
            print("2. View requests")
            print("3. Confirm/Reject booking")
            print("4. Generate Bill")
            print("5. View booking history")
            print("6. Logout")
            option = input("Enter your choice: ")
            if option == "1":
                self.check_rates()
            elif option == "2":
                self.view_request()
            elif option == "3":
                self.confirm_booking()
            elif option == "4":
                self.generate_bill()
            elif option == "5":
                self.bookings_history()
            elif option != "6":
                print("Invalid Choice")
