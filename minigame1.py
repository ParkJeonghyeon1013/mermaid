import time
import random
from c1_character import mermaid
from c2_seaweed_hunter import mini1_NPC


"""
now = datetime.datetime.now()
print(now)          # 2018-07-28 12:11:32.669083

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)      # 2018-07-28
 
nowTime = now.strftime('%H:%M:%S')
print(nowTime)      # 12:11:32
 
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)  # 2018-07-28 12:11:32
"""

# 게임 모듈 (1)
# 1은 미역 양식장 주인이 공격하는 것\n승리시 피해 없지만, 패배시 hp 깎인다

def minigame1_1 ():
    print("현재 코인: {0}".format(mermaid.coin))
    print("1 - 미역 양식장 주인의 작살 공격이 시작됩니다. 5초 내로 반격해주세요.")
    input("\n------------------------------------------------------------------------------\n")

    # second = 현재 시간을 받는거임
    s = time.ctime()
    second = int(s[17])*10+int(s[18])+60
    timer = second+5
 
    """print("second = 현재 시간:{0}\n".format(second))"""
    """print("timer = 5초 추가된 것:{0}\n".format(timer))"""
    
    # 아스키코드 / timer = second 에서 5초 더한 제한 시간 같은거
    letter = chr(random.randrange(65, 90))+chr(random.randrange(97, 122))+chr(random.randrange(97, 122))
    a_letter = input("{0}와 똑같이 입력해 반격하시오.\n".format(letter))


    # 같은 문자를 입력했을 때 / game = 입력 후의 시간임
    if letter == a_letter:
        after_entering = time.ctime()
        game = int(after_entering[17])*10+int(after_entering[18])+60
        print("second: {0}/ timer: {1}/ game: {2}".format(second, timer, game))
    
    # 게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
        if game <= second:
            game += 60
            print("game: {0}".format(game))

            # 제한 시간 내에 성공, 실패
            if game > timer:
                print("{0}초 초과해 실패".format(game-timer))
                mermaid.HP -= 20
                print("작살이 스쳐 HP가 20 감소합니다\n 남은 HP: {0}".format(mermaid.HP))
                input("------------------------------------------------------------------------------\n")   
            elif game <= timer:
                mermaid.kill += 0.5
                print("반격에 성공했습니다.\n")
                input("------------------------------------------------------------------------------\n")   
            
    # 일반적인 경우
        elif game > second:
            print("second: {0}/ game: {1}".format(second,game))
            # 제한 시간 내에 성공, 실패
            if game > timer:
                print("{0}초 초과해 실패".format(game-timer))
                mermaid.HP -= 20
                print("작살이 스쳐 HP가 20 감소합니다\n 남은 HP: {0}".format(mermaid.HP))
                input("------------------------------------------------------------------------------\n")   
            elif game <= timer:
                mermaid.kill += 0.5
                print("반격에 성공했습니다.\n")
                input("------------------------------------------------------------------------------\n")   
    else:
        mermaid.HP -= 20
        print("작살이 스쳐 HP가 20 감소합니다\n 남은 HP: {0}".format(mermaid.HP))
        input("------------------------------------------------------------------------------\n")

    return 0

# 게임 모듈 (2)
# 2는 접착식 거북손, 따개비 발견 \ Homi 로 뗄 수 있음. kill 포인트가 쌓이고, 패배시 hp 깎인다
def minigame1_2 ():
    print("현재 코인: {0}".format(mermaid.coin))
    m1_ran = random.randrange(1, 3)

