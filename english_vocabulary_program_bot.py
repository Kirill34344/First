import random

class Words:
    def __init__(self):
        self.__words = ["a", "b", "c", "d", "f"]


    def add_words(self, user_input_words):
        self.__words.append(user_input_words)


    def get_random_elements(self, k):
        n = len(self.__words)
        arr_copy = self.__words[:]
        result = []

        for i in range(k):
            index = int(random.random() * (n - i))
            result.append(arr_copy[index])
            arr_copy[index], arr_copy[n - i - 1] = arr_copy[n - i - 1], arr_copy[index]

        return result


def repeat_func(w, k):
    repeat = input("Do you want to enter another word (y), view 5 words (v), or end game (n)? ")
    if repeat == "y":
        user_input_repeat = int(input("How many words do you want to enter: "))
        for _ in range(user_input_repeat):
            user_input_words = input("Enter the word: ")
            w.add_words(user_input_words)
    elif repeat == "v":
        result = w.get_random_elements(k)
        print("Random words:", result)
    elif repeat == "n":
        print("Come back again!")
        return False
    else:
        print("Invalid input. Please enter 'y', 'v', or 'n'.")
    return True


def main():
    print("Welcome to the English vocabulary program!")
    k = 5
    w = Words()
    user_input_repeat = int(input("How many words do you want to enter: "))
    for _ in range(user_input_repeat):
        user_input_words = input("Enter the word: ")
        w.add_words(user_input_words)


    repeat = True
    while repeat:
        repeat = repeat_func(w, k)


if __name__ == "__main__":
    main()
