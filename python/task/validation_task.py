users=["ayan","anas","ovesh","rehan"]
password=["232","789","786","123"]


def menu():
    print("*********** MENU BAR ************")
    print("1. sign up")
    print("---------------")
    print("2. login")
    print("---------------")
    print("3. delete")
    print("---------------")
    print("4. deshboard")
    print("---------------")
    print("5. exit")
    print("---------------")
    print("*********************************")
        


def sign_up(new_user,new_pass):
    if new_user.isalnum() and new_pass.isalnum():
        if new_user in users:
            print("-----------------------------")
            print("this user is already register")
            print("-----------------------------")
        else:
            users.append(new_user)
            password.append(new_pass)
            print("---------------------")
            print("registration complete")
            print("---------------------")    
    else:
        print("-----------------------------")
        print("user or password is not valid")
        print("-----------------------------")    
    
def login(search):
    if search in users:
        print(users)
        print(password)
    else:
        print("----------------------------")
        print("***your name is not in data***")
        print("----------------------------")    

def delete(delete_user):
    if delete_user in users:
        index_num = users.index(delete_user)   
        users.pop(index_num)                   
        password.pop(index_num)
        
        print("---user deleteted---")
        print("user :",index_num) 
        print("--------------------")              
    else:
        print("--------------")
        print("User not found")
        print("--------------")

while True:
    menu()

    option=(input("enter your option :"))
    if option.isdigit():
        option = int(option)
        if option == 1:
                user=input("enter new user name :")
                new_pass=input("enter your password :")
                
                if len(user) <= 2 and len(user) >=8 and len(new_pass) <=8 :
                        if new_pass.count("0") > 2:
                            print("-------------------------")
                            print("0 more than 2 not allowed")
                            print("-------------------------\n")
                        else:
                            sign_up(user,new_pass)    
                else:
                    print("\n--------------------------------------")
                    print("name or password length is more than 7")
                    print("--------------------------------------\n")
                    
        elif option == 2:
                check = input("\nenter your name :")
                login(check)
        
        elif option == 3:
            delete_user=input("enter delete user :")
            delete(delete_user)
        
        elif option ==  4:
            print(users)
            print(password)           
            
        elif option == 5:
                print("*/*/*/*/*/***/*/*/**/**")
                print("***thanks for visit***")
                print("/*/*/****/*/*/***/*/***")
                break      
    else:
        print("/*/***/*//*/*/*")
        print(" invalid...")
        print("*//*/****/*/*//")    
