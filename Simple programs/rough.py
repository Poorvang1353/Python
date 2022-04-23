class circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

    def perimeter(self):
        return 2*3.14*self.radius


newCircle = circle(8)
print(newCircle.area)
print(newCircle.perimeter) 