num = int(input("Enter the number: "))
sum = 0
temp = num
while(temp>0):
    digit=temp%10
    sum += digit**3
    temp//=10

if(num==sum):
    print(num ,"is a armstrong number")
else:
    print(num , "is not a armstrong number")