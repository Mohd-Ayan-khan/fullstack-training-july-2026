import os
import json

subjects=[]
data={}
def json_data():
    user = input("Enter your json File name: ")
    data["id"]=input("Enter your ID :")
    data["name"]=input("Enter your Name :")
    data["class"]=input("Enter your Class :")
    data["city"]=input("Enter your City :")
    data["cours"]=input("Enter your Course :")
    
    print("\n=========================================")
    s=int(input("Enter how many subject you study :"))
    print("===========================================")
    
    for i in range(s):
        subject = input(f"\nenter your {i+1} subject :")
        mark = input(f"enter {i+1} subject marks :")
        subjects.append({"subjects":subject,"marks":mark})
    
    data["Subjects"]=subjects
    
    with open(user + ".json","w") as file:
        json.dump(data, file, indent=4)

    with open(user + ".txt","w") as file:
        file.write("---------------------\n")
        file.write("-- student detail --\n")
        file.write("---------------------\n\n")
        
        file.write(f"ID     :   {data['id']}\n")
        file.write(f"NAME   :   {data['name']}\n")
        file.write(f"CLASS  :   {data['class']}\n")
        file.write(f"CITY   :   {data['city']}\n")
        file.write(f"COURSE :   {data['cours']}\n")
        
        file.write("\n------------------")
        file.write("\n -- subjects: --\n")
        file.write("-----------------\n")
        
        for subject in data["Subjects"]:
            file.write(f"{subject['subjects']} : {subject['marks']}\n")
        
        file.write("------------------------")
        
        print("===============================")
        print(" YOUR JSON AND TXT FILE CREATED")
        print("===============================")
        

def get(name):
    
    with open(name,'r') as file:
        data = json.load(file)
        print(data)
    
    new = input("enter your new txt file name :\n")
    user = int(input("how many data you want to get :\n"))
    
    choice = []
    for i in range(user):
        ask = input("enter your data :")
        choice.append(ask)
    
    with open(new + ".txt","w") as file:
        for key,value in data.items():
            if key in choice:
                file.write(key + ":" + str(value) + "\n")
        
        print("------------------")
        print("data sussecfull")
        print("------------------")


def insert(flag):
    while True:
            print("\n--------------")
            print("1. Create File")
            print("--------------")
            print("2. Insert Data")
            print("--------------")
            print("3. Exit")
            print("--------------")
            
            option = int(input("enter your choice :\n"))
            
            if option == 1:
                file_name = input("Enter your file name :")
                with open(os.path.join(flag,file_name),"w") as file:
                    file.write("")
                    print("////////////")
                    print("file created")
                    print("////////////")
            elif option == 2:
                f = input("Enter file name :")
                data = input("Enter your data :")
                
                with open(os.path.join(flag,f),"w") as file2:
                    file2.write(data)
                    
                    print("//////////////////")
                    print("data will be added")
                    print("//////////////////")
                    
            elif option == 3:
                break
            else:
                print("///////////////")
                print("invalid number")
                print("*//////////////")




while True:
    print("\n-------------------")
    print("1. Create Directory")
    print("-------------------")
    print("2. Delete Directory")
    print("-------------------")
    print("3. Create json file")
    print("-------------------")
    print("4. data get")
    print("-------------------")
    
    option = int(input("enter your choice :"))
    
    if option == 1:
        name=input("Enter Directory Name :")
        os.mkdir(name)
        print("-----------------")
        print("Directory Created")
        print("-----------------")
        
        print("--------------------------------")
        print("Do you want to create file (y/n)")
        print("--------------------------------")
        
        choice = input("Enter your choice :")
        
        if choice == "y":
            insert(name)
        elif choice == "n":
            break
        else:
            print("///////////////")
            print("invalid number")
            print("*//////////////")
    
    elif option == 2:
        direct = input("Enter Directory name :")
        
        for file in os.listdir(direct):
            path = os.path.join(direct, file)

            if os.path.isfile(path):
                os.remove(path)

        os.rmdir(direct)

        print("\n----------------------")
        print("Directory was deleted")
        print("----------------------\n")
    elif option == 3:
        json_data()
    elif option == 4:
        file_name = input("enter your file name :")
        get(file_name)
    else:
        print("**************")
        print("invalid number")
        print("**************")
