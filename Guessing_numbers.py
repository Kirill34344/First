import random


print("Welcome to the game 'Guess the number'!")


def main():

    lower, upper = get_number_range()

    play_game(lower, upper)

    repeat_game()


def is_valid(user_input, lower, upper):
    return user_input.isdigit() and lower <= int(user_input) <= upper


def get_number_range():
    while True:
        print("\nLet's set the range of numbers:")
        lower = int(input("Lower limit: "))
        upper = int(input("Upper limit: "))
        if lower >= upper:
            print("The lower limit must be less than the upper limit. Try again.")
            continue
        break
    return lower, upper


def play_game(lower, upper):

    random_number = random.randint(lower, upper)
    attempts  = 0
    print("Random number:", random_number)


    while True:

        user_input = (input(f"Please enter a number from {lower} to {upper}: "))

        if is_valid(user_input, lower, upper):
            attempts  += 1
            user_input = int(user_input)
            if user_input > random_number:
                print("Your number is higher than the guessed one, try again")
            elif user_input < random_number:
                print("Your number is less than the guessed one, try again")
            else:
                print(f"\nYou guessed it, congratulations! The hidden number: {random_number}")
                print(f"\nNumber of attempts: {attempts }\n")
                attempts  = 0
                break
        else:
            print(f"Please enter a number from {lower} to {upper}.")

    print("Thank you for playing the guess the number program.", end="\n\n")


def repeat_game():
    while True:
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay == "y":
            main()
            break
        elif replay == "n":
            print("Goodbye!")
            break
        else:
            print("Please enter 'y' to start a new game or 'n' to exit.")


main()


# Понять как работает маин
# Уменьшить количество вложенности