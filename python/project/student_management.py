import os
import uuid
import json
import datetime
user = {}
data=[]
def log(error):
    with open("log.txt",'w') as file:
        date = datetime.datetime.now()
        path = os.getcwd()
        file.write(f"{path} : \n{error} : \n{date}\n")

def deshboard():
    while True:
        print("\n==================")
        print("1. Ragister")
        print("==================")
        print("2. update")
        print("==================")
        print("3. delete")
        print("==================")
        print("4. Exit")
        print("==================")
        
        
        try:
            choic = int(input("Enter your choice :"))
            
            if choic == 1:
                ragister()
            
            elif choic == 2:
                ask = input("Enter user id :")
                update(ask)
            
            elif choic == 3:
                find = input("Enter delete user id :")
                delete(find)
                
            elif choic == 4:
                print("===================")
                print("thanks for visiting")
                print("===================")
                break
            else:
                print("--------------")
                print("invalid number")
                print("--------------")
        except:
            print("------------------")
            print("Only number alowed")
            print("------------------")
        

def ragister():
    
            
    user["id"] = str(uuid.uuid4().int)[:3]
    while True:
        try:
            name = (input("Enter your name :"))
            
            if name.isalpha():
                user["name"] = name
                break

            else:
                log("Name must contain alphabets only")
                print("Invalid name")

        except Exception as e:
            log(e)
            print("Something went wrong")

    
    while True:
            try:
                age = (input("Enter your age :"))
                
                if age.isdigit():
                    age = int(age)
                    if 1 <= age <= 100:
                        user["age"] = age
                        break

                    else:
                        log("Age must be between 1 and 100")
                        print("Invalid age")

                else:
                    log("Age must contain numbers only")
                    print("Invalid age")

            except Exception as e:
                log(e)
                print("Something went wrong")
    
    while True:
        try:
            email = input("Enter Your Email :").lower()
            
            if '@' in email and '.' in email:
                user["Email"] = email
                break
            
            else:
                log("Error : invalid email formate")
                print("invalid email")
        except Exception as e:
            log(e)
            print("something went wrong")
    
    while True:
        try:
            addres = input("Enter your Address :")
            
            if addres.isalpha():
                user["address"]=addres
                break
            else:
                log("Error :Invalid address")
                print("invalid addres")
        except Exception as e:
            log(e)
            print("somthing went wrong")
    
    data.append(user)
    
    with open("data.json",'w') as file:
        json.dump(data,file,indent=4)

def update(ask):
    with open("data.json",'r') as file:
        detail = json.load(file)
        
        for user in detail:
            if user["id"] == ask:
                
                while True:
                        print("=======================")
                        print("what you want to change")
                        print("=======================\n")
                        print("-----------------------")
                        print("1. Name")
                        print("2. age")
                        print("3. email")
                        print("4. address")
                        print("-----------------------")
                        
                        option = (input("Enter your choice :"))
                            
                        if option == '1':
                            
                            while True:
                                    try:
                                        name = (input("Enter your name :"))
                                        
                                        if name.isalpha():
                                            user["name"] = name
                                            break
                            
                                        else:
                                            log("Name must contain alphabets only")
                                            print("Invalid name")
                            
                                    except Exception as e:
                                        log(e)
                                        print("Something went wrong")
                            
                        elif option =='2':
                            while True:
                                    try:
                                        age = (input("Enter your age :"))
                                            
                                        if age.isdigit():
                                            age = int(age)
                                            if 1 <= age <= 100:
                                                user["age"] = age
                                                break
                            
                                            else:
                                                log("Age must be between 1 and 100")
                                                print("Invalid age")
                            
                                        else:
                                            log("Age must contain numbers only")
                                            print("Invalid age")
                            
                                    except Exception as e:
                                        log(e)
                                        print("Something went wrong")
                        
                        elif option == '3':
                            while True:
                                    try:
                                        email = input("Enter Your Email :").lower()
                                        
                                        if '@' in email and '.' in email:
                                            user["Email"] = email
                                            break
                                        
                                        else:
                                            log("Error : invalid email formate")
                                            print("invalid email")
                                    except Exception as e:
                                        log(e)
                                        print("something went wrong")
                
                        elif option == '4':
                            while True:
                                    try:
                                        addres = input("Enter your Address :")
                                        
                                        if addres.isalpha():
                                            user["address"]=addres
                                            break
                                        else:
                                            log("Error :Invalid address")
                                            print("invalid addres")
                                    except Exception as e:
                                        log(e)
                                        print("somthing went wrong")
                        else:
                            print("== invalid number ==")
                        
                        with open("data.json",'w') as file:
                            json.dump(detail,file,indent=4)
                            
                            print("============")
                            print("DATA CHANGED")
                            print("============")
                            break
            else:
                print("==================")
                print("==user not found==")
                print("==================")

def delete(find):
    with open("data.json","r") as file:
        temp = json.load(file)
    
    for user in temp:
        if user["id"] == find:
            temp.remove(user)
            
            with open("data.json","w") as file:
                json.dump(temp,file, indent = 4)
                
            print("===================")
            print("succesfully deleted")
            print("===================")
    
    

while True:
    print("===============")
    print("1. Ragistration")
    print("============")
    print("2. Exit")
    print("===============")
    
    option = input("enter your choice :")
    
    if option.isdigit():
        option = int(option)
        
        if option == 1:
            deshboard()
        
        elif option == 2:
            print("-------------------")
            print("Thanks for vistiong")
            print("-------------------")
            break
