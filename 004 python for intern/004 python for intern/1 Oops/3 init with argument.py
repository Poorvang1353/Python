# class Computer:
    
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram

#     def config(self):
#         print("config of computer is", self.cpu,self.ram)

# c1=Computer('i5',8)
# c2=Computer('rayzon 3',4)

# c1.config()
# c2.config()


# class Data:
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def getname(self):
#         print("name and age is", self.name, self.age)

# d1=Data("harsh",20)
# d2=Data("nitin",25)

# d1.getname()
# d2.getname()


class Person:
    
    def __init__(self):
        self.name="navin"
        self.age = 20

    def info(self):
        print("info of student is", self.name, self.age)

c1=Person()
c1.info()


        