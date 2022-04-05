num = int(input("Enter a number: "))
check = list(range(1, num+5))

for number in check:
    if num % number == 0:
        print(number)