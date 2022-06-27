# A variable created inside a function belongs to the local 
# scope of that function, and can only be used inside that function.

# def myfunc():
#     x = 300
#     print(x)

# myfunc()

# The local variable can be accessed from a function within the function:

# def myfunc():
#     x = 300
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()

# myfunc()

# A variable created in the main body of the Python code 
# is a global variable and belongs to the global scope.

# x = 300

# def myfunc():
#   print(x)

# myfunc()

# print(x)

# If you use the global keyword, the variable belongs to the global scope:

# def myfunc():
#     global x
#     x = 300

# myfunc()

# print(x)

# To change the value of a global variable inside a function,
# refer to the variable by using the global keyword:

# x = 300

# def myfunc():
#     global x
#     x = 200

# myfunc()

# print(x)





