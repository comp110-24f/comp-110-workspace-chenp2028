"""Challenge question 2: Conditionals"""

__author__ = "730747329"


def guess_a_number() -> None:
    secret: int = 7
    x: int = int(input("Guess a number:"))
    print("Your guess was " + str(x))

    if secret == x:
        print("You got it!")
    elif secret > x:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
