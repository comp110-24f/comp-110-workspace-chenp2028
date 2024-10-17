"""Find and remove max function file for CQ 7"""

__author__ = "730747329"


def find_and_remove_max(l1: list[int]) -> int:

    if len(l1) == 0:  # return -1 if the list is empty
        return -1

    max = l1[0]  # setting max to the first item in the list
    for i in range(1, len(l1)):  # looping thru the list
        if l1[i] > max:
            max = l1[i]  # updates max if the item is greater
    print(max)  # print out max

    i = 0  # count variable
    while i < len(l1):  # looping thru the list
        if max == l1[i]:
            l1.pop(i)  # removing the max value
        else:
            i += 1  # increase count by 1 if the item is not removed

    return max  # return max
