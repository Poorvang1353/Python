def factorial_itretive(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    if n==1:
        return 1    
    else:
        return n * factorial_recursive(n-1)

number = int(input("Enter the number: "))
print("Factorial using itretive method",factorial_itretive(number))


print("\nFactorial using recursive method",factorial_recursive(number))