str = input("Enter your string: ")
vowels = 0
for i in str:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='I' or i=='i' or i=='o' or i=='O' or i=='u' or i=='U'):
        vowels = vowels + 1
print("Total number of vowels in this string = ",vowels)