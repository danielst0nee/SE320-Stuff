"""
Introduction Part 2
Functions/imports
"""

from random import randint
from utils import age

def roll_the_dice() -> int:
    return randint(1, 6)


def add(x: int, y: int) -> int:
    return x + y


my_list = []
for i in range(6):
    my_list.append(roll_the_dice())

# dictionaries
# collection of key value pairs, key is an immutable type

d = {"a": 20, "b": 40, "x": 99, "c": 17}

print(d.setdefault("q", -1))

print(d.get("q", "Not in the dictionary yet"))
print(d["b"])
print()

d1 = {"name": "John", "age": 37, "kids": 3}
d2 = {"name": "George", "age": 32, "kids": 1}
d3 = {"name": "Paul", "age": 35, "kids": 2}
d4 = {"name": "Ringo", "age": 38, "kids": 3}



band = [d1, d2, d3, d4]
print(sorted(band, key=age))#
print(sorted(band, key=lambda a: a.get("age")))


# if key doesn't exist, we can use a default
