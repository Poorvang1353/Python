def fibonacci():
    x=0
    y=1
    list = [x,y]
    num = int(input("Enter the number you want to print fibonacci series: "))

    while y<=num:
        # print(y)
        x,y = y,x+y
        list.append(y)
    print(list[1:-1])

    return fibonacci()


print(fibonacci())