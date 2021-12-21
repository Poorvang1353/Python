age = int(input("Enter your age : "))

if 1 < age < 18:
    print("You can't drive")
elif 18 < age < 100:
    print("You can drive")
else:
    print("Your age is invalid")