# 1이 나왔을 경우 거북손 채취
    if m1_ran == 1:
        print("2 - 거북손을 발견했습니다!\n굳이 채취하지 않아도 되지만, 코인은 좀 챙길 수 있을 것 같은데요?\n")

        # 거북손 채취 여부 선택
        while True:
            m1_choose = str(input("1 - 채취한다.\n2 - 얼마 못 벌 것 같으니 그냥 미역이나 찾으러 간다.\n"))

            if m1_choose == '1':
                print("\n------------------------------------------------------------------------------\n")
                m1_turtle = str(input("※ 작은 따옴표 제외\n국산 호미를 사용해 채취하려면 '호미'\n외국산 Homi로 채취하려면 'Homi'를 입력해주세요.\n"))

                # 호미 선택
                if m1_turtle == "호미":
                    mermaid.kill += 1
                    mermaid.HP -= 5
                    mermaid.coin += 5
                    mini1_NPC.shell_count += 1
                    print("역시 국산 호미! 거북손 채취를 성공했습니다.\n그러나, 호미질 하던 중 손에 상처를 입어 HP가 5 감소합니다\n현재 HP: {0}".format(mermaid.HP))
                    input("------------------------------------------------------------------------------\n")
                    print(mini1_NPC.shell_count)
                    break
                    
                elif m1_turtle == "Homi":
                    mermaid.kill += 1
                    mermaid.HP -= 5
                    mermaid.coin += 5
                    mini1_NPC.shell_count += 1
                    print("외국산 호미를 사용해 거북손 채취를 성공했습니다.\n그러나, 호미질 하던 중 손에 상처를 입어 HP가 5 감소합니다\n현재 HP: {0}".format(mermaid.HP))
                    input("------------------------------------------------------------------------------\n")
                    print(mini1_NPC.shell_count)
                    break

                else:
                    print("주머니에 넣어둔 호미가 갑자기 사라졌어요... 따개비 채취에 실패했습니다.")
                    input("------------------------------------------------------------------------------\n")   
                    break

            elif m1_choose == '2':
                print("생명은 소중한 것 같아요. 미역이나 찾으러 가볼까요?")
                input("\n------------------------------------------------------------------------------\n")   
                break

            else:
                print("선택 방안은 두 가지 뿐입니다. 다시 선택해주세요.")
                continue

# 2가 나왔을 경우 따개비 채취
    elif m1_ran == 2:
        print("2 - 따개비를 발견했습니다!\n굳이 채취하지 않아도 되지만, 코인은 좀 챙길 수 있을 것 같은데요?\n\n")

        while True:
            m1_choose = str(input("1 - 채취한다.\n2 - 얼마 못 벌 것 같으니 그냥 미역이나 찾으러 간다.\n"))

            # 따개비  채취 여부 선택
            if m1_choose == "1":
                m1_turtle = input("※ 작은 따옴표 제외\n국산 호미를 사용해 채취하려면 '호미'\n외국산 Homi로 채취하려면 'Homi'를 입력해주세요.\n")

                # 호미 선택
                if m1_turtle == "호미":
                    mermaid.kill += 1
                    mermaid.HP -= 5
                    mermaid.coin += 5
                    mini1_NPC.shell_count += 1
                    print("역시 국산 호미! 따개비 채취를 성공했습니다.\n그러나, 호미질 하던 중 손에 상처를 입어 HP가 5 감소합니다\n현재 HP: {0}".format(mermaid.HP))
                    input("------------------------------------------------------------------------------\n")
                    print(mini1_NPC.shell_count)
                    break

                elif m1_turtle == "Homi":
                    mermaid.kill += 1
                    mermaid.HP -= 5
                    mermaid.coin += 5
                    mini1_NPC.shell_count += 1
                    print("외국산 호미를 사용해 따개비 채취를 성공했습니다.\n그러나, 호미질 하던 중 손에 상처를 입어 HP가 5 감소합니다\n현재 HP: {0}".format(mermaid.HP))
                    input("------------------------------------------------------------------------------\n")
                    print(mini1_NPC.shell_count)
                    break

                else:
                    print("호미가 부러져 따개비 채취에 실패했습니다.")
                    print("\n------------------------------------------------------------------------------\n")
                    break

            elif m1_choose == '2':
                print("생명은 소중한 것 같아요. 미역이나 찾으러 가볼까요?")
                input("\n------------------------------------------------------------------------------\n")   
                break

            else:
                print("선택 방안은 두 가지 뿐입니다. 다시 선택해주세요.")
                continue
    return 0

