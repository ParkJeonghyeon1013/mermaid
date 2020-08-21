from c1_character import mermaid
from c3_pearlshell import children
from minigame2 import rps, minigame2_1_att, minigame2_1_def, minigame2_2_att, minigame2_2_def, minigame2_3, shell_1, shell_2, shell_3


# Stage2 - 진주  가게에서 알바(자기 아이들을 돌봐달라는 것임)
def s2_intro(name):
    print("------------------------------------------------------------------------------\n")
    print("[진주 사장]: [%s] 인어 어서오세요~ 무슨 일로 왔죠?"%name)
    print("[%s] 인어: 알바 공지를 보고 왔는데요..\n"%name)
    print("[진주 사장]: 아이고, 잘왔어요!! 안그래도 기다리고 있었어요!")
    print("[%s] 인어: 혹시 무슨 일을 하면 될까요?"%name)
    input("\n------------------------------------------------------------------------------\n")
    print("[진주 사장]: 두 가지만 도와주면 돼요!\n1. 제가 잠시 진주 도매시장에 다녀오는 동안 이 아이들과 함께 놀아주세요.\n2. 매일 같이 찾아오는 골치아픈 이들을 좀 쫓아 내주세요!")
    input("\n------------------------------------------------------------------------------\n")    
    print("[%s] 인어: 아, 잠깐! 그럼 코인은 얼마나 줄 수 있는거죠?"%name)
    print("[진주 사장]: 기본적으로 50코인을 드릴게요! 대신 아이들을 잘 놀아주시면 20코인 더!")    
    print("[%s] 인어: 네~ 알겠습니다. 아이들 걱정말고 편히 다녀오세요!"%name)
    print("[미역 사장]: 그럼 믿고 갔다 올게요~")
    print("(미역 사장이 나간다) 딸랑~")
    input("\n------------------------------------------------------------------------------\n")    
    
