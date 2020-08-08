#Map에서 어디로 갈지 물어본
def choose(stage):
    num=1
    stage_1 = "1 - 미역 공장 가본다"
    stage_2 = "2 - 진주 가게에 가본다"
    stage_3 = "3 - 약쟁이 소라게에게 가본다"
#첫번째 선택
    if stage == 0:
        num = str(input("어디를 가볼까요?\n%s\n%s\n%s\n"%(stage_1,stage_2,stage_3)))
        print(num)
#두번째 선택 (진주/소라게)
    elif stage == 1:
        num = str(input("어디를 가볼까요?\n%s\n%s\n"%(stage_2,stage_3)))
        print(num)
#두번째 선택 (미역/소라게)
    elif stage == 2:
        num = str(input("어디를 가볼까요?\n%s\n%s\n"%(stage_1,stage_3)))
        print(num)
#세번째 선택 (미역/진주)
    elif stage == 3:
        num = str(input("어디를 가볼까요?\n%s\n%s\n"%(stage_1,stage_2)))
        print(num)
    
    return num


def seaweed(a,b):
    print(a,b + "미역")
    return 0

def pearl(a,b):
    print(a,b + "진주")
    return 0
    
def full_map(self):
    print("어딜 가볼까요?")
    print("1 - 미역 공장 가본다\n2 - 진주 가게에 가본다\n3 - 약쟁이 소라게에게 가본다")


