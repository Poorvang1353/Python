# class Student:
    
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         self.lap=self.Laptop()

#     def show(self):
#         print(self.name,self.rollno)
#         self.lap.show()

#     class Laptop:

#         def __init__(self):
#             self.brand="HP"
#             self.cpu="i5"
#             self.ram=16

#         def show(self):
#             print(self.brand,self.cpu,self.ram)
        

# s1=Student("ramesh",1)
# s2=Student("mukesh",2)

# s1.show()
# s2.show()

class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # self.add=self.Address()

    def person_show(self):
        print(self.name,self.age)
        # self.add.address_show()

    # class Address:
        
    #     def __init__(self,street,contact):
    #         self.street=street
    #         self.contact=contact

    #     def address_show(self):
    #         print(self.street,self.contact)

    # a1=Address("amarnath",46138)
    # a2=Address("harihar",361214)

    # a1.address_show()
    # a2.address_show()
        
p1=Person("harsh",20)
p2=Person("deep",25)

p1.person_show()
p2.person_show()