# stage2(미니게임 1) - 청기백기 게임 / 통아저씨 게임
def s2_game1():
    print("<< 돌봐야 할 아이 [진주 아이]의 등장 >>")
    print("[진주 아이]: 안녕하세요??")
    print("[{0}] 인어: 네~ 안녕하세요? 부모님이 잠시 나간 동안 우리 재밌게 놀아봐요~".format(mermaid.name))
    print("[진주 아이]: 네!!!! 그럼 저랑 뭐하면서 노는 거예요?")
    input("\n------------------------------------------------------------------------------\n")
    print("[{0}] 인어: 흠,,, (주변에 보이는게 청기 백기와 통아저씨 게임이 있네요.\n무엇을 하며 놀아볼까요?".format(mermaid.name))

    # 진주아이와 할 게임 선택
    while True:
        play_num = str(input("1 - 청기 백기\n2 - 통아저씨 게임\n"))

        # 1(1) - 청기백기
        if play_num == '1':
            
            # 순서정하기 가위바위보
            print("\n------------------------------------------------------------------------------\n")
            print("청기백기 게임 규칙 설명\n")
            print("※ 소문자 'b'는 청기올려!, 소문자 'n'은 백기올려!\n※ 소문자 'bb'는 청기 내려!, 소문자 'nn'은 백기 내려! \n※ 3판2선승제로 진행 \n※ 1인당 5번의 공격이 진행되며 가장 적게 틀린 사람이 우승\n※ 3초 안에 알맞은 깃발을 들어야 함")
            print("\n그럼 게임을 시작해 볼까요?")
            input("\n------------------------------------------------------------------------------\n")
            print("[진주 아이]: 누가 먼저 할지 정해요!! 가위,바위,보!")
            who_1 = rps()

            # 아이 선공
            if who_1 == 1:
                flag_child = 0
                flag_mer = 0
                
                print("\n------------------------------------------------------------------------------\n")
                print("[진주 아이]: 그럼 저부터 공격 할게요!")
                
                for num1 in range(1, 4, 1):
                    
                    input("\n------------------------------------------------------------------------------\n")
                    print("{0}번째 판".format(num1))
                    p_1 = minigame2_1_def()
                    p_2 = minigame2_1_att()
                    input("\n------------------------------------------------------------------------------\n")

                    print("{0}번째 판 결과: [진주아이 - {1}점] [{2}인어 - {3}점]".format(num1, p_2, mermaid.name, p_1))

                    # 승점 비교 p1(인어) | p2(진주아이)
                    if p_1 < p_2:
                        flag_child += 1
                        print("[진주 아이]의 승리입니다!")
                        if flag_child == 2:
                            input("\n------------------------------------------------------------------------------\n")
                            print("[진주 아이]: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해요~")
                            children.children_win()
                            return 2
                        continue

                    elif p_1 > p_2:
                        flag_mer += 1
                        print("[{0}] 인어의 승리입니다!".format(mermaid.name))
                        if flag_mer == 2:
                            input("\n------------------------------------------------------------------------------\n")
                            print("[{0}] 인어: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해볼까요?".format(mermaid.name))
                            print("[진주 아이]: 이게 뭐예요... 애니깐 봐주고 그런거 없어요??ㅠㅠㅠ")
                            children.children_lose()
                            return 2
                        continue

                    elif p_1 == p_2:
                        print("{0}번째 판 결과, 무승부 입니다!".format(num1))
                        continue
                    break

            # 인어 선공
            elif who_1 == 2:
                flag_child = 0
                flag_mer = 0
                                
                print("\n------------------------------------------------------------------------------\n")
                print("[진주 아이]: 먼저 공격하세요!")
                                
                for num1 in range(1, 4, 1):

                    input("\n------------------------------------------------------------------------------\n")
                    print("{0}번째 판".format(num1))
                    p_1 = minigame2_1_att()
                    p_2 = minigame2_1_def()
                    input("\n------------------------------------------------------------------------------\n")

                    print("{0}번째 판 결과: [진주아이 - {1}점] [{2}인어 - {3}점]".format(num1, p_1, mermaid.name, p_2))

                    # 승점 비교 p1(진주아이) | p2(인어)
                    if p_1 > p_2:
                        flag_child += 1
                        print("[진주 아이]의 승리입니다!")
                        if flag_child == 2:
                            input("\n------------------------------------------------------------------------------\n")
                            print("[진주 아이]: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해요~")
                            children.children_win()
                            return 2
                        continue

                    elif p_1 < p_2:
                        flag_mer += 1
                        print("[{0}] 인어의 승리입니다!".format(mermaid.name))
                        if flag_mer == 2:
                            input("\n------------------------------------------------------------------------------\n")
                            print("[{0}] 인어: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해볼까요?".format(mermaid.name))
                            print("[진주 아이]: 이게 뭐예요... 애니깐 봐주고 그런거 없어요??ㅠㅠㅠ")
                            children.children_lose()
                            return 2
                        continue

                    elif p_1 == p_2:
                        print("{0}번째 판 결과, 무승부 입니다!".format(num1))
                        continue
                    break

        # 2(2) - 통아저씨 게임
        elif play_num == '2':
            print("\n------------------------------------------------------------------------------\n")
            print("통아저씨 게임 규칙 설명")
            print("※ 3판 2선승제\n※ 1~15의 숫자 중 하나를 선택해 통에 꽂힌 칼을 뽑습니다\n※ 칼을 뽑았을 때 통아저씨가 튀어오르면 지는 게임")
            input("\n------------------------------------------------------------------------------\n")
            print("[진주 아이]: 먼저 칼 뽑을 사람을 정해요!! 가위,바위,보!")
            who_2 = rps()

            # 아이 선공
            if who_2 == 1:
                flag_child = 0
                flag_mer = 0

                print("\n------------------------------------------------------------------------------\n")
                print("[진주 아이]: 그럼 저부터 뽑을 칼의 숫자를 고를게요!")

                for num1 in range(1, 4, 1):

                    print("\n------------------------------------------------------------------------------\n")
                    print("{0}번째 판".format(num1))

                    # 1,3에선 진주 아이부터 | 2에선 인어부터
                    if num1 == 1 or num1 == 3:
                        play = minigame2_2_def()
                        input("\n------------------------------------------------------------------------------\n")
                        print("{0}번째 판 결과: [{1}] 승리".format(num1, play))

                        if play == mermaid.name:
                            flag_mer += 1
                            if flag_mer == 2:
                                print("[{0}] 인어: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해볼까요?".format(mermaid.name))
                                print("[진주 아이]: 이게 뭐예요... 애니깐 봐주고 그런거 없어요??ㅠㅠㅠ")
                                children.children_lose()
                                return 1

                        elif play == children.name:
                            flag_child += 1
                            if flag_child == 2:
                                print("[진주 아이]: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해요~")
                                children.children_win()
                                return 1

                        continue

                    elif num1 == 2:
                        play = minigame2_2_att()
                        input("\n------------------------------------------------------------------------------\n")
                        print("{0}번째 판 결과: [{1}] 승리".format(num1, play))

                        if play == mermaid.name:
                            flag_mer += 1
                            if flag_mer == 2:
                                print("[{0}] 인어: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해볼까요?".format(mermaid.name))
                                print("[진주 아이]: 이게 뭐예요... 애니깐 봐주고 그런거 없어요??ㅠㅠㅠ")
                                children.children_lose()
                                return 1

                        elif play == children.name:
                            flag_child += 1
                            if flag_child == 2:
                                print("[진주 아이]: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해요~")
                                children.children_win()
                                return 1

                        continue

            # 인어 선공
            elif who_2 == 2:
                flag_child = 0
                flag_mer = 0

                print("\n------------------------------------------------------------------------------\n")
                print("[진주 아이]: 뽑을 칼의 숫자를 먼저 선택하세요!")

                for num1 in range(1, 4, 1):

                    print("\n------------------------------------------------------------------------------\n")
                    print("{0}번째 판".format(num1))

                    # 1,3에선 인어부터 | 2에선 진주 아이부터
                    if num1 == 1 or num1 == 3:
                        play = minigame2_2_att()
                        input("\n------------------------------------------------------------------------------\n")
                        print("{0}번째 판 결과: {1} 승리".format(num1, play))

                        if play == mermaid.name:
                            flag_mer += 1
                            if flag_mer == 2:
                                print("")
                                children.children_lose()
                                return 1

                        elif play == children.name:
                            flag_child += 1
                            if flag_child == 2:
                                print("[진주 아이]: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해요~")
                                children.children_win()
                                return 1

                        continue

                    elif num1 == 2:
                        play = minigame2_2_def()
                        input("\n------------------------------------------------------------------------------\n")
                        print("{0}번째 판 결과: {1} 승리".format(num1, play))

                        if play == mermaid.name:
                            flag_mer += 1
                            if flag_mer == 2:
                                print("[{0}] 인어: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해볼까요?".format(mermaid.name))
                                print("[진주 아이]: 이게 뭐예요... 애니깐 봐주고 그런거 없어요??ㅠㅠㅠ")
                                children.children_lose()
                                return 1

                        elif play == children.name:
                            flag_child += 1
                            if flag_child == 2:
                                print("[진주 아이]: 내가 두 판을 모두 이겼으니깐 그만하고, 이제 다른 게임도 해요~")
                                children.children_win()
                                return 1

                        continue

        else:
            print("게임은 두 가지 뿐입니다.")
            continue

