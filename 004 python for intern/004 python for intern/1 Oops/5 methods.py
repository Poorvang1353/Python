class Student:
    
    Collage="Ganpat Collage"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def get_average(self): #instance method contains "self" keyword
        print("average is",(self.m1+self.m2+self.m3)/3)

    @classmethod #class method contains "cls" keyword also use "@classmethod" decorator
    def get_collage(cls):
        return cls.Collage

    #when you dont work to class variable and instance variable use the static variable 
    @staticmethod #static method contains " " nothing also use "@staticmethod" decorator
    def information():
        print("when you dont work with class variable and instance variable use the static variable")

    


s1=Student(10,20,30)
s2=Student(15,25,10)

s1.get_average()
s2.get_average()

# Student.Collage = "Marchent Collage" # we can change the value of class variable 

print(s1.get_collage())
print(s2.get_collage())

Student.information()
    