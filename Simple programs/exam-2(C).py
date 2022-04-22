def fizzler(num):

    if num % 3 != 0 and num % 5 != 0:
        return num

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"

    if num % 3 == 0:
        return "Fizz"

    return "Buzz"

if __name__ == "__main__":

    number = int(input("Enter a number: "))

print(fizzler(number))