# stage2(미니게임 2) - 청기백기 게임 / 통아저씨 게임
def s2_game2 (num):
    if num == 1:
        input("\n------------------------------------------------------------------------------\n")
        print("[{0}] 인어: 그럼 청기백기 게임을 한번 해볼까요??\n".format(mermaid.name))
        print("[진주 아이]: 네, 좋아요!")
        # 순서정하기 가위바위보
        print("\n------------------------------------------------------------------------------\n")
        print("청기백기 게임 규칙 설명\n")
        print("※ 소문자 'b'는 청기올려!, 소문자 'n'은 백기올려!\n※ 소문자 'bb'는 청기 내려!, 소문자 'nn'은 백기 내려! \n※ 3판2선승제로 진행 \n※ 1인당 5번의 공격이 진행되며 가장 적게 틀린 사람이 우승\n※ 3초 안에 알맞은 깃발을 들어야 함")
        print("\n그럼 게임을 시작해 볼까요?")
        input("\n------------------------------------------------------------------------------\n")
        print("[진주 아이]: 누가 먼저 할지 정해요!! 가위,바위,보!")
        who_1 = rps()

        # 아이 선공
        if who_1 == 1:
            flag_child = 0
            flag_mer = 0

            print("\n------------------------------------------------------------------------------\n")
            print("[진주 아이]: 그럼 저부터 공격 할게요!")

            for num1 in range(1, 4, 1):

                input("\n------------------------------------------------------------------------------\n")
                print("{0}번째 판".format(num1))
                p_1 = minigame2_1_def()
                p_2 = minigame2_1_att()
                input("\n------------------------------------------------------------------------------\n")

                print("{0}번째 판 결과: [진주아이 - {1}점] [{2}인어 - {3}점]".format(num1, p_2, mermaid.name, p_1))

                # 승점 비교 p1(인어) | p2(진주아이)
                if p_1 < p_2:
                    flag_child += 1
                    print("[진주 아이]의 승리입니다!")
                    if flag_child == 2:
                        input("\n------------------------------------------------------------------------------\n")
                        print("[진주 아이]: 제가 두 판을 이겼으니.. 그만해요! 어! 돌아오셨어요!")
                        children.children_win()
                        return 2
                    continue

                elif p_1 > p_2:
                    flag_mer += 1
                    print("[{0}] 인어의 승리입니다!".format(mermaid.name))
                    if flag_mer == 2:
                        input("\n------------------------------------------------------------------------------\n")
                        print("[{0}] 인어: 내가 두 판을 모두 이겼으니깐 그만하고... ".format(mermaid.name))
                        print("[진주 아이]: 이게 뭐예요... 또 두 판을 다 이겨버리면... 어! 돌아오셨어요!")
                        children.children_lose()
                        return 2
                    continue

                elif p_1 == p_2:
                    print("{0}번째 판 결과, 무승부 입니다!".format(num1))
                    continue

                # 청기 백기 다음, 통아저씨


        # 인어 선공
        elif who_1 == 2:
            flag_child = 0
            flag_mer = 0

            print("\n------------------------------------------------------------------------------\n")
            print("[진주 아이]: 먼저 공격하세요!")

            for num1 in range(1, 4, 1):

                input("\n------------------------------------------------------------------------------\n")
                print("{0}번째 판".format(num1))
                p_1 = minigame2_1_att()
                p_2 = minigame2_1_def()
                input("\n------------------------------------------------------------------------------\n")

                print("{0}번째 판 결과: [진주아이 - {1}점] [{2}인어 - {3}점]".format(num1, p_1, mermaid.name, p_2))

                # 승점 비교 p1(진주아이) | p2(인어)
                if p_1 > p_2:
                    flag_child += 1
                    print("[진주 아이]의 승리입니다!")
                    if flag_child == 2:
                        input("\n------------------------------------------------------------------------------\n")
                        print("[진주 아이]: 제가 두 판을 이겼으니.. 그만해요! 어! 돌아오셨어요!")
                        children.children_win()
                        return 1
                    continue

                elif p_1 < p_2:
                    flag_mer += 1
                    print("[{0}] 인어의 승리입니다!".format(mermaid.name))
                    if flag_mer == 2:
                        input("\n------------------------------------------------------------------------------\n")
                        print("[진주 아이]: 이게 뭐예요... 또 두 판을 다 이겨버리면... 어! 돌아오셨어요!")
                        children.children_lose()
                        return 1
                    continue

                elif p_1 == p_2:
                    print("{0}번째 판 결과, 무승부 입니다!".format(num1))
                    continue

        else:
            print("게임은 두 가지 뿐입니다.")

    # 2(2) - 통아저씨 게임
    elif num == 2:
        input("\n------------------------------------------------------------------------------\n")
        print("[{0}] 인어: 그럼 통아저씨 게임을 한번 해볼까요??\n".format(mermaid.name))
        print("[진주 아이]: 네, 좋아요!")
        print("\n------------------------------------------------------------------------------\n")
        print("통아저씨 게임 규칙 설명")
        print("※ 3판 2선승제\n※ 1~15의 숫자 중 하나를 선택해 통에 꽂힌 칼을 뽑습니다\n※ 칼을 뽑았을 때 통아저씨가 튀어오르면 지는 게임")
        input("\n------------------------------------------------------------------------------\n")
        print("[진주 아이]: 먼저 칼 뽑을 사람을 정해요!! 가위,바위,보!")
        who_2 = rps()

        # 아이 선공
        if who_2 == 1:
            flag_child = 0
            flag_mer = 0

            print("\n------------------------------------------------------------------------------\n")
            print("[진주 아이]: 그럼 저부터 뽑을 칼의 숫자를 고를게요!")

            for num1 in range(1, 4, 1):

                print("\n------------------------------------------------------------------------------\n")
                print("{0}번째 판".format(num1))

                # 1,3에선 진주 아이부터 | 2에선 인어부터
                if num1 == 1 or num1 == 3:
                    play = minigame2_2_def()
                    input("\n------------------------------------------------------------------------------\n")
                    print("{0}번째 판 결과: [{1}] 승리".format(num1, play))

                    if play == mermaid.name:
                        flag_mer += 1
                        if flag_mer == 2:
                            print("[진주 아이]: 이게 뭐예요... 또 두 판을 다 이겨버리면... 어! 돌아오셨어요!")
                            children.children_lose()
                            return 2

                    elif play == children.name:
                        flag_child += 1
                        if flag_child == 2:
                            print("[진주 아이]: 제가 두 판을 이겼으니.. 그만해요! 어! 돌아오셨어요!")
                            children.children_win()
                            return 2

                    continue

                elif num1 == 2:
                    play = minigame2_2_att()
                    input("\n------------------------------------------------------------------------------\n")
                    print("{0}번째 판 결과: [{1}] 승리".format(num1, play))

                    if play == mermaid.name:
                        flag_mer += 1
                        if flag_mer == 2:
                            print("[진주 아이]: 이게 뭐예요... 또 두 판을 다 이겨버리면... 어! 돌아오셨어요!")
                            children.children_lose()
                            return 2

                    elif play == children.name:
                        flag_child += 1
                        if flag_child == 2:
                            print("[진주 아이]: 제가 두 판을 이겼으니.. 그만해요! 어! 돌아오셨어요!")
                            children.children_win()
                            return 2

                    continue

        # 인어 선공
        elif who_2 == 2:
            flag_child = 0
            flag_mer = 0

            print("\n------------------------------------------------------------------------------\n")
            print("[진주 아이]: 뽑을 칼의 숫자를 먼저 선택하세요!")

            for num1 in range(1, 4, 1):

                print("\n------------------------------------------------------------------------------\n")
                print("{0}번째 판".format(num1))

                # 1,3에선 인어부터 | 2에선 진주 아이부터
                if num1 == 1 or num1 == 3:
                    play = minigame2_2_att()
                    input("\n------------------------------------------------------------------------------\n")
                    print("{0}번째 판 결과: {1} 승리".format(num1, play))

                    if play == mermaid.name:
                        flag_mer += 1
                        if flag_mer == 2:
                            print("[진주 아이]: 이게 뭐예요... 또 두 판을 다 이겨버리면... 어! 돌아오셨어요!")
                            children.children_lose()
                            return 2

                    elif play == children.name:
                        flag_child += 1
                        if flag_child == 2:
                            print("[진주 아이]: 제가 두 판을 이겼으니.. 그만해요! 어! 돌아오셨어요!")
                            children.children_win()
                            return 2

                    continue

                elif num1 == 2:
                    play = minigame2_2_def()
                    input("\n------------------------------------------------------------------------------\n")
                    print("{0}번째 판 결과: {1} 승리".format(num1, play))

                    if play == mermaid.name:
                        flag_mer += 1
                        if flag_mer == 2:
                            print("[진주 아이]: 이게 뭐예요... 또 두 판을 다 이겨버리면... 어! 돌아오셨어요!")
                            children.children_lose()
                            return 2

                    elif play == children.name:
                        flag_child += 1
                        if flag_child == 2:
                            print("[진주 아이]: 제가 두 판을 이겼으니.. 그만해요! 어! 돌아오셨어요!")
                            children.children_win()
                            return 2
                    continue

