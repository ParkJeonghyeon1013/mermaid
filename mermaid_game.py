# 모듈 불러 올 때 : from 파일이름 import 함수 이름
from c1_character import mermaid
from s1_seaweed import s1_intro, s1_game, s1_outro
from s2_pearl import s2_intro, s2_game1, s2_game2, s2_outro
from s3_crab import money, potion_effect
from map import choose

"""어떻게 해야 main을 최대한 깔끔하게 만들 수 있을지 => 앞에서 이름 묻고 길 찾는 부분까지 다 모듈화 시켜버리기"""
class user_ask ():
    a = "코인이 얼마나 있는지 묻는다"
    b = "인간이 되는 약에 대해 묻는다"
    c = "코인 버는 방법을 묻는다"
    d = "소라게에게 간다"
    
class mermaid_answer ():
    answer_a = "지금 %s 코인 정도 있네요~" % mermaid.coin
    answer_b = "인간이 되는 약은 약쟁이 소라게에게 살 수 있어요!!"
    answer_c = "코인 버는 방법은 2가지가 있어요~\n\n첫 번째는 미역 공장에서 알바 하는 것!\n두 번째는 진주 가게에서 알바 하는 것!\n"
  
# 시작할지 말지 선택
print("\n--------------게임 진행 시 대화는 enter 혹은 숫자키로 진행됩니다-------------\n\n                     *Mermaid to Human*\n")
print("바닷속에 살던 인어는 자신과 생김새가 똑같은 육지의 인간을 발견합니다.\n행복해보이는 이들의 삶을 동경하게 된 인어는 사람이 되고자 인간이 되는 약을 사려고 하네요.")

while True:
    game_start_= str(input("인어의 여정을 함께 해주시겠습니까?  네- 1 / 아니오-2\n"))
    if game_start_ == "1":
        print("\n------------------------------------------------------------------------------\n")
        mermaid.name = input("인어 이름은 알고 시작하려고 하는 건가요? \n인어의 이름을 지어주세요!\n>>> ")
        break
    elif game_start_ == "2":
        print("인어는 평생 인어로 살아갔답니다^^\n 그래도 고생해서 만들었는데 Play 해주세요...")
        continue
    else:
        print("인어는 평생 인어로 살아갔답니다^^\n 그래도 고생해서 만들었는데 Play 해주세요...")
        continue

# intro - 게임 map에 대한 설명
print("""
     ~~~~~~~ ~~~~~     ~~~~~~~~   ~~~~~~~~~~~~~~~~
           ~~~~~   ~~~~~~~~~~~~~        ~~~~~~~~
      ~~~ ~~~~~~~~~    ~~~~~~~~~~~~       ~~~~~~~~~~~
                     여기는 깊은 심해
       ~~~~~~~ ~~~~~     ~~~~~~~~   ~~~~~~~~~~~~~~~~
           ~~~~~   ~~~~~~~~~~~~~        ~~~~~~~~
      ~~~ ~~~~~~~~~    ~~~~~~~~~~~~       ~~~~~~~~~~~""")

print("\n안녕하세요? 반가워요~ 저는 인어 [%s] 입니다~\n인간은 되고 싶고 코인(= 인어 세계의 화폐)은 없고... \n그런 절 도와주시겠다고 선뜻 와주셔서 고마워요~" % (mermaid.name))
input("\n------------------------------------------------------------------------------\n")

while True:
    ask = str(input("1 - %s \n2 - %s\n" % (user_ask.a, user_ask.b)))
    print("------------------------------------------------------------------------------")
    # 코인 | 약
    if ask == "1":
        print("%s\n\n인간이 되는 약에 대해서는 궁금하지 않나요?" % (mermaid_answer.answer_a))

        while True:
            
            ask1 = str(input("1 - 궁금해요! \n2 - 빨리 시작이나 합시다!\n"))
            if ask1 == "1":
                print("------------------------------------------------------------------------------\n")
                print("%s" % (mermaid_answer.answer_b))
                print("소라게에게 약을 사기 위해선 코인이 필요해요! 이곳에서 %s" % (mermaid_answer.answer_c))
                break
            elif ask1 == "2":
                print("------------------------------------------------------------------------------\n")
                print("급하시네요.. 그냥 바로 코인을 얻는 방법을 알려드릴게요~\n\n%s" % (mermaid_answer.answer_c))
                break
            else:
                print("다시 생각해보세요")
                continue
        break
    
    # 약 | 코인
    elif ask == "2":
        print("%s" % (mermaid_answer.answer_b))
        print("소라게에게 약을 사기 위해선 코인이 필요해요!")
        input("------------------------------------------------------------------------------\n")
        print("이곳에서 %s" % (mermaid_answer.answer_c))
        break
    else:
        print("다시 질문해주세요!\n")
        continue

