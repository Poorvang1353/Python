class Person:
    
    Hobby="Playing Cricket" #variable define outside init and inside the class is called class variable

    def __init__(self):  #the variable defined inside init is called instance variable
        self.name = "harsh"
        self.age = 28


c1=Person()
c2=Person()

Person.Hobby = "Watching TV" #we can change the class variable

print(c1.name,c1.age,c1.Hobby)
print(c2.name,c2.age,c2.Hobby)



# c1.name="mahesh" #we can also change the name
# print(c1.name)




    