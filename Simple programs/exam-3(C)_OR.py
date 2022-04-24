list1= [9,8,7,6,5,4,3,]
print('Original list:', list1)
list2=[]
length=len(list1)


while length > 0:
    list2.append(list1[length-1])
    length = length - 1
print('Reversed list:', list2)


