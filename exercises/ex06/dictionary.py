"""EX 06 Dictionary"""

__author__ = "730747329"


def invert(d1: dict[str, str]) -> dict[str, str]:
    """Inverse the diciontary where key and value is flipped in new dictionary"""
    new_dict: dict[str, str] = {}  # initializing a empty dictionary

    for i in d1:  # looping thru the input dict
        count = 0  # count variable for value occurance
        for (
            j
        ) in (
            d1
        ):  # looping thru the input dictionary again to check for duplicate values
            if d1[i] == d1[j]:
                count += 1  # increasing count by each time
        if count > 1:  # id duplicates exist, raise KeyError
            raise KeyError(
                "Dictionary can't be inversed! d1 contains duplicated values"
            )
        else:
            new_dict[d1[i]] = (
                i  # inverse and add to new dictionary if no duplicate values
            )

    print(new_dict)  # print inverse dictionary
    return new_dict


def favorite_color(d1: dict[str, str]) -> str:
    """Finding the color with the greatest occurance"""
    color: str = ""  # initializating empty string for favorite color
    count_color: dict[str, int] = (
        {}
    )  # initializating a new dict to count number of colors occurances
    max: int = 0  # initializating a max variable

    for i in d1:  # looping thru the input dictionary
        if d1[i] in count_color:
            count_color[
                d1[i]
            ] += 1  # increase the color occurance by if it exist in dictionary
        else:
            count_color[d1[i]] = 1  # create a new color item if not

    for i in count_color:  # finding the color with the highest occurance
        if max < count_color[i]:
            max = count_color[i]  # setting max to the greater color occurance
            color = i  # store the color in the color variable

    return color


def count(l1: list[str]) -> dict[str, int]:
    """Counting the item occurance in the input list"""
    d1: dict[str, int] = {}  # initializating a empty dictionary

    for i in l1:  # looping thru the input list
        if i in d1:
            d1[i] += 1  # increase the item occurance by 1 if it exists
        else:
            d1[i] = 1  # create a new item in dictionary if its the first time

    print(d1)

    return d1


def alphabetizer(l1: list[str]) -> dict[str, list[str]]:
    """Create a dictionary with key as the starting letter
    and value as words that start with that letter"""
    d1: dict[str, list[str]] = {}  # initializating an empty dictionary

    for i in l1:  # looping thru items in the list
        if i[0].lower() in d1:  # if the starting letter is already in the dict
            d1[i[0].lower()].append(i)  # append the word to the letter key
        else:
            d1[i[0].lower()] = [i]  # create a new key value pair if it's new

    print(d1)
    return d1


def update_attendance(d1: dict[str, list[str]], day: str, student: str) -> None:
    """Mutating the input list by updating attendence"""
    if day in d1:  # check to see if the day already exist in the dictionary
        for (
            i
        ) in (
            d1.values()
        ):  # looping thru the values to check if the student already exist
            if not (student in i):
                d1[day].append(
                    student
                )  # only append if the student does not exist and the day exist
    else:
        d1[day] = [student]  # create a new item if the day doesn't exist

    return None
