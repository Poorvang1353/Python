print("Enter the first number")
num1 = int(input())
print("Enter the second number ")
num2 = int(input())
print("Enter any operator(+,-,*,/,%)")
opr = input()


if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "/":
    print(num1 / num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "%":
    print(num1 % num2)
else:
    print("Unexepted choice")
