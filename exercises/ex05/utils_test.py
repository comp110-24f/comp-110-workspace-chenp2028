"""This file will contain the unit tests"""

__author__ = "730747329"

from utils import only_evens, sub, add_at_index
import pytest

# only_evens test cases


def test_evens_return() -> None:
    """Test the right output"""
    assert only_evens([1, 2, 3, 4]) == [2, 4]  # only evens is returned
    return None


def test_evens_mutate() -> None:
    """Make sure list is not mutated"""
    l1 = [1, 2, 3, 4]
    only_evens(l1)
    assert l1 == [1, 2, 3, 4]  # listed is not mutated after calling
    return None


def test_evens_edge() -> None:
    """Edge case for only evens function: list containing only 1 element"""
    assert only_evens([1]) == []  # return [] when only element is odd
    return None


# sub test cases


def test_sub_return() -> None:
    """Testing the return value"""
    assert sub([1, 2, 3, 4], 0, 3) == [1, 2, 3]  # correct subset should be returned
    return None


def test_sub_mutate() -> None:
    """Making sure sub does not mutate the input list"""
    list1 = [1, 2, 3, 4]
    sub(list1, 0, 2)
    assert list1 == [1, 2, 3, 4]  # input list is not mutated after calling sub
    return None


def test_sub_edge() -> None:
    """Edge case for sub function: list containing only 1 element"""
    assert sub([1], 0, 1) == [1]  # return [1] when there is only 1 element in list
    return None


# add_at_index test cases


def test_add_mutate_return() -> None:
    """Making sure the list is correctly mutated"""
    list1 = [1, 2, 3, 4]
    add_at_index(list1, 0, 1)
    assert list1 == [
        1,
        0,
        2,
        3,
        4,
    ]  # making sure list is correctly mutated after calling


def test_add_edge() -> None:
    """Edge case for add_in_index funcion: adding at index 0"""
    list1 = [1, 2, 3, 4]
    add_at_index(list1, 0, 0)
    assert list1 == [0, 1, 2, 3, 4]  # 0 is added to index 0
    return None


def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    list1 = [1, 2, 3, 4]
    with pytest.raises(IndexError):
        add_at_index(list1, 0, 6)
        # an IndexError is raised for the case when the add_at_index
        # is given an index that is greater than the length of our <list_object>
