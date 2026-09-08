
import json
import uuid
import datetime


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

        
        with open("python/task/hotel_data.json", "r") as file:
            booking = json.load(file)

        booking.append(data)

        with open("python/task/hotel_data.json", "w") as file:
            json.dump(booking, file, indent=4)

        print("-------------------")
        print("Booking successful!")
        print("-------------------")

        print("Table ID :", self.table_id)
        print("Table Size :", self.table_size)
        print("Start Time :",self.table_time.strftime("%d-%m-%Y %I:%M:%S %p"))
        print("Duration :", self.table_duration, "hours")
        print("End Time :",end_time.strftime("%d-%m-%Y %I:%M:%S %p"))

def time_count():

    with open("python/task/hotel_data.json", "r") as file:
        hotel = json.load(file)

    with open("python/task/available_table.json", "r") as file:
        table = json.load(file)

    now = datetime.datetime.now()

    remaining_booking = []

    for user in hotel:

        end_time = datetime.datetime.strptime(
            user["end_time"],
            "%d-%m-%Y %I:%M:%S %p"
        )

        if now >= end_time:

            if user["table_size"] == "vip":
                table["vip_table"] += 1

            elif user["table_size"] == "medium":
                table["medium_table"] += 1

            elif user["table_size"] == "short":
                table["short_table"] += 1

            print("--------------------")
            print("Table is available again")
            print("Table ID :", user["table_id"])
            print("--------------------")

        else:

            remaining_booking.append(user)

            print("--------------------")
            print("Time is not complete")
            print("--------------------")

    with open("python/task/hotel_data.json", "w") as file:
        json.dump(remaining_booking, file, indent=4)

    with open("python/task/available_table.json", "w") as file:
        json.dump(table, file, indent=4)
            


class Menu:

    def menu(self):

        while True:
            
            time_count()

            print("====================")
            print("--- Booking Menu ---")
            print("====================")
            print("--------------------")
            print("1. Table Booking")
            print("--------------------")
            print("2. Exit")
            print("--------------------")
            print("====================")

            option = input("Enter your choice : ")

            if option == "1":

                
                    with open("python/task/available_table.json", "r") as file:
                        available = json.load(file)

                
                    
                    table_id = str(uuid.uuid4().int)[:3]

                    table_size = input("Enter your Table size (vip || medium || short): ").lower()

                    if table_size == "vip":
                        key = "vip_table"

                    elif table_size == "medium":
                        key = "medium_table"

                    elif table_size == "short":
                        key = "short_table"

                    else:
                        print("----------------")
                        print("Invalid table size")
                        print("----------------")
                        continue

                    if available[key] <= 0:

                        print("---------------------------")
                        print("This Table is not available")
                        print("---------------------------")
                        continue

                    available[key] -= 1

                    try:
                        table_duration = int(input("Enter time duration (in hours): "))

                        if table_duration <= 0:
                            print("-------------------------------")
                            print("Duration must be greater than 0")
                            print("-------------------------------")

                            available[key] += 1
                            continue

                    except Exception:

                        print("---------------------------")
                        print("Please enter a valid number")
                        print("---------------------------")

                        available[key] += 1
                        continue

                    table_time = datetime.datetime.now()

                    with open("python/task/available_table.json", "w") as file:
                        json.dump(available, file, indent=4)

                    print("-----------------------")
                    print("Available table updated")
                    print("-----------------------")

                    obj = Table(table_id,table_size,table_time,table_duration)

                    obj.table_book()

            elif option == "2":

                print("-------------------")
                print("Thanks for visiting")
                print("-------------------")
                break

            else:

                print("----------------")
                print("Invalid choice!")
                print("----------------")


object = Menu()
object.menu()