# 게임 모듈 (3)
# 3은 미역 발견\n 승리시 10개의 코인을 얻을 수 있지만, 패배시 아무 변화 없음
def minigame1_3 ():
    print("\n현재 코인: {0}".format(mermaid.coin))
    print("3 - 미역을 발견했습니다! \n5초 내로 채취하지 않으면 물살에 떠내려 갈지 몰라요.")
    input("\n------------------------------------------------------------------------------\n")
    # second = 현재 시간을 받는거임
    s = time.ctime()
    second = int(s[17])*10+int(s[18])+60
    timer = second+5
 
    """print("second = 현재 시간:{0}\n".format(second))"""
    """print("timer = 5초 추가된 것:{0}\n".format(timer))"""

    # 아스키코드 / timer = second 에서 5초 더한 제한 시간 같은거
    letter = chr(random.randrange(65, 90))+chr(random.randrange(97, 122))+chr(random.randrange(97, 122))
    a_letter = input("{0}와 똑같이 입력해 미역을 채취하시오.\n".format(letter))

    # 같은 문자를 입력했을 때 / game = 입력 후의 시간임
    if letter == a_letter:
        after_entering = time.ctime()
        game = int(after_entering[17])*10+int(after_entering[18])+60
        
        """print("second: {0}/ timer: {1}/ game: {2}".format(second,timer,game))"""
    
    # 게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
        if game <= second:
            game += 60
            
            # 제한 시간 내에 성공, 실패
            if game > timer:
                print("{0}초 초과해 실패".format(game-timer))
                print("센 물살에 미역이 떠내려 갔습니다.")

            elif game <= timer:
                mermaid.coin += 10
                mini1_NPC.seaweed_count += 1
                seaweed_num = mini1_NPC.seaweed_count
                print(mini1_NPC.seaweed_count)

                # 미역을 얼마나 더 모아야 하는지
                if seaweed_num >= 5:
                    print("미역을 다 모았습니다!")
                    print("\n------------------------------------------------------------------------------\n")
                    return seaweed_num

                else:
                    print("미역 채집(1)에 성공했습니다.\n앞으로 채집해야 할 미역 개수: {0}".format(5-seaweed_num))
                    input("\n------------------------------------------------------------------------------\n")   
         
    # 일반적인 경우
        elif game > second:
            """print("second: {0}/ game: {1}".format(second,game))"""
            
            # 제한 시간 내에 성공, 실패
            if game > timer:
                print("{0}초 초과해 실패".format(game-timer))
                print("센 물살에 미역이 떠내려 갔습니다.")
            elif game <= timer:
                mermaid.coin += 10
                mini1_NPC.seaweed_count += 1
                seaweed_num = mini1_NPC.seaweed_count
                print(mini1_NPC.seaweed_count)

                # 미역을 얼마나 더 모아야 하는지
                if seaweed_num >= 5:
                    print("미역을 다 모았습니다!")
                    print("\n------------------------------------------------------------------------------\n")
                else:
                    print("미역 채집(1)에 성공했습니다.\n앞으로 채집해야 할 미역 개수: {0}".format(5-seaweed_num))
                    input("\n------------------------------------------------------------------------------\n")   

    else:
        mermaid.HP -= 10
        print("센 물살에 미역이 떠내려 갔습니다.")
        input("\n------------------------------------------------------------------------------\n")
            
