students=[
    {"name":"ayan", "marks":85},
    {"name":"awaz", "marks":55},
    {"name":"rehan", "marks":45},
    {"name":"ikra", "marks":34},
    {"name":"sohil", "marks":10}
]

count=0
print("\n***passing Max is more than 50***")
print("\n***PASS Student***")

for student in students:
    if student["marks"]>50:
        print(student["name"],"=",student["marks"] )
        count+=1
    

print("\n***FAIL Student***")

for student in students:
    if student["marks"]<50:
        print(student["name"],"=",student["marks"])

print("\n***add 2 more student***")

students.append({"name":input("enter student name :"), "marks":int(input("enter marks"))})
students.append({"name":input("enter student name :"), "marks":int(input("enter marks"))})

print("\n***Pass student***")
for student in students:
    if student["marks"]>50:
        print(student["name"],"=",student["marks"] )
        count+=1

print("\n***Fail student***")
for student in students:
    if student["marks"]<50:
        print(student["name"],"=",student["marks"])
        
    

print("\ntotal pass student",count)    