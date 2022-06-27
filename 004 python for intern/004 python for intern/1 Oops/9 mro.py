# method resolution order takes method of super class in a order formate

class A:
    def feature1(self):
        print("feature of class a")

class B:
    def feature1(self):
        print("feature of class b")

class C(A,B):
    def feature1(self):
        super().feature1()
        print("feature of class c")

c1=C()
c1.feature1()