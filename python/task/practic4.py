datadict={}

datadict["id"]=int(input("enter your id :"))
datadict["name"]=(input("enter your name :"))
datadict["address"]=(input("enter your address :"))
datadict["pin"]=int(input("enter your pin :"))
datadict["course"]=(input("enter your course :"))
datadict["qualification"]=(input("enter your qualification :"))


for key,value in datadict.items():
    print(f"{key} = {value}")

