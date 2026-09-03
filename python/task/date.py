import datetime

now = datetime.datetime.now()

year = now.strftime("%Y")
month = now.strftime("%B")
date = now.strftime("%d")
hours = now.strftime("%I")
minute = now.strftime("%M")
sec = now.strftime("%S")

print("\n---- current date / month and year ----")
print("\nToday :", date, "/", month, "/", year)
print("-----------------------------------------")

print("\n----------- current time ------------------")
print("\nTime :", hours, ":", minute, ":", sec,)
print("---------------------------------------------")

print("\n------------------------------")
print("********* week finder ********")
print("------------------------------")

while True:
    user_date = (input("Enter your date :"))
    if user_date.isdigit():
        user_date = int(user_date)
        if user_date < 32:
                break
        else:
            print("invalid date...") 
    else:
        print("\n----------------------")
        print("only digit are allowed")
        print("----------------------")
        
        
while True:
    user_month = (input("Enter your month :"))
    if user_month.isdigit():
            user_month = int(user_month)
            if user_month < 13:
                    break
            else:
                print("invalid date...") 
    else:
        print("\n----------------------")
        print("only digit are allowed")
        print("----------------------")
        
while True:
    user_year = (input("Enter your year :"))
    if len(user_year) == 4 and user_year.isdigit():
        user_year=int(user_year)
        if user_year < 10000:
            break
        else:
            print("invalid...")
    else:
        print("invalid year...")
user = datetime.datetime(user_year,user_month,user_date)

print("Week is:", user.strftime("%A"))