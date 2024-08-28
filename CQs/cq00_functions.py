"""CQ00 - Functions Practice"""

__author__ = "730747329"

"""This function will just take your input and repeat it back to you"""


def mimic(message: str) -> str:
    return message


""" The main function will call other functions"""


def main() -> None:
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
