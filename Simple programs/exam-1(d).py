#prime number or not


num = int(input("Enter the number between 1 to 100: "))

if(1<num<101):
    if num > 1:
  
        for i in range(2, int(num/2)+1):
  
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
  
    else:
        print(num, "is not a prime number")

else:
    print("Please, Enter valid input")