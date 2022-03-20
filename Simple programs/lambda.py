#Before using lambda
from re import A
from unittest import result


def sqaure(a):
    return a*a

p = sqaure(5)
print(p)

#After using lambda 
f = lambda a: a*a

result = f(5)
print(result)


#Another example
f= lambda a,b: a+b
result = f(5 ,3)
print(result)