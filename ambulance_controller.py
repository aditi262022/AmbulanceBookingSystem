from ambulance_records import AmbulanceModel
from ambulance_view import AmbulanceView

class AmbulanceController:
    @staticmethod
    def book_ambulance():
        print("\nBook an Ambulance")
        name = AmbulanceView.get_input("Enter your name: ")
        contact = AmbulanceView.get_input("Enter your contact number: ")
        location = AmbulanceView.get_input("Enter your location: ")
        booking_id = AmbulanceModel.save_booking(name, contact, location)
        print(f"Ambulance booked with ID: {booking_id}")

    @staticmethod
    def view_records():
        records = AmbulanceModel.get_records()
        AmbulanceView.display_records(records)

    @staticmethod
    def search_records():
        search_term = AmbulanceView.get_input("Enter a name or booking ID to search: ")
        records = AmbulanceModel.get_records()
        found_records = [record for record in records if search_term in record[1] or search_term == record[0]]
        AmbulanceView.display_search_records(found_records)

    @staticmethod
    def cancel_booking():
        booking_id_to_cancel = AmbulanceView.get_input("Enter the ID of the booking to cancel: ")
        AmbulanceModel.cancel_booking(booking_id_to_cancel)

# Main program's loop
while True:
    AmbulanceView.display_menu()
    choice = AmbulanceView.get_input("Enter your choice: ")

    if choice == "1":
        AmbulanceController.book_ambulance()
    elif choice == "2":
        AmbulanceController.view_records()
    elif choice == "3":
        AmbulanceController.search_records()
    elif choice == "4":
        AmbulanceController.cancel_booking()
    elif choice == "5":
        # Emergency Contacts functionality goes here
        pass
    elif choice == "6":
        # Emergency Instructions functionality goes here
        pass
    elif choice == "7":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")