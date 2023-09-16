import random


class Player:
    name = None
    symbol = None
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol



class User(Player):
    def __init__(self, sumbol : str):
        self.symbol = sumbol

    def set_name(self, name):
        self.name = name


class II(Player):
    name = "Бот"
    def __init__(self, sumbol : str):
        self.symbol = sumbol
    
    def step(maps:list):
        n = []
        for i in maps:
            if(type(i) == int):
                n.append(i)
        return random.choice(n)
    