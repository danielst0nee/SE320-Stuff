"""Practice game"""


class Game:
    """a simple game for players"""

    def __init__(self, *args) -> None:
        """initialize Game"""
        self.players = args

    def __str__(self) -> None:
        """print player names"""
        result = ""
        for i, name in enumerate(self.players, start=1):
            result += f"{i}. {name}\n"
        return result

    def __len__(self) -> int:
        """returns the number of players"""
        return len(self.players)

    def __eq__(self, __o) -> bool:
        return self.players == __o.players


g = Game("Amy", "Bob", "Joel", "Ann")
print(g)
print(len(g))

w = Game("Amy", "Bob", "Joel", "Ann")
print(g == w)
