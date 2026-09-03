hindi=int(input("enter your hindi marks"))
english=int(input("enter english marks"))
math=int(input("enter math marks"))

if hindi >= 0 or hindi <= 100 or english >= 0 or english <= 100 or math >= 0 or math <= 100:
    print("\n**** number not valid ****")

else:
    total=hindi+english+math
    percent=(total/300)*100

    print("total: ",total)
    print("percent :",percent)

    if percent >= 90:
        print("A gard")

    elif percent >=60:
        print("b grade")
    
    elif percent >=50:
        print("c grade")
    
    elif percent >=40:
        print("d grade")
    
    else:
        print("fail") 
