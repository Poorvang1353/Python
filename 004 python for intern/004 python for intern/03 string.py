
# # Strings:

# x = str("s1") # x will be 's1'
# y = str(2)    # y will be '2'
# z = str(3.0)  # z will be '3.0'

# print(type(x))
# print(type(y))
# print(type(z))

# # Assign String to a Variable
# a = "Hello"
# print(a)

# # Multiline Strings
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)


# # Strings are Arrays
# a = "Hello, World!"
# print(a[1])

# # String Length
# a = "Hello, World!"
# print(len(a))

# # Check String
# txt = "The best things in life are free!"
# print("free" in txt)



# # Slicing Strings
# # Get the characters from position 2 to position 5 (not included):
# b = "Hello, World!"
# print(b[2:5])

# # Get the characters from the start to position 5 (not included):
# b = "Hello, World!"
# print(b[:6])

# # Get the characters from position 2, and all the way to the end:
# b = "Hello, World!"
# print(b[2:])




# # Get the characters:
# # From: "o" in "World!" (position -5)
# # To, but not included: "d" in "World!" (position -2):

# b = "Hello, World!"
# print(b[-5:-2])


# # Modify Strings
# The upper() method returns the string in upper case:
# a = "Hello, World!"
# print(a.upper())


# # The lower() method returns the string in lower case:
# a = "HELLO WORLD"
# print(a.lower())


# # The strip() method removes any whitespace from the beginning or the end:
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"


# # The replace() method replaces a string with another string:
# a = "Hello, World!"
# print(a.replace("World", "GUYS"))


# # The split() method splits the string into substrings if it finds instances of the separator:
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']


# # String Concatenation
# # Merge variable a with variable b into variable c:

# a = "Hello "
# b = "World"
# c = a + b
# print(c)


# # To add a space between them, add a " ":

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)


# # String Format
# # As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

# Example
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# # Use the format() method to insert numbers into strings:
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))
# # print(type(age))


# # The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))


# # You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))


