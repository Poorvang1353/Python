string = input("Enter your string: ")
str1 = ""
for i in string:
    str1 = i + str1  
print("Reverse Order :  ", str1)
if(string == str1):
   print("Entered string is a Palindrome String")
else:
   print("Entered string is not a Palindrome String")