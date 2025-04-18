import random 


def is_valid(user_input, lower, upper):
    return user_input.isdigit() and lower <= int(user_input) <= upper


def play_game(lower, upper, random_number, attempts):

    print("Random number:", random_number)

    user_input = (input(f"Please enter a number from {lower} to {upper}: "))

    user_input = int(user_input)

    if user_input > random_number:
        print("Your number is higher than the guessed one, try again")
        attempts  += 1
    elif user_input < random_number:
        print("Your number is less than the guessed one, try again")
        attempts  += 1
    elif user_input == random_number:
        print(f"\nYou guessed it, congratulations! The hidden number: {random_number}")
        print(f"\nNumber of attempts: {attempts }\n")
        attempts += 1
        return False
    else:
        print(f"Please enter a number from {lower} to {upper}.")
    return True


def repeat_game():

    while True:
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay == "y":
            main()
            break
        elif replay == "n":
            print("\nGoodbye!", end="\n""\n")
            print("Thank you for playing the guess the number program.", end="\n")
            break
        else:
            print("Please enter 'y' to start a new game or 'n' to exit.")


def main():

    print("Welcome to the game 'Guess the number'!")

    print("\nLet's set the range of numbers:")

    attempts  = 0

    lower = int(input("Lower limit: "))
    upper = int(input("Upper limit: "))

    random_number = random.randint(lower, upper)

    repeat = True
    while repeat == True:
        attempts += 1
        repeat = play_game(lower, upper, random_number, attempts)

    repeat_game()


main()
