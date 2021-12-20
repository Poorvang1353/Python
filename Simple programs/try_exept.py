print("Enter the fist number")
num1 = input()
print("Enter the second number")
num2 = input()

try:
    print("The sum of two number is", int(num1) + int(num2))

except Exception as error:
    print(error)


print("This line is very important")
