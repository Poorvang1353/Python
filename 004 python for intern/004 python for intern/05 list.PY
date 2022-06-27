# # Python Lists
# # List items are ordered, changeable, and allow duplicate values.

# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# # Lists allow duplicate values:
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)

# # List Length
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# # A list with strings, integers and boolean values:
# list1 = ["abc", 34, True, 40, "male"]


# # What is the data type of a list?
# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# # Using the list() constructor to make a List:
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# # Access List Items

# # Print the second item of the list:
# thislist = ["apple", "banana", "cherry"]
# print(thislist[1])

# # Print the last item of the list:
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# # Return the third, fourth, and fifth item:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# # This example returns the items from the beginning to, but NOT including, "kiwi":
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# # This example returns the items from "cherry" to the end:
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# # Change Item Value
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# # Change a Range of Item Values
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# # Add List Items
# # To add an item to the end of the list, use the append() method:
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# # Insert an item as the second position:
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)

# # Add the elements of tropical to thislist:
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)


# # Remove List Items
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# # Specified Index
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# # Remove the last item:
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)


# # Remove the first item:
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)


# # Delete the entire list:
# thislist = ["apple", "banana", "cherry"]
# del thislist

# # Clear the list content:
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# # Sort List Alphanumerically
# # Sort the list alphabetically:
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# # Sort the list numerically:
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# # Sort the list descending:
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# # Copy Lists
# # Make a copy of a list with the copy() method:
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


# # Make a copy of a list with the list() method:
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)



# # Join Lists
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# # Use the extend() method to add list2 at the end of list1:
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

# # List Methods
# # Add an element to the fruits list:
# fruits = ['apple', 'banana', 'cherry']
# fruits.append("orange")


# # Remove all elements from the fruits list:
# fruits = ['apple', 'banana', 'cherry', 'orange']
# fruits.clear()


# # Return the number of times the value "cherry" appears in the fruits list:
# fruits = ['apple', 'banana', 'cherry']
# x = fruits.count("cherry")

# # What is the position of the value "cherry":
# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry")

# # Insert the value "orange" as the second element of the fruit list:
# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(1, "orange")


# # Remove the second element of the fruit list:
# fruits = ['apple', 'banana', 'cherry']
# fruits.pop(1)


# # Remove the "banana" element of the fruit list:
# fruits = ['apple', 'banana', 'cherry']
# fruits.remove("banana")