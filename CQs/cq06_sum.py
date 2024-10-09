"""Summing the elements of a list using different loops"""

__author__ = "730747329"


def w_sum(vals: list[float]) -> float:
    sum: float = 0.0  # initalize sum as 0.0
    i: int = 0  # count variable

    while i < len(vals):
        sum += vals[i]  # add each item value to sum
        i += 1  # increase count variable by 1
    return sum


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0  # initalize sum as 0.0

    for i in vals:  # loop thru each item in list
        sum += i  # added each item value to sum
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0  # initalize sum as 0.0

    for i in range(0, len(vals)):  # starting at zero and ending at len(vals)-1
        sum += vals[i]  # adding each item value of sum
    return sum
