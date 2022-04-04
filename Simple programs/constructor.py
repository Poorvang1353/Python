class Employee:

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}, Salary is {self.salary} and role is {self.role}"

Poorvang = Employee("Poorvang", 342, "Instructor")
print(Poorvang.salary)