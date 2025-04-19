import random


def user_input(array):
    user_input_repeat = int(input("How much do you enter the word: "))
    for _ in range(user_input_repeat):
        user_input_words = (input("Enter the word: "))
        array.append(user_input_words)


def repeat_func(array, k):
    repeat = input("do you want to enter another word or view 5 words or end game? (y/v/n): ")
    if repeat == "y":
        user_input(array)
    elif repeat == "v":
        get_random_elements(array, k)
    elif repeat == "n":
        print("come back")
        return False
    else:
        print("Please enter 'y' to new game or 'n' to exit.")
    return True


def get_random_elements(arr, k):
    n = len(arr)
    result = []

    for i in range(k):
        index = int(random.random() * (n - i))
        result.append(arr[index])
        arr[index], arr[n - i - 1] = arr[n - i - 1], arr[index]
    print(result)


def main():
    print("Welcome to the English vocabulary program!")

    array = ["a", "b", "c", "d", "f"]
    k = 5

    user_input(array)

    repeat = True
    while repeat == True:
        repeat = repeat_func(array, k)


main()
