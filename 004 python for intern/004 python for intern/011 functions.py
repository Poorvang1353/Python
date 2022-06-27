# Creating a Function
# def my_function():
#   print("Hello from a function")

# Calling a Function
# def my_function():
#       print("Hello from a function")

# my_function()


# Arguments
# def my_function(fname):
#       print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# Number of Arguments
# This function expects 2 arguments, and gets 2 arguments:

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")



# If you try to call the function with 1 or 3 arguments, you will get an error:
# Example
# This function expects 2 arguments, but gets only 1:

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")



# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name:

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")


# Keyword Arguments
# def my_function(child3, child2, child1):
#       print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# Arbitrary Keyword Arguments, **kwargs
# If the number of keyword arguments is unknown, add a double ** before the parameter name:

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")



# Default Parameter Value
# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value:

# Example
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# Passing a List as an Argument
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

# Example
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)


# Return Values
# To let a function return a value, use the return statement:

# Example
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# Example
# def myfunction():
#   pass
