"""This file will implement some more list utility functions"""

__author__ = "730747329"


def only_evens(l1: list[int]) -> list:
    """Returns a list with only even elements"""
    evenList: list[int] = []  # create an empty list

    for i in l1:  # looping thru the input list
        if i % 2 == 0:  # append the element if its even
            evenList.append(i)
    print(evenList)  # print even list
    return evenList  # return even list


def sub(l1: list[int], start: int, end: int) -> list:
    """Return a subset of list using known start and end index"""
    subList: list[int] = []  # create an empty list

    if start < 0:  # set start index to 0 if it's negative
        start = 0
    if end > len(l1):  # set end index to length of the list if it's greater than that
        end = len(l1)

    if (
        len(l1) == 0 or start >= len(l1) or end <= 0
    ):  # return empty list if the conditions are met
        print(subList)  # print empty list
        return subList

    for i in range(
        start, end
    ):  # looping thru the list using known start and end index. end is inconclusive
        subList.append(l1[i])  # appending element to subList

    print(subList)  # print out sub list
    return subList


def add_at_index(l1: list[int], element: int, index: int) -> None:
    """Modify the input lsit to place the element at given index"""

    if index < 0 or index > len(l1):  # raise Index out of bound error
        raise IndexError("Index is out of bounds for the input list")
    else:
        l1.append(0)  # appending a placeholder to the end of the list
        for i in range(index, len(l1) - 1):  # starting at 0 and end at
            num = l1[i]
            l1[i + 1] = num

        l1[index] = element

    return None
