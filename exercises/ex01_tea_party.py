"""Tea Party Exercise"""

__author__ = "730747329"


""" This function will be calling the other functions"""


def main_planner(guests: int) -> None:
    teaBags = tea_bags(people=guests)
    treat = treats(ppl=guests)
    print("A cozy tea party for " + str(guests) + " people")
    print("Tea Bags: " + str(teaBags))
    print("Treats: " + str(treat))
    print("Cost: $" + str(cost(tea_count=teaBags, treat_count=treat)))
    return None


"This function will return the number of teabags "


def tea_bags(people: int) -> int:
    total = people * 2
    return total


""" This function will return the number of treat needed"""


def treats(ppl: int) -> int:
    total = int(1.5 * tea_bags(people=ppl))
    return total


"""This Function will return the total cost of the tea party"""


def cost(tea_count: int, treat_count: int) -> float:
    total = (0.5 * tea_count) + (0.75 * treat_count)
    return total


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
