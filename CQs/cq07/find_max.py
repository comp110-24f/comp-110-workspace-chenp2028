"""Find and remove max function file for CQ 7"""

__author__ = "730747329"


def find_and_remove_max(l1: list[int]) -> int:
    max = 0

    if len(l1) == 0:
        max = -1
        print(max)
        return max

    elif len(l1) == 1:
        max = l1[0]
        l1.pop(0)
        print(max)
        return max
    else:
        for i in l1:
            if i > max:
                max = i
        print(max)

        i = 0
        while i < len(l1):
            if max == l1[i]:
                l1.pop(i)
            i += 1
        if max == l1[0]:
            l1.pop(0)

        return max
