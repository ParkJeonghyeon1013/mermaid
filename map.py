#Map에서 어디로 갈지 물어본
def choose():
    map_num = 0
    stage_1 = "1 - 미역 공장 가본다"
    stage_2 = "2 - 진주 가게에 가본다"
    stage_3 = "3 - 약쟁이 소라게에게 가본다"
    
    while True:
        map_num = int(input("어디를 가볼까요?\n%s\n%s\n%s\n"%(stage_1,stage_2,stage_3)))
        if map_num == 1:
            break
        elif map_num == 2:
            break
        elif map_num == 3:
            break
        else:
            print("다시 입력해주세요")
            continue
    print(map_num)
    return(map_num)

def seaweed(a,b):
    print(a,b + "미역")
    return 0

def pearl(a,b):
    print(a,b + "진주")
    return 0
    
def full_map(self):
    print("어딜 가볼까요?")
    print("1 - 미역 공장 가본다\n2 - 진주 가게에 가본다\n3 - 약쟁이 소라게에게 가본다")
        
choose()