# 체력 회복 모듈 
def mini1_health():
    print("[{0}] 인어: 제 체력이 {1}밖에 남지 않았어요...".format(mermaid.name, mermaid.HP))
    print("[미역 사장]: 그러게 내가 뭐랬어? 조심하라니깐! \n체력이 50 회복되는 포션을 준비해두긴 했는데, 미역 3개를 공짜로 주면 포션을 주지.\n")

    while True:
        mini_h = str(input("1- 체력 회복 포션을 산다. 2- 사지 않는다.\n"))

    # 돈이 있을 경우
        if mini_h == "1" and mini1_NPC.seaweed_count >= 3:
            mini1_NPC.seaweed_count -= 3
            mermaid.HP += 50
            mermaid.coin -= 30
            print("[미역 사장]: 다시 열심히 일해야겠구만! 고생해~~")
            print("[{0}] 인어: 미역 3개와 체력 회복 포션을 교환했으니, {1}개의 미역을 더 채취해야 해요... \n현재 체력이 {2}로 올랐다.".format(mermaid.name, (5-mini1_NPC.seaweed_count), mermaid.HP))
            break
            
    # 돈이 없을 경우
        elif mini_h == "1" and mini1_NPC.seaweed_count < 3:
            print("[{0}] 인어: 지금까지 모은 미역이 {1}개 뿐이에요. 조금만 줄여주실 수 있나요?".format(mermaid.name, mini1_NPC.seaweed_count))
            print("[미역 사장]: 허... 참... 그래 열심히 일 하다 다친거니 미역 1개!\n더이상은 안돼!")
        
            if mini1_NPC.seaweed_count >= 1:
                mini1_NPC.seaweed_count -= 1
                mermaid.HP += 50
                mermaid.coin -= 10
                print("[%s] 인어: 감사합니다~"%mermaid.name)
                print("[미역 사장]: 그래~ 얼른 미역이나 가져와!!! 그래야 너도 나도 돌아가지!")
                print("[{0}] 인어: 미역 1개와 체력 회복 포션을 교환했으니, {1}개의 미역을 더 채취해야 해요...\n현재 체력이 {2}로 올랐다.".format(mermaid.name, (5-mini1_NPC.seaweed_count), mermaid.HP))
                break

            else:
                mermaid.HP += 50
                print("[미역 사장]: 어어? 왜 우물쭈물하고 있어! 설마 미역을 하나도 채취하지 못한거야? \n어휴.. 우리 가게에서 일하다 다친거니 그냥 주지.. 대신 얼른 미역 모아오도록 해!")
                print("[{0}] 인어: 네? 정말요? 감사합니다!\n현재 체력이 {1}로 올랐다".format(mermaid.name, mermaid.HP))
                break

        else:
            print("[%s] 인어: 다시 한번 생각해보세요...")
            continue
    return 0

"""
import random
import time

       #second = 현재 시간을 받는거임
s = time.ctime()
second = int(s[17])*10+int(s[18])+60
print("second = 현재 시간:{0}\n".format(second))

    #아스키코드 / timer = second에서 5초 더한 제한 시간 같은거
letter=chr(random.randrange(65,90))+chr(random.randrange(97,122))
timer = second+5
print("timer = 5초 추가된 것:{0}\n".format(timer))

a_letter=input("{0}와 똑같이 입력하시오\n".format(letter))

    #같은 문자를 입력했을 때 / game = 입력 후의 시간임
if letter == a_letter:
    after_entering= time.ctime()
    game = int(after_entering[17])*10+int(after_entering[18])+60
    print("second: {0}/ timer: {1}/ game: {2}".format(second,timer,game))
    
    #게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
    if game <= second:
        game += 60
        print("game: {0}".format(game))
            #제한 시간 내에 성공, 실패
        if game > timer:
            print("{0}초 초과해 실패".format(game-timer))
        elif game <= timer:
             print("성공")
            
    #일반적인 경우
    elif game > second:
        print("second: {0}/ game: {1}".format(second,game))
            #제한 시간 내에 성공, 실패
        if game > timer:
            print("{0}초 초과해 실패".format(game-timer))
        elif game <= timer:
            print("성공")
else:
    print("실패")

"""

