# s = "Silver Oak University"
# s1 = s.replace("e","" )
# s2 = s1.replace("s","")
# print(s2)


# lst = [10,3,6,4]
# lst.reverse()
# print(lst)


# days = 365
# hr = 24
# mins = 60
# minInYear= days*hr*mins
# print(minInYear)



# def Average(lst):
# 	return sum(lst) / len(lst)

# lst = [15, 9, 55, 41, 35, 20, 62, 49]
# average = Average(lst)

# print("Average of the list =", average)



# def decimalToBinary(n):
#     return bin(n).replace("0b","")
# if __name__ == '__main__':
#     print(decimalToBinary(18))
#     print(decimalToBinary(8))
#     print(decimalToBinary(7))


#sort list without using built-in function
# my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
# new_list = []

# while my_list:
#     min = my_list[0]  
#     for x in my_list: 
#         if x < min:
#             min = x
#     new_list.append(min)
#     my_list.remove(min)    

# print(new_list)



#prime number or not
# num = 12
# if num > 1:
  
#     for i in range(2, int(num/2)+1):
  
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
  
# else:
    # print(num, "is not a prime number")



#reversed string using user difined function
# def reverse(str):   
#     string = "".join(reversed(str)) # reversed() function inside the join() function  
#     return string   
  
# s = "JavaTpoint"  
  
# print ("The original string is : ",s)   
# print ("The reversed string using reversed() is : ",reverse(s) )  


# tp = (1,2,3,4,5,6,7,8,9,10)
# li = list()
# for i in range(len(tp)):
#     if(tp[i] %2==0):
#         li.append(tp[i])
# tp2 = tuple(li)
# print(tp2)


# num = int(input("Enter the number: "))
# sum = 0
# temp = num
# while(temp>0):
#     digit=temp%10
#     sum += digit**3
#     temp//=10

# if(num==sum):
#     print(num ,"is a armstrong number")
# else:
#     print(num , "is not a armstrong number")


