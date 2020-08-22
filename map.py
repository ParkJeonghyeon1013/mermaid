# Map 에서 어디로 갈지 물어본
def choose(stage):
    stage_1 = "미역 공장 가본다"
    stage_2 = "진주 가게에 가본다"
    stage_3 = "약쟁이 소라게에게 가본다"

# 첫번째 선택
    if stage == 0:
        while True:
            num = str(input("첫 출발, 어디를 가볼까요?\n1- %s\n2- %s\n3- %s\n" % (stage_1, stage_2, stage_3)))
            if num == '1' or num == '2' or num == '3':
                return num
            else:
                print("다시 선택해주세요")
                continue

# 두번째 선택 (진주/소라게)
    elif stage == 1:
        while True:
            num = str(input("어디를 가볼까요?\n1- %s\n2- %s\n" % (stage_2, stage_3)))
            if num == '1' or num == '2':
                return num
            else:
                print("다시 선택해주세요")
                continue

# 두번째 선택 (미역/소라게)
    elif stage == 2:
        while True:
            num = str(input("어디를 가볼까요?\n1- %s\n2- %s\n" % (stage_1, stage_3)))
            if num == '1' or num == '2':
                return num
            else:
                print("다시 선택해주세요")
                continue

# 세번째 선택 (미역/진주)
    elif stage == 3:
        while True:
            num = str(input("어디를 가볼까요?\n1- %s\n2- %s\n" % (stage_1, stage_2)))
            if num == '1' or num == '2':
                return num
            else:
                print("다시 선택해주세요")
                continue
