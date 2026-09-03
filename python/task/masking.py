import maskpass
import json
data = []

class Ragistration:
    
    def __init__(self,password=""):
        self.__password = password

    def ragister(self):
        
        dict = {}
        
        dict["id"]=input("Enter your ID :")
        
        self.__password = maskpass.askpass("Enter your password :",mask="*")
        
        dict["password"]=self.__password
        dict["name"]=input("Enter your Name :")
        dict["age"]=int(input("Enter your Age :"))
        dict["address"]=input("Enter your Address :")
        
        data.append(dict)
        
        print("---------------------")
        print("Ragistration complete")
        print("---------------------")
    
    def get_pass(self):
        return self.__password
    
    def set_pass(self,new_pass):
        self.__password = new_pass
        

class display(Ragistration):
    
    def display(self):
        print(json.dumps(data, indent = 4))
            
    

class update(display):
    
    
    def update_data(self,ask):
        
        for user in data:
            if ask == user["id"]:
                        print("-------------------")
                        print("--- Change list ---")
                        print("-------------------")
                        print("1. ID")
                        print("-------------------")
                        print("2. Password")
                        print("-------------------")
                        print("3. Name")
                        print("-------------------")
                        print("4. Age")
                        print("-------------------")
                        print("5. Address")
                        print("-------------------")
                        
                        option = int(input("Enter your choice :"))
                        
                        if option == 1:
                            id1 = input("Enter new id :")
                            user["id"] = id1
                            
                            print("-----------")
                            print("data change")
                            print("-----------")
                        
                        elif option == 2:
                            new_pass = maskpass.askpass("Enter new password :",mask="*")
                            user["password"] = new_pass
                            
                            print("---------------")
                            print("password change")
                            print("---------------")
                                
                            
                        elif option == 3:
                            name1 = input("Enter new name :")
                            user["name"] = name1
                            
                            print("-----------")
                            print("data change")
                            print("-----------")
                        
                        elif option == 4:
                            age1 = int(input("Enter new age :"))
                            user["age"] = age1
                            
                            print("-----------")
                            print("data change")
                            print("-----------")
                        
                        elif option == 5:
                            add = input("Enter new address :")
                            user["address"] = add
                            print("-----------")
                            print("data change")
                            print("-----------")
                        
                        else:
                            print("--------------")
                            print("invalid number")
                            print("--------------")
            else:
                print("--------------")
                print("user not found")
                print("--------------")

class delete(update):
    
    def deleter(self,ask):
        
        for user in data:
            if ask == user["id"]:
                data.remove(user)
                
                print("----------------")
                print("User deleted")
                print("----------------")
                break
            else:
                print("--------------")
                print("user not found")
                print("--------------")


        


class menu(update):
    
    def menu1(self):
        while True:
            print("===============")
            print("1. Ragistration")
            print("===============")
            print("2. Display")
            print("===============")
            print("3. Update")               
            print("===============")
            print("4. Delete")
            print("===============")
            print("5. Exit")
            print("===============")
            
            choice = int(input("Enter your choice :"))
            
            if choice == 1:
                op = menu()
                op.ragister()
                
            elif choice == 2:
                op.display()
            
            elif choice == 3:
                ask = input("Enter your id :")
                op.update_data(ask)
            
            elif choice == 4:
                object1 = delete()
                ask = input("Enter Deleter user id :")
                object1.deleter(ask)
            
            elif choice == 5:
                print("------------------")
                print("thanks for visting")
                print("------------------")
                break
            else:
                print("-------------")
                print("invalid numer")
                print("-------------")
object = menu()
object.menu1()
                
                
                              
                
                    
            
            
            
        