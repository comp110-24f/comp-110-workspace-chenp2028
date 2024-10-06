"""This program will model the Wordle game"""

__author__ = "730747329"


def input_guess(length: int) -> str:
    """Checks and make sure the guess length is equal to the secret word length"""
    check: bool = True

    while check:
        word: str = input("Enter a " + str(length) + " character word: ")

        if length == len(word):
            print(word)
            check = False  # break when false
        else:
            word = input("That wasn't " + str(length) + " chars! Try again: ")
            if length == len(word):
                check = False  # break when false

    return word  # type: ignore # returning the word


def contains_char(word: str, char: str) -> bool:
    """This function will check if a char exist in a function"""
    assert len(char) == 1
    match: bool = False
    i: int = 0  # count index

    while i < len(word):
        if char == word[i]:
            match = True
        i += 1
    return match


def emojified(guess: str, word: str) -> str:
    "This function will print out emojis to represent accuracy"
    assert len(guess) == len(word)

    # colored squares
    white: str = "\U00002B1C"
    green: str = "\U0001F7E9"
    yellow: str = "\U0001F7E8"

    output: str = ""  # output string
    i: int = 0  # indexing

    while i < len(guess):
        if guess[i] == word[i]:
            output += green
        elif contains_char(word, guess[i]):
            output += yellow
        else:
            output += white

        i = i + 1

    return output


def main(word: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1  # counting turns
    cont: bool = True  # status of game

    while cont:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(word))  # guess input

        if guess == word:  # if guess mataches secret word
            print(emojified(guess, word))
            print(f"You won in {turn}/6 turns!")
            cont = False
        elif turn == 6:  # when the user run out of turns
            print("X/6 - Sorry, try again tomorrow!")
            cont = False
        else:  # keep going until the word is guessed
            print(emojified(guess, word))
            turn += 1
    return None


if __name__ == "__main__":
    main(word="codes")  # calling the main() function
