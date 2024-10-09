"""list Utility Functions"""

__author__ = "730747329"


def all(list1: list[int], num: int) -> bool:
    """Checking to make sure everything item in the list is equal to the number"""
    result: bool = True  # used to determine if the item and number is different or not
    i: int = 0  # the count variable

    if len(list1) == 0:  # if the list is empty
        result = False  # result becomes false if the list is empty

    while (
        i < len(list1) and result
    ):  # while the count variable is less than the list length and result is true
        if list1[i] != num:  # false if the item and number doesn't equal
            result = False
        i += 1  # increasing count variable
    print(result)  # printing our result
    return result


def max(list1: list[int]) -> int:
    """This function will return the largest number in the list"""
    if len(list1) == 0:  # if the list is empty
        raise ValueError("max() arg is an empty List")
    else:  # otherwise do this
        max: int = list1[0]  # assuming the first number is largest
        i: int = 0  # count variable

        while i < len(list1):  # while i is less than the list length
            if list1[i] > max:
                max = list1[i]  # updates max if the next item is greater
            i += 1  # increasing count variable
        print(max)  # print max
        return max


def is_equal(l1: list[int], l2: list[int]) -> bool:
    """This function checkts if element at every index is equal"""
    result: bool = True  # use to see if the items are the same
    i: int = 0  # count variable

    if len(l1) == len(l2):  # checking to make sure the length is the same
        while i < len(l1):
            if l1[i] != l2[i]:
                result = (
                    False  # result becomes false if the items doesn't match each other
                )
            i += 1  # increasing count variable
    else:  # if length is differnt, result is false
        result = False

    return result


def extend(l1: list[int], l2: list[int]) -> None:
    """This function will mutate the first list by append list 2 to it"""
    i: int = 0  # count variable

    while i < len(l2):  # loop throught list 2
        l1.append(l2[i])  # appends a item to list 1
        i += 1  # increasing count variable
    return None
