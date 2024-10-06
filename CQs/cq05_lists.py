"""Mutating functions."""

__author__ = "730747329"


def manual_append(l1: list[int], num: int) -> None:
    """This function will mutate a list by appending"""
    l1.append(num)
    return None


def double(l1: list[int]) -> None:
    """This function go double every item in the list"""
    i = 0
    while i < len(l1):
        l1[i] = l1[i] * 2
        i = i + 1
    return None


list_1: list[int] = [1, 2, 3]

list_2: list[int] = list_1  # changing 1 would change 2

double(list_2)  # double the list

# would print the same list
print(list_1)
print(list_2)
