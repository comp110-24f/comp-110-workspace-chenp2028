"""This program will model the Wordle game"""

__author__ = "730747329"


def input_guess(length: int) -> str:
    """Checks and make sure the guess length is equal to the secret word length"""
    check = True

    while check:
        word = input("Enter a " + str(length) + " character word: ")

        if length == len(word):
            print(word)
            check = False
            # break
        else:
            word = input("That wasn't " + str(length) + " chars! Try again: ")

    return word


def contains_char(word: str, char: str) -> bool:
    """This function will check if a char exist in a function"""
    assert len(char) == 1
