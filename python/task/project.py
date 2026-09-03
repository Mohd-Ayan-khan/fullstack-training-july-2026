data={}

print("*****************************")
print("*** smart student id card ***")
print("*****************************")

data["institute"]=input("enter institute name :").capitalize()

while 1:
    data["student"]=input("enter student name :").capitalize()

    if data["student"].isalpha() == 1:
        break
    else:
        print("invalid name...")

while 1:
    data["father"]=input("enter father name :").capitalize()
    if data["father"].isalpha() == 1:
        break
    else:
        print("invalid name...")

while 1:
    data["roll"]=input("enter roll number :").zfill(10)
    if data["roll"].isdigit() == 1:
        break
    else:
        print("invalid roll number...")

data["class"]=input("enter your class :")
data["section"]=input("enter your section :")
data["department"]=input("enter your department :").title()
data["city"]=input("enter your city :").capitalize()
data["blood"]=input("enter your blood group :").capitalize()

while 1:
    data["phone"]=input("enter your phone number :")
    if data["phone"].isdigit():
        break
    else:
        print("invalid phone number...")


print("-------------------------")
print(" \tSTUDENT ID CARD ")
print("-------------------------")

print(f" {data["student"]}")

print(f" STUDENT NAME : {data["student"]}")
print(f" ROLL NUMBER : {data["roll"]}")
print(f" DEPARTMENT : {data["department"]}")
print(f" CITY : {data["city"]}")

print("Validation Report : ")
print(f" Name valid : True")
print(f" Roll Valid : True\n")

print("Student Code : ")
print(f"Student code : {data["department"]}-{data["section"]}-{data["roll"]}")