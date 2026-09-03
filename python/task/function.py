num=[20,11,67,29,32]


while(True):
    print("\n*******************")
    print("1. append")
    print("2. pop")
    print("3. insert")
    print("4. remove")
    print("5. count")
    print("6. reverse")
    print("7. clear")
    print("8. copy")
    print("9. extend")
    print("10. sort")
    print("11. index")
    print("12. Exit")
    print("*******************")


    option=int(input("enter a option :"))

    if option == 1:
        number=int(input("enter your Number :"))
        print(num)
        num.append(number)
        print(num)

    elif option == 2:
        num.pop()
        print(num)    

    elif option == 3:
        number=int(input("enter your Number :"))
        index=int(input("enter your index :"))
        print()
        num.insert(index,number)
        print(num)    

    elif option == 4:
        number=int(input("enter your Number :")) 
        num.remove(number)

    elif option == 5:
        number=int(input("enter your Number :")) 
        n=num.count(number)
        print(n)
        
    elif option == 6:
        num.reverse()
        print(num)    

    elif option == 7:
        num.clear()
        print(num)
        
    elif option == 8:
        copy_list=num.copy()
        print(num)
        print(copy_list)
        
    elif option == 9:
        num2=[1,2,3,5]
        num.extend(num2)
        print(num)

    elif option == 10:
        print(num)
        num.sort()
        print(num)

    elif option == 11:
        print(num)
        number=int(input("enter your number :"))
        print(num.index(number))
    
    elif option == 12:
        break
        
        