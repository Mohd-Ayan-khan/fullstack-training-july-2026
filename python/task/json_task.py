import json
import os
import uuid


def ragister():

    deatail = {}

    deatail["id"] = str(uuid.uuid4().int)[:3]
    deatail["name"] = input("Enter your Name : ")
    deatail["age"] = input("Enter your Age : ")
    deatail["gmail"] = input("Enter your Gmail id : ")
    deatail["qualification"] = input("Enter your Qualification : ")

    file_name = "json_data.json"

    if os.path.exists(file_name):

        with open(file_name, "r") as file:
            data = json.load(file)

    else:
        data = []

    data.append(deatail)

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

    print("========================")
    print("Registration successful!")
    print("========================")

def update(search):
    
    with open("json_data.json",'r') as file:
        data=json.load(file)
    
    for user in data:
        
        if user["id"] == search:
            
            print("\n==== USER FOUND ====")
            
            print("\n=====================")
            print("---- Update data ----")
            print("=====================")
            
            user["name"]=input("Enter New Name :")
            user["age"]=input("Enter New Age :")
            user["gmail"]=input("Enter New Gmail :")
            user["qualification"]=input("Enter New Qualification :")
            
            with open("json_data.json","w") as file:
                json.dump(data,file, indent=4)
            
            print("////////////")
            print("Data Updated")
            print("////////////")
            
            return
    print("////////////")
    print("ID not found")
    print("////////////")

def delete(search):
    
    with open("json_data.json",'r') as file:
        data = json.load(file)
    
    for user in data:
        if user["id"] == search:
            data.remove(user)
            
            with open("json_data.json","w") as file:
                json.dump(data,file,indent=4)
            
            print("====================")
            print("--- User Removed ---")
            print("====================")
            return
        
    print("------------")
    print("ID not found")
    print("------------")
    
while True:

    print("==============")
    print("1. Register")
    print("==============")
    print("2. Update data")
    print("==============")
    print("3. Delete data")
    print("==============")
    print("4. Exit")
    print("==============")

    option = int(input("Enter your choice : "))

    if option == 1:
        ragister()

    elif option == 2:
        search = (input("Enter user id :"))
        update(search)
    elif option == 3:
        search = input("Enter user id :")
        delete(search)
    elif option == 4:
        break
    else:
        print("==============")
        print("INVALID NUMBER")
        print("==============")