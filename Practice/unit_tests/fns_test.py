"""Testing functions in func test file"""

from func_test import get_first, remove_first


def test_get_first() -> None:
    assert get_first(l1=["A", "B", "C"]) == "A"


def tset_remove_first() -> None:
    l0: list[str] = ["A", "B", "C"]
    remove_first(l0)
    assert l0 == ["B", "C"]
