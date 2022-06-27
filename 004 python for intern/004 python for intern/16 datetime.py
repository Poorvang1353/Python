# Import the datetime module and display the current date:

# import datetime

# x = datetime.datetime.now()
# print(x)

# When we execute the code from the example above the result will be:

# 2022-06-13 13:37:57.631452
# The date contains year, month, day, hour, minute, second, and microsecond.

# Return the year and name of weekday:

# import datetime

# x = datetime.datetime.now()

# print(x.year)
# print(x.strftime("%A"))

# Create a date object:

# import datetime

# x = datetime.datetime(2020, 5, 17)

# print(x)

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.


import datetime

x = datetime.datetime(2018, 6, 1)

# print(x.strftime("%B"))
print(x.strftime("%a")) #Weekday, short version

# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM



