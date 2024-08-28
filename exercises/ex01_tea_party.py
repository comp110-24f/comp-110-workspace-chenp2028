"""Tea Party Exercise"""

__author__ = "730747329"


def main_planner(guests: int) -> None:
    """The main_planner function will be the entrypoint of your program"""

    # teaBags = tea_bags(people=guests)
    # treat = treats(ppl=guests)
    print("A cozy tea party for " + str(guests) + " people")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(ppl=guests)))
    print(
        "Cost: $"
        + str(cost(tea_count=tea_bags(people=guests), treat_count=treats(ppl=guests)))
    )
    return None


def tea_bags(people: int) -> int:
    """The tea_bags function will return the number of teabags"""

    return people * 2


def treats(ppl: int) -> int:
    """The treats function will return the number of treat needed"""

    return int(1.5 * tea_bags(people=ppl))


def cost(tea_count: int, treat_count: int) -> float:
    """The cost Function will return the total cost of the tea party"""

    return (0.5 * tea_count) + (0.75 * treat_count)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
