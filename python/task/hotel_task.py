
import json
import uuid
import datetime


class Table:

    def __init__(self, table_id, table_size, table_time, table_duration, user):
        self.table_id = table_id
        self.table_size = table_size
        self.table_time = table_time
        self.table_duration = table_duration
        self.user = user

    def table_book(self):

        duration = datetime.timedelta(hours=self.table_duration)
        end_time = self.table_time + duration

        data = {
            "table_id": self.table_id,
            "table_size": self.table_size,
            "table_time": self.table_time.strftime("%d-%m-%Y %I:%M:%S %p"),
            "table_duration": self.table_duration,
            "end_time": end_time.strftime("%d-%m-%Y %I:%M:%S %p"),
            "customer_no": self.user
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
        print("Start Time :", self.table_time.strftime("%d-%m-%Y %I:%M:%S %p"))
        print("Duration :", self.table_duration, "hours")
        print("End Time :", end_time.strftime("%d-%m-%Y %I:%M:%S %p"))
        print("customer :", self.user)


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

                user = int(input("Enter customer number : "))

                if user <= 0:

                    print("---------------------------")
                    print("Invalid customer number")
                    print("---------------------------")
                    continue

                if user > 8:

                    print("---------------------------")
                    print("Maximum 8 customers allowed")
                    print("---------------------------")
                    continue

                table_size = input("Enter table size (vip || medium || short): ").lower()

                if table_size == "vip":
                    capacity = 8

                elif table_size == "medium":
                    capacity = 4

                elif table_size == "short":
                    capacity = 2

                else:

                    print("---------------------------")
                    print("Invalid table size")
                    print("---------------------------")
                    continue

                tables = []

                if user <= capacity:

                    key = table_size + "_table"

                    if available[key] > 0:
                        tables.append(table_size)

                if len(tables) == 0:

                    if user <= 2:

                        if available["short_table"] > 0:
                            tables.append("short")

                        elif available["medium_table"] > 0:
                            tables.append("medium")

                        elif available["vip_table"] > 0:
                            tables.append("vip")

                    elif user <= 4:

                        if available["medium_table"] > 0:
                            tables.append("medium")

                        elif available["short_table"] >= 2:
                            tables.append("short")
                            tables.append("short")

                        elif available["vip_table"] > 0:
                            tables.append("vip")

                    elif user <= 6:

                        if available["medium_table"] >= 2:
                            tables.append("medium")
                            tables.append("medium")

                        elif available["medium_table"] >= 1 and available["short_table"] >= 1:
                            tables.append("medium")
                            tables.append("short")

                        elif available["short_table"] >= 3:
                            tables.append("short")
                            tables.append("short")
                            tables.append("short")

                        elif available["vip_table"] > 0:
                            tables.append("vip")

                    elif user <= 8:

                        if available["vip_table"] > 0:
                            tables.append("vip")

                        elif available["medium_table"] >= 2:
                            tables.append("medium")
                            tables.append("medium")

                        elif available["medium_table"] >= 1 and available["short_table"] >= 2:
                            tables.append("medium")
                            tables.append("short")
                            tables.append("short")

                        elif available["short_table"] >= 4:
                            tables.append("short")
                            tables.append("short")
                            tables.append("short")
                            tables.append("short")

                if len(tables) == 0:

                    print("---------------------------")
                    print("No suitable table available")
                    print("---------------------------")
                    continue

                try:

                    table_duration = int(
                        input("Enter time duration (in hours): ")
                    )

                    if table_duration <= 0:

                        print("---------------------------")
                        print("Duration must be greater than 0")
                        print("---------------------------")
                        continue

                except Exception:

                    print("---------------------------")
                    print("Please enter a valid number")
                    print("---------------------------")
                    continue

                table_time = datetime.datetime.now()

                for size in tables:
                    available[size + "_table"] -= 1

                with open("python/task/available_table.json", "w") as file:
                    json.dump(available, file, indent=4)

                print("-----------------------")
                print("Available table updated")
                print("-----------------------")

                for size in tables:

                    table_id = str(uuid.uuid4().int)[:3]

                    obj = Table(
                        table_id,
                        size,
                        table_time,
                        table_duration,
                        user
                    )

                    obj.table_book()

                print("---------------------------")
                print("Total table booked :", len(tables))
                print("---------------------------")

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
