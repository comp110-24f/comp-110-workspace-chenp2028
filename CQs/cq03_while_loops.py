"""Challenge quetion 3 - While Loops"""

__author__ = "730747329"


def num_instances(phrase: str, search_char: str) -> int:
    count = 0  # number of char
    i = 0  # index number

    # loop through the phrase
    while len(phrase) > i:
        if phrase[i] == search_char:
            count = count + 1  # increasing count if found
        i = i + 1  # changing index
    print(count)  # printing count
    return count


num_instances(phrase="HelloHeLloHEllo", search_char="a")
