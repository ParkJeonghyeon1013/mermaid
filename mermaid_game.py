class mermaid:
    name = "박"
    HP = 100
    SP = 5
    coin = 0

class pearl:
    print("진주 사장")

class seaweed:
    print("미역")

class user_ask:
    a = "코인이 얼마나 있는지 묻는다"
    b = "인간이 되는 약에 대해 묻는다"
    c = "코인 버는 방법을 묻는다"
    d = "소라게에게 간다"
    
class mermaid_answer:
    answer_a = "지금 %s원 정도 있네요~"%mermaid.coin
    answer_b = "인간이 되는 약은 약쟁이 소라게에게 살 수 있어요!!"
    answer_c = "코인 버는 방법은 2가지가 있어요~\n\n첫 번째는 진주 가게에서 알바 하는 것!\n두 번째는 미역 가게에서 알바 하는 것!\n"

class map:
    stage_1 = "1 - 미역 공장 가본다"
    stage_2 = "2 - 진주 가게에 가본다"
    stage_3 = "3 - 약쟁이 소라게에게 가본다"
    
# 시작할지 말지 선택
print("바닷속에 살던 인어는 자신과 생김새가 똑같은 육지의 인간을 발견합니다.\n행복해보이는 이들의 삶을 동경하게 된 인어는 사람이 되고자 인간이 되는 약을 사려고 하네요.")

while 1:
    game_start_= input("인어의 여정을 함께 해주시겠습니까?  네- 1 / 아니요-2\n")
    if game_start_ == "1":
        mermaid.name = input("인어 이름은 알고 시작하려고 하는 건가요? \n인어의 이름을 지어주세요!\n")
        break
    elif game_start_ == "2":
        print("인어는 평생 인어로 살아갔답니다^^\n 그래도 고생해서 만들었는데 Play 해주세요...")
        continue

# intro - 게임 map에 대한 설명
print("""~~~~~~~ ~~~~~     ~~~~~~~~   ~~~~~~~~~~~~~~~~
           ~~~~~   ~~~~~~~~~~~~~        ~~~~~~~~
      ~~~ ~~~~~~~~~    ~~~~~~~~~~~~       ~~~~~~~~~~~
                    여기는 깊은 심해
       ~~~~~~~ ~~~~~     ~~~~~~~~   ~~~~~~~~~~~~~~~~
           ~~~~~   ~~~~~~~~~~~~~        ~~~~~~~~
      ~~~ ~~~~~~~~~    ~~~~~~~~~~~~       ~~~~~~~~~~~""")

print("안녕하세요? 반가워요~ 저는 인어 [%s] 입니다~\n인간은 되고 싶고 코인은 없고... 그런 절 도와주시겠다고 선뜻 와주셔서 고마워요~"%(mermaid.name))
input()

while True:
    ask = str(input("1 - %s \n2 - %s\n"%(user_ask.a, user_ask.b)))
    #코인 | 약
    if ask == "1":
        print("%s\n\n인간이 되는 약에 대해서는 궁금하지 않나요?"%(mermaid_answer.answer_a))

        while True:
            ask1 = str(input("1 - 궁금해요! \n2 - 빨리 시작이나 합시다!\n"))
            if ask1 == "1":
                print("%s"%(mermaid_answer.answer_b))
                print("소라게에게 약을 사기 위해선 코인이 필요해요!\n이곳에서 %s"%(mermaid_answer.answer_c))
                break
            elif ask1 == "2":
                print("급하시네요.. 그냥 바로 코인을 얻는 방법을 알려드릴게요~\n\n%s"%(mermaid_answer.answer_c))
                break
            else:
                print("다시 생각해보세요")
                continue
        break
    
    #약 | 코인
    elif ask == "2":
        print("%s"%(mermaid_answer.answer_b))
        print("소라게에게 약을 사기 위해선 코인이 필요해요!")
        input()
        print("\n이곳에서 %s"%(mermaid_answer.answer_c))
        break
    else:
        print("다시 질문해주세요!\n")
        continue

# intro - 게임 진행
"""import map
print(map.full_map)
"""
# Stage1 - 진주 가게에서 알바


# Stage1.1 - 진주를 빼앗긴 조개와의 전투




# Stage2 - 미역 가게에서 알바

# Stage2.1 - 흘러 들어온 미역을 되찾기 위해 온 미역 양식업주


# Stage3 - 소라게 [코인없음 / 코인 다 채움 [얼마나 죽였느냐에 따라 Bad/ Good ending]]

#less_money
if mermaid.coin < 100:
    print("[소라게]: 코인도 없는게 어디서! %s코인 더 벌어와!"%(100-mermaid.coin))
#enough_money
elif coin >= 100:
    print("[소라게]: 코인을 다 벌었나보군? 그렇게 인간이 되고 싶어하는 이유가 대체 뭔지...")
    input()
    print("[소라게]: 물약 여기있다! 먹기 전 주의 사항이... 하나 있는데...\n")
    while True:
        ending = int(input("1 - 주의 사항을 듣고 마실지 말지 결정한다\n2 - 듣지 않고 바로 마신다\n"))
        #주의 사항을 듣고
        if ending == 1:
            print("[소라게]: 이 물약은 마시는 사람에 따라 결과가 다르게 나타나. 그동안 코인을 위해 저질렀던 더러운 일이 있다면 마시지 않는게 좋을껄?")

            ending2 = int(input("1 - 마신다\n2 - 그냥 인어로 살아간다\n"))
                     
            if ending2 == 1:
                print("\n(꿀꺽)\n")
                break
            
            elif ending2 == 2:
                print("[인어 이름 어쩌구]: 코인을 얻기 위해 너무 많은 피를 묻혔어. 그냥 난 이렇게 살아갈래... 도와줘서 고마워")
                input()
                print("소라게의 의미심장한 미소와 함께 파도가 갑작스럽게 몰려든다.\n\n(꿀꺽)\n\n물약이 인어의 입 안으로 한 방울 떨어졌다.")
                break
            break
        #주의 사항을 듣지 않고
        elif ending == 2:
            print("\n(꿀꺽)\n")
            print("[소라게]: 엥? 그냥 이렇게 마셔버린다고? 후회할 텐데...")
            break
        else:
            print("다시 한 번 생각해보자")
            continue

"""import random

coin=random.randrange(0,200)
print(coin)
"""


