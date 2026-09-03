def fibonacci(number):
    first = 0
    second = 1


    for i in range(number):
        print(first)
        third = first + second
        first = second
        second = third


num = int(input("Enter the number of terms: "))
fibonacci(num)