# intro - 게임 진행
input("------------------------------------------------------------------------------\n")
stage = 0
map_num = choose(stage)

# Stage1 - 미역 공장에서 알바
if map_num == '1':
    s1_intro()
    s1_game()
    s1_outro()

    stage = 1
    map_num = choose(stage)

    # 미역 - 진주가게 - 소라게
    if map_num == '1':
        s2_intro()
        next_game = s2_game1()
        s2_game2(next_game)
        s2_outro()

        print("\n[{0}] 인어: {1}코인을 모았습니다! 약쟁이 소라게를 찾아가 물약과 교환해야겠어요~".format(mermaid.name, mermaid.coin))
        money()
        potion_effect()

    # 미역 - 소라게 - 진주가게 - 소라게
    elif map_num == '2':
        money()

        print("[{0}] 인어: 이제 진주가게로 가서 좀만 더 모으면 될 것 같아요!".format(mermaid.name))
        s2_intro()
        next_game = s2_game1()
        s2_game2(next_game)
        s2_outro()

        print("\n[{0}] 인어: {1}코인을 모았습니다! 약쟁이 소라게를 찾아가 물약과 교환해야겠어요~".format(mermaid.name, mermaid.coin))
        money()
        potion_effect()

# Stage2 - 진주  가게에서 알바
elif map_num == '2':
    s2_intro()
    next_game = s2_game1()
    s2_game2(next_game)
    s2_outro()

    stage = 2
    map_num = choose(stage)

    # 진주 - 미역 - 소라게
    if map_num == '1':
        s1_intro()
        s1_game()
        s1_outro()

        print("\n[{0}] 인어: {1}코인을 모았습니다! 약쟁이 소라게를 찾아가 물약과 교환해야겠어요~".format(mermaid.name, mermaid.coin))
        money()
        potion_effect()

    # 진주 - 소라게  - 미역 - 소라게
    elif map_num == '2':
        money()

        print("[{0}] 인어: 이제 미역 공장으로 가서 좀만 더 모으면 될 것 같아요!".format(mermaid.name))
        s1_intro()
        s1_game()
        s1_outro()

        print("\n[{0}] 인어: {1}코인을 모았습니다! 약쟁이 소라게를 찾아가 물약과 교환해야겠어요~".format(mermaid.name, mermaid.coin))
        money()
        potion_effect()

# Stage3 - 소라게 [코인없음 / 코인 다 채움 [얼마나 죽였느냐에 따라 Bad/ Good ending]]
elif map_num == '3':
    money()

    stage = 3
    map_num = choose(stage)

    # 진주 - 미역 - 소라게
    if map_num == '1':
        s1_intro()
        s1_game()
        s1_outro()

        stage = 1
        map_num1 = choose(stage)

        if map_num1 == '1':
            s2_intro()
            next_game = s2_game1()
            s2_game2(next_game)
            s2_outro()

            print("\n[{0}] 인어: {1}코인을 모았습니다! 약쟁이 소라게를 찾아가 물약과 교환해야겠어요~".format(mermaid.name, mermaid.coin))
            money()
            potion_effect()

        elif map_num1 == '2':
            money()

            print("[{0}] 인어: 이제 진주 가게로 가서 좀만 더 모으면 될 것 같아요!".format(mermaid.name))
            s2_intro()
            next_game = s2_game1()
            s2_game2(next_game)
            s2_outro()

            print("\n[{0}] 인어: {1}코인을 모았습니다! 약쟁이 소라게를 찾아가 물약과 교환해야겠어요~".format(mermaid.name, mermaid.coin))
            money()
            potion_effect()

    # 진주 - 소라게  - 미역 - 소라게
    elif map_num == '2':
        s2_intro()
        next_game = s2_game1()
        s2_game2(next_game)
        s2_outro()

        stage = 2
        map_num1 = choose(stage)

        if map_num1 == '1':
            s1_intro()
            s1_game()
            s1_outro()

            print("\n[{0}] 인어: {1}코인을 모았습니다! 약쟁이 소라게를 찾아가 물약과 교환해야겠어요~".format(mermaid.name, mermaid.coin))
            money()
            potion_effect()

        elif map_num1 == '2':
            money()

            print("[{0}] 인어: 이제 미역 공장으로 가서 좀만 더 모으면 될 것 같아요!".format(mermaid.name))
            s1_intro()
            s1_game()
            s1_outro()

            print("\n[{0}] 인어: {1}코인을 모았습니다! 약쟁이 소라게를 찾아가 물약과 교환해야겠어요~".format(mermaid.name, mermaid.coin))
            money()
            potion_effect()

