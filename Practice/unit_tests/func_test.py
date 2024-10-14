def get_first(l1: list[str]) -> str:
    return l1[0]


def remove_first(l1: list[str]) -> None:
    l1.pop(0)
    return None


def get_and_remove_first(l1: list[str]) -> str:
    first: str = l1[0]
    l1.pop(0)
    return first
