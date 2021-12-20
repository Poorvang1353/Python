n = 18
number_of_guesses=1
print("Number of guesses is limited to only 9 times: ")
while(number_of_guesses<=9):
    guess_number = int(input("Guess the number = "))
    if guess_number<18:
        print("Please enter greater number\n")
    elif guess_number>18:
        print("Please entre lesser number\n")
    else:
        print("You won!\n")
        print("You guessed in",number_of_guesses,"attempt")
        break
    print(9-number_of_guesses,"Guesses left\n")
    number_of_guesses+=1

if number_of_guesses>9:
    print("Game over!")
    print("The secret number is 18")
