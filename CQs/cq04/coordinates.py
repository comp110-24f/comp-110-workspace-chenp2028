"""This is a file in CQ 04"""

__author__ = "730747329"


def get_coords(xs: str, ys: str) -> None:
    i = 0
    j = 0
    while i < len(xs):

        while j < len(ys):
            print(f"({xs[i]}, {ys[j]})")
            j = j + 1
        j = 0
        i = i + 1
