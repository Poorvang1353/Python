num = int(input("Enter a number: "))
check = list(range(1, num+1))

for number in check:
    if num % number == 0:
        print(number)