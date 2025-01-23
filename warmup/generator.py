from typing import Generator


def foo() -> Generator[int, None, None]:  # first is type return, second is type yielding, third is type sending to generator
    x = 2
    for i in range(10):
        x += 2
        yield x


for i in foo():
    print(i)
