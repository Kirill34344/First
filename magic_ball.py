from random import choice

answers = [
    "Undoubtedly", "I think so", "It's unclear for now, try again", "Don't even think about it",
    "It's predetermined", "Most likely", "Ask later", "My answer is no",
    "No doubt about it", "Good prospects", "Better not tell you", "According to my data, no",
    "Definitely yes", "The signs say yes", "Cannot predict now", "The outlook isn't very good",
    "You can be sure of it", "Yes. Focus and ask again"
]


def ask_question_and_get_answer():
    input("Ask your question: ")
    print(choice(answers))


def should_repeat_game():
    user_input = input("Would you like to ask another question? (y/n): ").lower()
    if user_input == "y":
        ask_question_and_get_answer()
    elif user_input == "n":
        print("Come back, if you have any questions!")
        return False
    else:
        print("Please enter 'y' to new game or 'n' to exit.")
    return True


def main():
    print("Hello World, I am a magic ball and I know the answer to any question you have.")

    user_name = input("What is your name? ")

    print(f"Hello, {user_name}!")

    ask_question_and_get_answer()

    repeat = True
    while repeat == True:
        repeat = should_repeat_game()


main()