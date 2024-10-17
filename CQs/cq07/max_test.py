"""This file will serve as the unit test for CQ 7"""

__author__ = "730747329"

from find_max import find_and_remove_max


def test_find_max() -> None:  # test case 1: making sure if returns the exptected value
    l1 = [1, 8, 2, 3, 3]
    assert find_and_remove_max(l1) == 8
    return None


def test_find_and_remove() -> None:  # test case 2: making sure it removes the max value
    l1 = [10, 9, 8, 7, 10]
    find_and_remove_max(l1)
    assert l1 == [9, 8, 7]
    return None


def test_edge_case() -> None:  # edge case: when there is only 1 int in the list
    l1 = [7]
    find_and_remove_max(l1)
    assert l1 == []
    return None
