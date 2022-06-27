# to take any constructor or method of super class we have to use "super()" keyword

class A:
    
    def __init__(self):
        print("in a init")

class B(A):

    def __init__(self):
        super().__init__()
        print("in b init")

b1=B()