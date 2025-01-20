def foo(*x: int) -> int: 
    """returns the sum of all args"""
    return sum(x)



print(foo(1,2))
print(foo(1,2,3))
print(foo(1 ,2, 3, 4, 5, 6, 7))