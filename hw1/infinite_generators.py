"""
Author: Daniel Stone

Filename: infinite_generators.py

File Description: Produce two infinite generators. The first once generates a fibonacci sequence,
while the second generates a "look-say" sequence, where the numbers you read and say aloud are
printed in the next sequence.

For example, 1 -> "one 1" -> 11 -> "two ones" -> 21 -> one two and one one -> 1211

Help: Help from Chat GPT debugging conditions for while loop and location of yield statement in look_say()
"""
from typing import Generator

def fibonacci(n: int = None) -> Generator[int, None, None]:
    """
    Generates infinite fibonacci sequence.
    
    Arguments: 
                n is an optional argument for the number of terms to be generated

    Yields: 
                int: next number in the fibonacci sequence
    """
    n1, n2 = 0, 1
    count = 0

    while n is None or count < n:

        yield n1
        n1, n2 = n2, n1 + n2
        count += 1



def look_say(n: int = None) -> Generator[int, None, None]:
    """
    Generates infitine look-say sequence.

    Arguments:
                n is an optional argument for the number of terms to be generated

    Yields: 
                int: next number in the fibonacci sequence

    Example:
                1, 11, 21, 1211, 111221, and so on
"""
    loop_counter = 0 # counter for how many terms need to be generated
    num = "1" # current value in sequence

    while n is None or loop_counter < n:

        yield int(num)
        num_counter = 1 # counter for current letter
        last_char = num[0] # stores previous value of num string
        ans = "" # working value to concatenate values as num is iterated over

        # iterate over current num, starting at second character in the string
        for current_char in num[1:]:
            if current_char == last_char:
                num_counter += 1 # increment counter is current_char same as last_char
            else:
                ans += str(num_counter) + last_char # append counter of character and character to ans
                num_counter = 1 # reset counter for the next letter
            last_char = current_char #update last_char

        ans += str(num_counter) + last_char # append last counter of character and character to ans
        num = ans # update num
        loop_counter += 1 # increment while loop counter

assert list(fibonacci(10)) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
assert list(fibonacci(-1)) == []
assert list(fibonacci(0)) == []
assert list(fibonacci(1)) == [0]
assert list(fibonacci(2)) == [0, 1]

assert list(look_say(10)) == [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, 31131211131221, 13211311123113112211]
assert list(look_say(-1)) == []
assert list(look_say(0)) == []
assert list(look_say(1)) == [1]
assert list(look_say(2)) == [1, 11]
