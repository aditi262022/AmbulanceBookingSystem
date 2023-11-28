class AmbulanceView:
    @staticmethod
    def display_menu():
        print("\nAmbulance Booking System")
        print("1. Book an Ambulance")
        print("2. View Booking Records")
        print("3. Search Booking Records")
        print("4. Cancel Booking")
        print("5. Emergency Contacts")
        print("6. Emergency Instructions")
        print("7. Exit")

    @staticmethod
    def display_records(records):
        print("\nBooking Records:")
        if not records:
            print("No records found.")
            return
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Contact: {record[2]}, Location: {record[3]},"
                  f" DateTime: {record[4]}, Status: {record[5]}")

    @staticmethod
    def display_search_records(found_records):
        if found_records:
            print("Found Records:")
            for record in found_records:
                print(record)
        else:
            print("No matching records found.")

    @staticmethod
    def get_input(message):
        return input(message)