# 조개 엔딩
def s2_outro():
    minigame2_3()

    input("\n------------------------------------------------------------------------------\n")
    print("딸랑!")
    print("[{0}] 인어: 어서오세요~".format(mermaid.name))
    print("[조 개]: ... 사장님 계신가요?")
    print("[{0}] 인어: 아니요... 잠깐 어디 가셨어요".format(mermaid.name))

    input("\n------------------------------------------------------------------------------\n")
    print("[조 개]: 혹시 제 이야기 좀 들어주실래요?")
    listen = shell_1()

    if listen == '1':
        input("\n------------------------------------------------------------------------------\n")
        print("[조 개]: 사실 [진주 사장]님께서 제 진주를 훔쳐가셨어요...")
        mermaid.shell_kill
        print("[{0}] 인어: 네? 뭐라고요?!? 그래서 사장님이...".format(mermaid.name))
        print("[조 개]: 제 동생 수술비라서 꼭 대가를 받고 팔았어야 했는데, 몰래 훔쳐갈거라곤 생각하지 못했어요...")
        shell_2()
        input("\n------------------------------------------------------------------------------\n")
        print("[{0}] 인어: 신고는 하셨나요?".format(mermaid.name))
        print("[조 개]: 아뇨, 동생 옆에서 쉴 틈이 없어서..")
        shell_3()

    elif listen == '2':
        input("\n------------------------------------------------------------------------------\n")
        print("딸랑\n그 자리에 서있는 [조 개]를 뒤로 하고, 인간이 되는 약을 사기 위해 나왔다")
        print("[조 개]: 째릿.......")
        print("[{0}] 인어: 엥? 순간 서늘한 느낌이 들었다..".format(mermaid.name))
        mermaid.shell_kill
