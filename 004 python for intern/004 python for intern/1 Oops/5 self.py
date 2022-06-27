class Person:
    
    def __init__(self):
        self.name="navin"
        self.age=20

    def update(self):
        self.age=28

c1=Person()
c2=Person()

print(c1.name)
print(c1.age)

c1.update()
print(c1.age)
        
    