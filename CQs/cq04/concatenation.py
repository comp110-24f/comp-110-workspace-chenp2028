"""This is a file in CQ 04"""

__author__ = "730747329"


def concat(p1: str, p2: str) -> str:
    """This function will concat two strings"""
    output = p1 + p2
    print(output)
    return output


word1 = "happy"

word2 = "tuesday"
if __name__ == "__main__":
    concat(word1, word2)
