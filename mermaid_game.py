# 모듈 불러 올 때 : from 파일이름 import 함수 이름
from s3_crab import less
from s3_crab import enough
from s1_seaweed import s1_intro
from s1_seaweed import s1_money

#아스키코드
import random
coin=random.randrange(97,122)
print(chr(coin))

class mermaid:
    name = "박"
    HP = 100
    SP = 5
    coin = 100

class user_ask:
    a = "코인이 얼마나 있는지 묻는다"
    b = "인간이 되는 약에 대해 묻는다"
    c = "코인 버는 방법을 묻는다"
    d = "소라게에게 간다"
    
class mermaid_answer:
    answer_a = "지금 %s 코인 정도 있네요~"%mermaid.coin
    answer_b = "인간이 되는 약은 약쟁이 소라게에게 살 수 있어요!!"
    answer_c = "코인 버는 방법은 2가지가 있어요~\n\n첫 번째는 진주 가게에서 알바 하는 것!\n두 번째는 미역 가게에서 알바 하는 것!\n"
  
# 시작할지 말지 선택
print("----------------게임 진행 시 대화는 enter 혹은 숫자키로 진행됩니다----------------\n\n                                 *Mermaid to Human*\n")
print("바닷속에 살던 인어는 자신과 생김새가 똑같은 육지의 인간을 발견합니다.\n행복해보이는 이들의 삶을 동경하게 된 인어는 사람이 되고자 인간이 되는 약을 사려고 하네요.")

while 1:
    game_start_= str(input("인어의 여정을 함께 해주시겠습니까?  네- 1 / 아니요-2\n"))
    if game_start_ == "1" or "네":
        mermaid.name = input("인어 이름은 알고 시작하려고 하는 건가요? \n인어의 이름을 지어주세요!\n")
        break
    elif game_start_ == "2" or "아니오":
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
                print("소라게에게 약을 사기 위해선 코인이 필요해요! 이곳에서 %s"%(mermaid_answer.answer_c))
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
input()
print("[%s] 인어: 100코인을 향해 함께 출발해봐요!"%mermaid.name)
from map import choose
map_intro = str(choose)
print(map_intro)

# Stage1 - 미역 가게에서 알바
if map_intro == "1":
    s1_intro(mermaid.name)
    s1_money(mermaid.coin)

# Stage2 - 진주  가게에서 알바
elif map_intro == "2":
    print("진주 가게 준비중")
    
# Stage2.1 - 진주를 빼앗긴 조개와의 전투

# Stage3 - 소라게 [코인없음 / 코인 다 채움 [얼마나 죽였느냐에 따라 Bad/ Good ending]]
elif map_intro == "3":
    #less_money
    if mermaid.coin < 100:
        less(mermaid.coin)
    #enough_money
    elif mermaid.coin >= 100:
        enough(mermaid.coin)

#random 모듈 불러오는 방법
"""
import random

coin=random.randrange(0,200)
print(coin)


다리가 생겼다

 (⊙.⊙)
ㅡ ㅁ ㅡ
   |    |
"""



