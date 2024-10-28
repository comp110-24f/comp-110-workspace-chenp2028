"""EX 06 Dictionary"""

__author__ = "730747329"


def invert(d1: dict[str, str]) -> dict[str, str]:
    """Inverse the diciontary where key and value is flipped in new dictionary"""
    new_dict: dict[str, str] = {}

    # add to new dict first, check to make sure the next value doesn't exist as a ket
    # check before adding

    for i in d1:
        count = 0
        for j in d1:
            if d1[i] == d1[j]:
                count += 1
        if count > 1:
            raise KeyError(
                "Dictionary can't be inversed! d1 contains duplicated values"
            )
        else:
            new_dict[d1[i]] = i

    print(new_dict)
    return new_dict


def favorite_color(d1: dict[str, str]) -> str:
    color = ""
    count_color = {}
    max = 0

    for i in d1:
        if d1[i] in count_color:
            count_color[d1[i]] += 1
        else:
            count_color[d1[i]] = 1

    for i in count_color:
        if max < count_color[i]:
            max = count_color[i]
            color = i

    return color


def count(l1: list[str]) -> dict[str, int]:
    d1 = {}

    for i in l1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1

    print(d1)

    return d1


def alphabetizer(l1: list[str]) -> dict[str, list[str]]:
    d1 = {}

    for i in l1:  # looping thru items in the list
        if i[0].lower() in d1:  # if the starting letter is already in the dict
            d1[i[0].lower()].append(i)  # append the word to the letter key
        else:
            d1[i[0].lower()] = [i]  # create a new key value pair if it's new

    print(d1)
    return d1


def update_attendance(d1: dict[str, list[str]], day: str, student: str) -> None:
    if day in d1:
        d1[day].append(student)
    else:
        d1[day] = [student]
    return None
