data={}

data["id"]=int(input("enter id :"))
data["name"]=(input("enter your name :"))
data["address"]=(input("enter your addres :"))
data["pin"]=(int(input("enter your pin code :")))

if data["pin"] >= 100000 and data["pin"] <= 999999:
    print("valid")
else:
    print("not valid")        
    
print(data)    