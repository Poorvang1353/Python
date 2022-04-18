
print("Select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:

    choise = input("Enter choise(1/2/3/4): ")

    if choise in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choise == '1':
             print(num1, '+', num2, '=', (num1+num2))
        elif choise == '2':
            print(num1, '-', num2, '=', (num1-num2))
        elif choise == '3':
            print(num1, '*', num2, '=', (num1*num2))
        elif choise == '4':
            print(num1, '/', num2, '=', (num1/num2))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
