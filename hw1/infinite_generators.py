"""
Author: Daniel Stone

Filename: infinite_generators.py

File Description: Produce two infinite generators. The first once generates a fibonacci sequence,
while the second generates a "look-say" sequence, where the numbers you read and say aloud are
printed in the next sequence.

For example, 1 -> "one 1" -> 11 -> "two ones" -> 21 -> one two and one one -> 1211
"""
from typing import Generator

def fibonacci(*args) -> Generator(int, None, None):
    """
    Generates infinite fibonacci sequence.
    
    Arguments: 
                *args is an optional argument for the number of terms to be generated

    Yields: 
                int: next number in the fibonacci sequence
    """
    #code here

def look_say(*args) -> Generator(int, None, None):
    """
    Generates infitine look-say sequence.

    Arguments:
                *args is an optional argument for the number of terms to be generated

    Yields: 
                int: next number in the fibonacci sequence

    Example:
                1, 11, 21, 1211, 111221, and so on

    """
    #code here