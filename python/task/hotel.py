
import json
import uuid
import datetime

booking = []


class Table:

    def __init__(self, table_id, table_size, table_time, table_duration):
        self.table_id = table_id
        self.table_size = table_size
        self.table_time = table_time
        self.table_duration = table_duration

    def table_book(self):

        duration = datetime.timedelta(hours=self.table_duration)

        end_time = self.table_time + duration

        data = {
            "table_id": self.table_id,
            "table_size": self.table_size,
            "table_time": self.table_time.strftime("%d-%m-%Y %I:%M:%S %p"),
            "table_duration": self.table_duration,
            "end_time": end_time.strftime("%d-%m-%Y %I:%M:%S %p")
        }

        try:
            with open("hotel_data.json", "r") as file:
                booking = json.load(file)

        except Exception:
            booking = []

        booking.append(data)

        with open("hotel_data.json", "w") as file:
            json.dump(booking, file, indent=4)

        print("-------------------")
        print("Booking successful!")
        print("-------------------")
        
        print("Table ID :", self.table_id)
        print("Table Size :", self.table_size)
        print("Start Time :", self.table_time.strftime("%d-%m-%Y %I:%M:%S %p"))
        print("Duration :", self.table_duration, "hours")
        print("End Time :", end_time.strftime("%d-%m-%Y %I:%M:%S %p"))

try:
    with open("available_table.json", "r") as file:
        available = json.load(file)

except Exception:
    available = {
        "vip_table": 3,
        "medium_table": 6,
        "short_table": 7
    }


class menu:

    def menu(self):

        while True:

            print("====================")
            print("--- Booking Menu ---")
            print("====================")
            print("--------------------")
            print("1. table booking")
            print("--------------------")
            print("2. exit")
            print("--------------------")

            option = input("Enter your choice : ")

            if option == "1":

                table_id = str(uuid.uuid4().int)[:3]

                table_size = input("Enter your Table size (vip || medium || short): ").lower()

                if table_size == "vip":
                    key = "vip_table"

                elif table_size == "medium":
                    key = "medium_table"

                elif table_size == "short":
                    key = "short_table"

                else:
                    print("------------")
                    print("Invalid size")
                    print("------------")
                    

                if available[key] <= 0:

                    print("---------------------------")
                    print("This Table is not available")
                    print("---------------------------")
                
                else:
                     available[key] -= 1
                    

                table_time = datetime.datetime.now()

                table_duration = int(input("Enter time duration (in hours): "))

                with open("available_table.json", "w") as file:
                    json.dump(available, file, indent=4)

                print("-----------------")
                print("data was change")
                print("-----------------")
                
                obj = Table(table_id,table_size,table_time,table_duration)
                obj.table_book()

            elif option == "2":
                print("-------------------")
                print("Thanks for visiting")
                print("-------------------")
                break

            else:
                print("===============")
                print("Invalid choice!")
                print("===============")


object = menu()
object.menu()

