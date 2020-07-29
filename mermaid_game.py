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
    answer_c = "코인 버는 방법은 2가지가 있어요~\n 첫 번째는 진주 가게에서 알바 하는 것!\n 두 번째는 미역 가게에서 알바 하는 것!\n"
    answer_d = "따라오세요!"
    
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

# intro
print("""~~~~~~~ ~~~~~     ~~~~~~~~   ~~~~~~~~~~~~~~~~
           ~~~~~   ~~~~~~~~~~~~~        ~~~~~~~~
      ~~~ ~~~~~~~~~    ~~~~~~~~~~~~       ~~~~~~~~~~~
                    여기는 깊은 심해
       ~~~~~~~ ~~~~~     ~~~~~~~~   ~~~~~~~~~~~~~~~~
           ~~~~~   ~~~~~~~~~~~~~        ~~~~~~~~
      ~~~ ~~~~~~~~~    ~~~~~~~~~~~~       ~~~~~~~~~~~""")

print("안녕하세요? 반가워요~ 저는 인어 [%s] 입니다~\n인간은 되고 싶고 코인은 없고... 그런 절 도와주시겠다고 선뜻 와주셔서 고마워요~"%(mermaid.name))
input()
ask = int(input("1 - %s \n2 - %s\n"%(user_ask.a, user_ask.b)))
while true:
    if ask == 1:
        print("%s"%(mermaid_answer.answer_a))
    elif ask == 2:
        print("%s"%(mermaid_answer.answer_b))
    else:
        print("다시 질문해주세요!")
        continue



# Stage2 - 진주 가게에서 알바
# Stage2.1 - 진주를 빼앗긴 조개와의 전투



# Stage3 - 미역 가게에서 알바


# Stage3.1 - 흘러 들어온 미역을 되찾기 위해 온 미역 양식업주
