from c1_character import mermaid

# less_money
def less():
    print("[소라게]: 코인도 없는게 어디서! %s코인 더 벌어와!" % (100-mermaid.coin))

# enough_money
def enough():
    print("[소라게]: 코인을 다 벌었나보군? 그렇게 인간이 되고 싶어하는 이유가 대체 뭔지...")
    print("[소라게]: 물약 여기있다! 먹기 전 주의 사항이... 하나 있는데...\n")
    input()

    while True:
        ending = str(input("1 - 주의 사항을 듣고 마실지 말지 결정한다\n2 - 듣지 않고 바로 마신다\n"))

        #주의 사항을 듣고
        if ending == "1":
            print("[소라게]: 이 물약은 마시는 사람에 따라 결과가 다르게 나타나. 그동안 코인을 위해 저질렀던 더러운 일이 있다면 마시지 않는게 좋을껄?")

            ending2 = int(input("1 - 마신다\n2 - 그냥 인어로 살아간다\n"))
                     
            if ending2 == "1":
                print("\n(꿀꺽)\n")
                break
            
            elif ending2 == "2":
                print("[인어 이름 어쩌구]: 코인을 얻기 위해 너무 많은 피를 묻혔어. 그냥 난 이렇게 살아갈래... 도와줘서 고마워")
                input()
                print("소라게의 의미심장한 미소와 함께 파도가 갑작스럽게 몰려든다.\n\n(꿀꺽)\n\n물약이 인어의 입 안으로 한 방울 떨어졌다.")
                break
            
            break
        
        #주의 사항을 듣지 않고
        elif ending == "2":
            print("\n(꿀꺽)\n")
            print("[소라게]: 엥? 그냥 이렇게 마셔버린다고? 후회할 텐데...")
            break

        else:
            print("다시 한 번 생각해보자")
            continue
        
    

"""
class human():
    def sing(self):
        print("노래 부르기")

class rain(human):
    def sing(self):
        print("화려한 조명이 나를 감싸네")

rain = rain()
changha = human()

rain.sing()

changha.sing()




import random:
    # 행운의 번호 추첨할 수 있도록 들어갔을 때 돈을 줌.
class crab:
    def __init__(self,name, HP,MP):
        self.lucknum =  random()
        


    def att(self,monster):
        if self.MP==100:
            sefl.MP==50
            monster.HP==50

mus1 = monster("주황버섯",100,100)
mus1.name = "파랑버섯"

        print("[약쟁이 소라게]: 돈도 없는게 어디서!")
"""

# 완료된 소라게 3가지 멘트 but, 함수 별로 모듈화 필요함.
"""
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
            continue"""
