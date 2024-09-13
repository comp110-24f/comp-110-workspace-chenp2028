"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730747329"


# this function will check and make the word has 5 characters
def input_word() -> str:
    word: str = input("Enter a 5-character word: ")

    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # exitting the program early
        print("'" + word + "'")
    else:
        print("'" + word + "'")
    return word


# check and make sure only one character is inputted
def input_letter() -> str:
    letter: str = input("Enter a single character: ")

    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # exiting the program early
        print("'" + letter + "'")
    else:
        print("'" + letter + "'")

    return letter


# calls the input_word and input_letter to make the wordle work
def contains_char(word: str = input_word(), letter: str = input_letter()) -> None:
    print("Searching for " + letter + " in " + word)
    i = 0  # index checker
    count = 0  # instance counter

    # loops through the word to check each index
    while len(word) > i:
        if letter == word[i]:
            print(letter + " found at index " + str(i))
            count = count + 1
        i = i + 1
    # Printing out the instances
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)

    return None


# calling the contains_char()
def main():
    contains_char()


# calls the main()
if __name__ == "__main__":
    main()
