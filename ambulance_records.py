import os
import datetime

DATA_FILE = "ambulance_records.txt"

class AmbulanceModel:
    @staticmethod
    def generate_booking_id():
        if not os.path.exists(DATA_FILE):
            return 1
        else:
            with open(DATA_FILE, "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1]
                    return int(last_line.split(",")[0]) + 1
                else:
                    return 1

    @staticmethod
    def save_booking(name, contact, location):
        booking_id = AmbulanceModel.generate_booking_id()
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DATA_FILE, "a") as file:
            file.write(f"{booking_id},{name},{contact},{location},{current_datetime},Pending\n")
        return booking_id

    @staticmethod
    def get_records():
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as file:
            return [line.strip().split(",") for line in file]

    @staticmethod
    def cancel_booking(booking_id_to_cancel):
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()

        found = False
        with open(DATA_FILE, "w") as file:
            for line in lines:
                booking_id, _, _, _, _, _ = line.strip().split(",")
                if booking_id == booking_id_to_cancel:
                    print(f"Booking ID {booking_id} has been canceled.")
                    found = True
                else:
                    file.write(line)
        if not found:
            print(f"No booking found with ID {booking_id_to_cancel}.")
class AmbulanceModel:
    @staticmethod
    def generate_booking_id():
        if not os.path.exists(DATA_FILE):
            return 1
        else:
            with open(DATA_FILE, "r") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1]
                    return int(last_line.split(",")[0]) + 1
                else:
                    return 1

    @staticmethod
    def save_booking(name, contact, location):
        booking_id = AmbulanceModel.generate_booking_id()
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DATA_FILE, "a") as file:
            file.write(f"{booking_id},{name},{contact},{location},{current_datetime},Pending\n")
        return booking_id

    @staticmethod
    def get_records():
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as file:
            return [line.strip().split(",") for line in file]

    @staticmethod
    def cancel_booking(booking_id_to_cancel):
        with open(DATA_FILE, "r") as file:
            lines = file.readlines()

        found = False
        with open(DATA_FILE, "w") as file:
            for line in lines:
                booking_id, _, _, _, _, _ = line.strip().split(",")
                if booking_id == booking_id_to_cancel:
                    print(f"Booking ID {booking_id} has been canceled.")
                    found = True
                else:
                    file.write(line)
        if not found:
            print(f"No booking found with ID {booking_id_to_cancel}.")
