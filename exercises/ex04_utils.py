"""list Utility Functions"""

__author__ = "730747329"


def all(list1: list[int], num: int) -> bool:
    """Checking to make sure everything item in the list is equal to the number"""
    result: bool = True
    i: int = 0

    while i < len(list1) and result:
        if list1[i] != num:
            result = False
        i += 1
    print(result)
    return result


def max(list1: list[int]) -> int:
    """This function will return the largest number in the list"""
    if len(list1) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        max: int = list1[0]  # assuming the first number is largest
        i: int = 0

        while i < len(list1):
            if list1[i] > max:
                max = list1[i]  # updates max if the next item is greater
            i += 1
        print(max)
        return max


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """This function checkts if element at every index is equal"""
    result: bool = True
    i: int = 0

    if len(l1) == len(l2):
        while i < len(l1):
            if l1[i] != l2[i]:
                result = False
            i += 1
    else:
        result = False

    return result


def extend(l1: list[int], l2: list[int]) -> None:
    """This function will mutate the first list by append list 2 to it"""
    i: int = 0

    while i < len(l2):
        l1.append(l2[i])
        i += 1
    return None
