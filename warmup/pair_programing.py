""" Dictionary flipping demo """
from json import dumps

"""
Function to flip dictionaries
"""


def flip(d: dict[str, int | list]) -> dict[int, str]:
    fd = dict()
    for key, value in d.items():
        if isinstance(value, list):
            fd.update(flip(value[1]))
            value = value[0]
        if value in fd:
            fd[value] += f", {key}"
        else:
            fd[value] = key
    return fd


if __name__ == "__main__":
    d1 = {
        "Paul": 1942,
        "John": 1940,
        "George": 1943,
        "Ringo": 1940
    }
d2 = {
    "Paul": [1942, {
        "Heather McCartney": 1962,
        "Mary McCartney": 1969,
        "Stella McCartney": 1971,
        "James McCartney": 1977,
        "Beatrice McCartney": 2003
    }],
    "John": [1940, {"Julian Lennon": 1963,
                    "Kyoko Chan Cox": 1963,
                    "Sean Lennon": 1975}],
    "George": [1943, {"Dhani Harrison": 1978}],
    "Ringo": [1940, {
        "Zak Starkey": 1965,
        "Jason Starkey": 1967,
        "Lee Starkey": [1970, {"Smokey": 2009, "Jakamo": 2009, "Ruby Tiger":
                               2009}]}]
}
print(dumps(flip(d1), indent=4, sort_keys=True))
print(dumps(flip(d2), indent=4, sort_keys=True))
