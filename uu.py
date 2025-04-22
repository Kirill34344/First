import random

class Words:
    def __init__(self):
        self.__array = ["a", "b", "c", "d", "f"]


    def main(self):
        print("Welcome to the English vocabulary program!")

        k = 5

        self.user_input()

        repeat = True
        while repeat == True:
            repeat = self.repeat_func(k)


    def user_input(self):
        user_input_repeat = int(input("How much do you enter the word: "))
        for _ in range(user_input_repeat):
            user_input_words = (input("Enter the word: "))
            self.__array.append(user_input_words)


    def repeat_func(self, k):
        repeat = input("do you want to enter another word or view 5 words or end game? (y/v/n): ")
        if repeat == "y":
            self.user_input()
        elif repeat == "v":
            self.get_random_elements(k)
        elif repeat == "n":
            print("come back")
            return False
        else:
            print("Please enter 'y' to new game or 'n' to exit.")
        return True


    def get_random_elements(self, k):
        n = len(self.__array)
        arr_copy = self.__array[:]
        result = []

        for i in range(k):
            index = int(random.random() * (n - i))
            result.append(arr_copy[index])
            arr_copy[index], arr_copy[n - i - 1] = arr_copy[n - i - 1], arr_copy[index]
        print(result)


if __name__ == "__main__":
    w = Words()
    w.main()
