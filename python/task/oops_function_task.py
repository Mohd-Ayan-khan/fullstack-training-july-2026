import uuid
import json
import os
import datetime


data = []

class logs():
    def log(self,error):
        with open("log.log",'w') as file:
            date = datetime.datetime.now()
            path = os.getcwd()
            file.write(f"{path} : \n{error} : \n{date}\n")


log1 = logs()

class ragistration:
    
    def ragister(self):
        user = {}
        
        user["id"] = str(uuid.uuid4().int)[:3]
        while True:
                try:
                    name = (input("Enter your name :"))
                    
                    if name.isalpha():
                        user["name"] = name
                        break
        
                    else:
                        log1.log("Name must contain alphabets only")
                        print("Invalid name")
        
                except Exception as e:
                    log1.log(e)
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
                                log1.log("Age must be between 1 and 100")
                                print("Invalid age")
        
                        else:
                            log1.log("Age must contain numbers only")
                            print("Invalid age")
        
                    except Exception as e:
                        log1.log(e)
                        print("Something went wrong")
            
        while True:
                try:
                    email = input("Enter Your Email :").lower()
                    
                    if '@' in email and '.' in email:
                        user["Email"] = email
                        break
                    
                    else:
                        log1.log("Error : invalid email formate")
                        print("invalid email")
                except Exception as e:
                    log1.log(e)
                    print("something went wrong")
        
        while True:
                try:
                    addres = input("Enter your Address :")
                    
                    if addres.isalpha():
                        user["address"]=addres
                        break
                    else:
                        log1.log("Error :Invalid address")
                        print("invalid addres")
                except Exception as e:
                    log1.log(e)
                    print("somthing went wrong")
                
        data.append(user)
                         
        with open("data.json",'w') as file:
            json.dump(data,file,indent=4)
        
        print("---------------------")
        print("Ragistration Complete")
        print("---------------------")
                        
class update_data(ragistration):
    
    def update(self,ask):
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
                                            log1.log("Name must contain alphabets only")
                                            print("Invalid name")
                            
                                    except Exception as e:
                                        log1.log(e)
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
                                                log1.log("Age must be between 1 and 100")
                                                print("Invalid age")
                            
                                        else:
                                            log1.log("Age must contain numbers only")
                                            print("Invalid age")
                            
                                    except Exception as e:
                                        log1.log(e)
                                        print("Something went wrong")
                        
                        elif option == '3':
                            while True:
                                    try:
                                        email = input("Enter Your Email :").lower()
                                        
                                        if '@' in email and '.' in email:
                                            user["Email"] = email
                                            break
                                        
                                        else:
                                            log1.log("Error : invalid email formate")
                                            print("invalid email")
                                    except Exception as e:
                                        log1.log(e)
                                        print("something went wrong")
                
                        elif option == '4':
                            while True:
                                    try:
                                        addres = input("Enter your Address :")
                                        
                                        if addres.isalpha():
                                            user["address"]=addres
                                            break
                                        else:
                                            log1.log("Error :Invalid address")
                                            print("invalid addres")
                                    except Exception as e:
                                        log1.log(e)
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


class delete_user(update_data):
    
    def delete(self,find):
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


obj = delete_user()


class menu(delete_user):
    
    def menu(self):
        
        while True:
            print("================")
            print("----- MENU -----")
            print("================\n")
            print("----------------")        
            print("1. Ragistration")
            print("----------------")        
            print("2. Update")
            print("----------------")        
            print("3. Delete")
            print("----------------")        
            print("4. Exit")
            print("----------------")
            
            option = input("Enter your choice :")
            
            if option.isdigit():
                if option == "1":
                    obj.ragister()
                
                elif option == "2":
                    ask = input("Update user id :")
                    obj.update(ask)
                
                elif option == "3":
                    ask = input("Enter delete user id :")
                    obj.delete(ask)
                
                elif option == "4":
                    print("-------------------")
                    print("Thanks for vistiong")
                    print("-------------------")
                    break
            else:
                print("--------------")
                print("invalid number")
                print("--------------")
                    

temp = menu()

temp.menu()                                
        
                    


