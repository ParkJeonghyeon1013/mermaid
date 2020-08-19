class mini2_NPC():
    def __init__(self,name,win2,lose2,ai_num):
        self.name = name
        self.ai_num = ai_num
        self.win2 = win2
        self.lose2 = lose2
        
    def children_win(self):
        self.win2 += 1
        
    # 애가 져서 기분 나빠짐
    def children_lose(self):
        self.lose2 += 1
        


"""class Character:
    #hp = 0
    #mp = 0
    #ad = 0
    #dp = 0
    #nowhp = hp
    #nowmp = mp

    def __init__(self,name,hp,ad,dp):
        self.name = name
        self.hp = hp
        self.ad = ad
        self.dp = dp
        self.nowhp = hp

    def att(self, character):
        if character.dp >= self.ad:
            character.nowhp -= 1
            print("-1!!!")
        else:
            character.nowhp -= self.ad - character.dp
            print(f"-{self.ad - character.dp}!!!")"""
