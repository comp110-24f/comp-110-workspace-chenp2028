"""This file will serve as the unit test for CQ 7"""

__author__ = "730747329"

from find_max import find_and_remove_max


def test_find_max() -> None:
    l1 = [1, 8, 2, 3, 3]
    assert find_and_remove_max(l1) == 8 and l1 == [1, 2, 3, 3]
    return None


def test_find_and_remove() -> None:
    l1 = [10, 9, 8, 7, 10]
    find_and_remove_max(l1)
    assert l1 == [9, 8, 7]
    return None


def test_edge_case() -> None:
    l1 = [7, 7, 7]
    find_and_remove_max(l1)
    assert l1 == []
    return None
