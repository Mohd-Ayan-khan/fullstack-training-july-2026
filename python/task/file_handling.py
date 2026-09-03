def create():
    file_name=input("enter your file name :")
    dataprint=input("enter your data :")
    
    with open(str(file_name),'w') as file:
        data = file.write(dataprint)
        print(data)


def read_file():
    search = input("enter your file name")
    
    with open(str(search),'r') as file:
        data = file.read()
        print(data)

def insert():
    name = input("enter your file name :")
    with open(name,"r") as see:
        print(see.read())
    
    with open(name,"w") as file:
        
        print("data position was :",file.tell())
        place = int(input("enter your postion :"))
        print("your current position was :",file.seek(place))
        
        word = input("enter your data :")
        file.write(word)


while True:
    print("------------------")
    print("1. create file")
    print("------------------")
    print("2. read file")
    print("------------------")
    print("3. insert somthing")
    print("------------------")
    
    
    choice=int(input("enter your choice :"))
    
    if choice ==1:
        create()
    elif choice == 2:
        read_file()
    elif choice == 3:
        insert()