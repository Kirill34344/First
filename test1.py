import random


def user_input(words):
    user_input_repeat = int(input("How much do you enter the word: "))
    for _ in range(user_input_repeat):
        user_input_words = (input("Enter the word: "))
        words.append(user_input_words)


def repeat_func(words):
    repeat = input("do you want to enter another word or view 5 words or end game? (y/v/n): ")
    if repeat == "y":
        user_input(words)
    elif repeat == "v":
        output_words(words)
    elif repeat == "n":
        print("come back")
        return False
    else:
        print("Please enter 'y' to new game or 'n' to exit.")
    return True


def output_words(words):
    number = random.random()
    for i in range(5):
        print(words[number])


def main():
    print("Welcome to the English vocabulary program!")

    words = ["a", "b", "c", "d", "f"]

    user_input(words)

    repeat = True
    while repeat == True:
        repeat = repeat_func(words)


main()