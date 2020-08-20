class Mermaid ():
    def __init__(self, name, HP, DP, coin, kill):
        self.name = "박"
        self.HP = 100
        self.DP = 5
        self.coin = 0
        self.kill = 0

mermaid = Mermaid("박", 100, 5, 0, 0)

"""
class character:
    #hp = 0
    #mp = 0
    #ad = 0
    #dp = 0
    #nowhp = hp
    #nowmp = mp


def att(self, character):
        if character.dp >= self.ad:
            character.nowhp -= 1
            print("-1!!!")
        else:
            character.nowhp -= self.ad - character.dp
            print(f"-{self.ad - character.dp}!!!")
"""
