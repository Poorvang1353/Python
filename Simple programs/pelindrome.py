


i = int(input("Enter the number: "))
rev = 0
x = i
while(i>0):
    rev = (rev*10)+i%10
    i = i//10
if(x==rev):
    print(x," is pelindrome number")
else:
    print(x," is not pelindrome number")