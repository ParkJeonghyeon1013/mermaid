import random
import time
from c1_character import mermaid
from c3_pearlshell import mini2_NPC

# 가위바위보 모듈
def rps():
    while True:
        ai_rps = random.randrange(1,4)
        me_rps = str(input("\n가위, 바위, 보 中 낼 것을 입력해주세요!\n"))

        if me_rps == '가위' and ai_rps == 1:
            print("[{0}] 인어: {1} vs [진주아이]: 가위\n결과: 무승부".format(mermaid.name, me_rps))
            continue
        elif me_rps == '가위' and ai_rps == 2:
            print("[{0}] 인어: {1} vs [진주아이]: 바위\n결과: 진주아이 승".format(mermaid.name, me_rps))
            return 1
        elif me_rps == '가위' and ai_rps == 3:
            print("[{0}] 인어: {1} vs [진주아이]: 보\n결과: [{2}] 인어 승".format(mermaid.name, me_rps, mermaid.name))
            return 2

        # 내가 바위 냈을 때
        elif me_rps == '바위' and ai_rps == 1:
            print("[{0}] 인어: {1} vs [진주아이]: 가위\n결과: [{2}] 인어 승".format(mermaid.name, me_rps, mermaid.name))
            return 2
        elif me_rps == '바위' and ai_rps == 2:
            print("[{0}] 인어: {1} vs [진주아이]: 바위\n결과: 무승부".format(mermaid.name, me_rps))
            continue
        elif me_rps == '바위' and ai_rps == 3:
            print("[{0}] 인어: {1} vs [진주아이]: 보\n결과: 진주아이 승".format(mermaid.name, me_rps))
            return 1

        # 내가 보 냈을 때
        elif me_rps == '보' and ai_rps == 1:
            print("[{0}] 인어: {1} vs [진주아이]: 가위\n결과: 진주아이 승".format(mermaid.name, me_rps))
            return 1
        elif me_rps == '보' and ai_rps == 2:
            print("[{0}] 인어: {1} vs [진주아이]: 바위\n결과: [{2}] 인어 승".format(mermaid.name, me_rps, mermaid.name))
            return 2
        elif me_rps == '보' and ai_rps == 3:
            print("[{0}] 인어: {1} vs [진주아이]: 보\n결과: 무승부".format(mermaid.name, me_rps))
            continue

        # 걍 이상
        else:
            print("올바르게 입력해주세요.")
            continue
        # 내가 가위 냈을 때

# 게임 모듈 (1) - 공격
# 아이들과의 게임 1 - 청기백기 게임 / 3판2선승제
# 승리시 피해 없지만, 아이들이 울어 사탕을 사줘야 함.
def minigame2_1_att ():
    flag_list = ["청기 올려", "백기 올려", "청기 내려", "백기 내려", "청기올리지 말고 백기올려", "백기올리지 말고 청기올려", "청기올리지 말고 백기내려", "백기올리지 말고 청기내려" ]

    win = 0
    lose = 0

    print("\n------------------------------------------------------------------------------\n")
    print("[{0}] 인어: 이번엔 제가 공격이에요!".format(mermaid.name))


    for mininum2_1 in range(1, 6, 1):
        input("\n------------------------------------------------------------------------------\n")
        print("<<< 공격 {0} >>>".format(mininum2_1))

        while True:
            print("1- {0} / 2- {1} / 3- {2} / 4- {3}\n5- {4} / 6- {5}\n7- {6} / 8- {7}\n".format(flag_list[0], flag_list[1], flag_list[2], flag_list[3], flag_list[4], flag_list[5], flag_list[6], flag_list[7]))
            flag_command = str(input("[{0}] 인어: 공격 명령을 입력해주세요!\n".format(mermaid.name)))

            # 8가지의 상황
            if flag_command == '1':
                print("\n------------------------------------------------------------------------------\n")
                flag_act = random.randrange(1, 5)
                print("[{0}] 인어: 청기 올려!".format(mermaid.name))
                if flag_act == 1:
                    print("[진주 아이]: 휙! (; 청기를 올린다")
                    win += 1
                    break
                else:
                    print("[진주 아이]: 휙! ): 백기를 올린다")
                    lose += 1
                    break

            elif flag_command == '2':
                print("\n------------------------------------------------------------------------------\n")
                flag_act = random.randrange(1, 5)
                print("[{0}] 인어: 백기 올려!".format(mermaid.name))
                if flag_act == 1:
                    print("[진주 아이]: 휙! (; 백기를 올린다")
                    win += 1
                    break
                else:
                    print("[진주 아이]: 휙! ): 청기를 올린다")
                    lose += 1
                    break
                    
            elif flag_command == '3':
                print("\n------------------------------------------------------------------------------\n")
                flag_act = random.randrange(1, 5)
                print("[{0}] 인어: 청기 내려!".format(mermaid.name))
                if flag_act == 1:
                    print("[진주 아이]: 휙! (; 청기를 내린다")
                    win += 1
                    break
                else:
                    print("[진주 아이]: 휙! ): 백기를 내린다")
                    lose += 1
                    break
                    
            elif flag_command == '4':
                print("\n------------------------------------------------------------------------------\n")
                flag_act = random.randrange(1, 5)
                print("[{0}] 인어: 백기 내려!".format(mermaid.name))
                if flag_act == 1:
                    print("[진주 아이]: 휙! (; 백기를 내린다")
                    win += 1
                    break
                else:
                    print("[진주 아이]: 휙! ): 청기를 내린다")
                    lose += 1
                    break
                    
            elif flag_command == '5':
                print("\n------------------------------------------------------------------------------\n")
                flag_act = random.randrange(1, 5)
                print("[{0}] 인어: 청기올리지 말고 백기올려!".format(mermaid.name))
                if flag_act == 1:
                    print("[진주 아이]: 휙! (; 백기를 올린다")
                    win += 1
                    break
                else:
                    print("[진주 아이]: 휙! ): 청기를 올린다")
                    lose += 1
                    break
                    
            elif flag_command == '6':
                print("\n------------------------------------------------------------------------------\n")
                flag_act = random.randrange(1, 5)
                print("[{0}] 인어: 백기올리지 말고 청기올려".format(mermaid.name))
                if flag_act == 1:
                    print("[진주 아이]: 휙! (; 청기를 올린다")
                    win += 1
                    break
                else:
                    print("[진주 아이]: 휙! ): 백기를 올린다")
                    lose += 1
                    break
                    
            elif flag_command == '7':
                print("\n------------------------------------------------------------------------------\n")
                flag_act = random.randrange(1, 5)
                print("[{0}] 인어: 청기올리지 말고 백기내려".format(mermaid.name))
                if flag_act == 1:
                    print("[진주 아이]: 휙! (; 백기를 내린다")
                    win += 1
                    break
                else:
                    print("[진주 아이]: 휙! ): 청기를 내린다")
                    lose += 1
                    break
                    
            elif flag_command == '8':
                print("\n------------------------------------------------------------------------------\n")
                flag_act = random.randrange(1, 5)
                print("[{0}] 인어: 백기올리지 말고 청기내려".format(mermaid.name))
                if flag_act == 1:
                    print("[진주 아이]: 휙! (; 청기를 내린다")
                    win += 1
                    break
                else:
                    print("[진주 아이]: 휙! ): 백기를 내린다")
                    lose += 1
                    break

            else:
                print("\n------------------------------------------------------------------------------\n")
                print("공격 명령이 틀렸습니다.")
                continue
    
    return win


# 게임 모듈 (1) - 수비
def minigame2_1_def ():

    win = 0
    lose = 0

    children1 = mini2_NPC("[진주 아이]", 0, 0, 0)
    print("\n------------------------------------------------------------------------------\n")
    print("[{0}] 인어: 이번엔 제가 수비예요!\n".format(mermaid.name))
    print("청기 올리기 - b / 청기 내리기 - bb\n백기 올리기 - n / 백기 내리기 - nn\n")
    print("3초 안에 입력하세요.")

    for mininum2_1 in range(1, 6, 1):
        input("\n수비 {0}------------------------------------------------------------------------\n".format(mininum2_1))

        flag_command = random.randrange(1, 9)
        
        s = time.ctime()
        second = int(s[17])*10+int(s[18])+60
        timer = second+3
        
        # 8가지의 상황 - 청기 올려
        if flag_command == 1:
            flag_act = str(input("[진주 아이]: 청기 올려!\n"))
            after_entering = time.ctime()
            game = int(after_entering[17]) * 10 + int(after_entering[18]) + 60
            print("second: {0}/ timer: {1}/ game: {2}".format(second, timer, game))
            
            if flag_act == 'b':
                
                # 게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
                if game <= second:
                    game += 60
                    print("game: {0}".format(game))
                    
                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                            
                    elif game <= timer:
                        print("[{0}]: 휙! (; 청기를 올린다".format(mermaid.name))
                        win += 1
                            
                # 일반적인 경우         
                elif game > second:
                    print("second: {0}/ game: {1}".format(second,game))

                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("{0}초 초과해 실패".format(game-timer))
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                  
                    elif game <= timer:
                        print("[{0}]: 휙! (; 청기를 올린다".format(mermaid.name))
                        win += 1
                        
            elif flag_act == 'bb':
                print("[{0}]: 휙! :( 청기를 내린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'n':
                print("[{0}]: 휙! :( 백기를 올린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'nn':
                print("[{0}]: 휙! :( 백기를 내린다".format(mermaid.name))                
                lose += 1
            else:
                print("[{0}] 인어: 휙! ): 뭔가 잘못올렸다.".format(mermaid.name))
                lose += 1
                
        # 8가지의 상황 - 백기 올려
        elif flag_command == 2:
            flag_act = str(input("[진주 아이]: 백기 올려!\n"))
            after_entering = time.ctime()
            game = int(after_entering[17]) * 10 + int(after_entering[18]) + 60
            print("second: {0}/ timer: {1}/ game: {2}".format(second, timer, game))
            
            if flag_act == 'n':
                
                # 게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
                if game <= second:
                    game += 60
                    print("game: {0}".format(game))
                    
                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                            
                    elif game <= timer:
                        print("[{0}]: 휙! (; 백기를 올린다".format(mermaid.name))
                        win += 1
                            
                # 일반적인 경우         
                elif game > second:
                    print("second: {0}/ game: {1}".format(second,game))

                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("{0}초 초과해 실패".format(game-timer))
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                  
                    elif game <= timer:
                        print("[{0}]: 휙! (; 백기를 올린다".format(mermaid.name))
                        win += 1
                        
            elif flag_act == 'b':
                print("[{0}]: 휙! :( 청기를 올린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'bb':
                print("[{0}]: 휙! :( 청기를 내린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'nn':
                print("[{0}]: 휙! :( 백기를 내린다".format(mermaid.name))                
                lose += 1
            else:
                print("[{0}] 인어: 휙! ): 뭔가 잘못 올렸다.".format(mermaid.name))
                lose += 1

        # 8가지의 상황 - 청기 내려
        elif flag_command == 3:
            flag_act = str(input("[진주 아이]: 청기 내려!\n"))
            after_entering = time.ctime()
            game = int(after_entering[17]) * 10 + int(after_entering[18]) + 60
            print("second: {0}/ timer: {1}/ game: {2}".format(second, timer, game))
            
            if flag_act == 'bb':
                
                # 게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
                if game <= second:
                    game += 60
                    print("game: {0}".format(game))
                    
                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                            
                    elif game <= timer:
                        print("[{0}]: 휙! (; 청기를 내린다".format(mermaid.name))
                        win += 1
                            
                # 일반적인 경우         
                elif game > second:
                    print("second: {0}/ game: {1}".format(second,game))

                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("{0}초 초과해 실패".format(game-timer))
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                  
                    elif game <= timer:
                        print("[{0}]: 휙! (; 청기를 내린다".format(mermaid.name))
                        win += 1
                        
            elif flag_act == 'b':
                print("[{0}]: 휙! :( 청기를 올린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'n':
                print("[{0}]: 휙! :( 백기를 올린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'nn':
                print("[{0}]: 휙! :( 백기를 내린다".format(mermaid.name))                
                lose += 1
            else:
                print("[{0}] 인어: 휙! ): 뭔가 잘못올렸다.".format(mermaid.name))
                lose += 1

        # 8가지의 상황 - 백기 내려
        elif flag_command == 4:
            flag_act = str(input("[진주 아이]: 백기 내려!\n"))
            after_entering = time.ctime()
            game = int(after_entering[17]) * 10 + int(after_entering[18]) + 60
            print("second: {0}/ timer: {1}/ game: {2}".format(second, timer, game))
            
            if flag_act == 'nn':
                
                # 게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
                if game <= second:
                    game += 60
                    print("game: {0}".format(game))
                    
                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                            
                    elif game <= timer:
                        print("[{0}]: 휙! (; 백기를 내린다".format(mermaid.name))
                        win += 1
                            
                # 일반적인 경우         
                elif game > second:
                    print("second: {0}/ game: {1}".format(second,game))

                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("{0}초 초과해 실패".format(game-timer))
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                  
                    elif game <= timer:
                        print("[{0}]: 휙! (; 백기를 내린다".format(mermaid.name))
                        win += 1
                        
            elif flag_act == 'bb':
                print("[{0}]: 휙! :( 청기를 내린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'b':
                print("[{0}]: 휙! :(  청기를 올린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'n':
                print("[{0}]: 휙! :( 백기를 올린다".format(mermaid.name))
                lose += 1
            else:
                print("[{0}] 인어: 휙! ): 뭔가 잘못올렸다.".format(mermaid.name))
                lose += 1

        # 8가지의 상황 - 청기올리지 말고 백기올려
        elif flag_command == 5:
            flag_act = str(input("[진주 아이]: 청기올리지 말고 백기올려!\n"))
            after_entering = time.ctime()
            game = int(after_entering[17]) * 10 + int(after_entering[18]) + 60
            print("second: {0}/ timer: {1}/ game: {2}".format(second, timer, game))

            if flag_act == 'n':
                
                # 게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
                if game <= second:
                    game += 60
                    print("game: {0}".format(game))
                    
                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                            
                    elif game <= timer:
                        print("[{0}]: 휙! (; 백기를 올린다".format(mermaid.name))
                        win += 1
                            
                # 일반적인 경우         
                elif game > second:
                    print("second: {0}/ game: {1}".format(second,game))

                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("{0}초 초과해 실패".format(game-timer))
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                  
                    elif game <= timer:
                        print("[{0}]: 휙! (; 백기를 올린다".format(mermaid.name))
                        win += 1
                        
            elif flag_act == 'bb':
                print("[{0}]: 휙! :( 청기를 내린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'b':
                print("[{0}]: 휙! :(  청기를 올린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'nn':
                print("[{0}]: 휙! :(  백기를 내린다".format(mermaid.name))                
                lose += 1
            else:
                print("[{0}] 인어: 휙! ): 뭔가 잘못올렸다.".format(mermaid.name))
                lose += 1

        # 8가지의 상황 - 백기올리지 말고 청기올려
        elif flag_command == 6:
            flag_act = str(input("[진주 아이]: 백기올리지 말고 청기올려!\n"))
            after_entering = time.ctime()
            game = int(after_entering[17]) * 10 + int(after_entering[18]) + 60
            print("second: {0}/ timer: {1}/ game: {2}".format(second, timer, game))

            if flag_act == 'b':
                
                # 게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
                if game <= second:
                    game += 60
                    print("game: {0}".format(game))
                    
                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                            
                    elif game <= timer:
                        print("[{0}]: 휙! (; 청기를 올린다".format(mermaid.name))
                        win += 1
                            
                # 일반적인 경우         
                elif game > second:
                    print("second: {0}/ game: {1}".format(second,game))

                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("{0}초 초과해 실패".format(game-timer))
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                  
                    elif game <= timer:
                        print("[{0}]: 휙! (; 청기를 올린다".format(mermaid.name))
                        win += 1
                        
            elif flag_act == 'bb':
                print("[{0}]: 휙! :(  청기를 내린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'n':
                print("[{0}]: 휙! :(  백기를 올린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'nn':
                print("[{0}]: 휙! :(  백기를 내린다".format(mermaid.name))                
                lose += 1
            else:
                print("[{0}] 인어: 휙! ): 뭔가 잘못올렸다.".format(mermaid.name))
                lose += 1

        # 8가지의 상황 - 청기올리지 말고 백기내려
        elif flag_command == 7:
            flag_act = str(input("[진주 아이]: 청기올리지 말고 백기내려!\n"))
            after_entering = time.ctime()
            game = int(after_entering[17]) * 10 + int(after_entering[18]) + 60
            print("second: {0}/ timer: {1}/ game: {2}".format(second, timer, game))
            
            if flag_act == 'nn':
                
                # 게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
                if game <= second:
                    game += 60
                    print("game: {0}".format(game))
                    
                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                            
                    elif game <= timer:
                        print("[{0}]: 휙! (; 백기를 내린다".format(mermaid.name))
                        win += 1
                            
                # 일반적인 경우         
                elif game > second:
                    print("second: {0}/ game: {1}".format(second,game))

                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("{0}초 초과해 실패".format(game-timer))
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                  
                    elif game <= timer:
                        print("[{0}]: 휙! (; 백기를 내린다".format(mermaid.name))
                        win += 1
                        
            elif flag_act == 'bb':
                print("[{0}]: 휙! :( 청기를 내린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'n':
                print("[{0}]: 휙! :( 백기를 올린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'b':
                print("[{0}]: 휙! :(  청기를 올린다".format(mermaid.name))                
                lose += 1
            else:
                print("[{0}] 인어: 휙! :(  뭔가 잘못올렸다.".format(mermaid.name))
                lose += 1

        # 8가지의 상황 - 백기올리지 말고 청기내려
        elif flag_command == 8:
            flag_act = str(input("[진주 아이]: 백기올리지 말고 청기내려!\n"))
            after_entering = time.ctime()
            game = int(after_entering[17]) * 10 + int(after_entering[18]) + 60
            print("second: {0}/ timer: {1}/ game: {2}".format(second, timer, game))
            
            if flag_act == 'bb':
                
                # 게임 시작할 때의 시간이 56 57 58 59 였을 때 후에 받는 after 시간이 1,2,3이 됨으로 60을 한 번 더 더해줘야 함
                if game <= second:
                    game += 60
                    print("game: {0}".format(game))
                    
                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                            
                    elif game <= timer:
                        print("[{0}]: 휙! (; 청기를 내린다".format(mermaid.name))
                        win += 1
                            
                # 일반적인 경우         
                elif game > second:
                    print("second: {0}/ game: {1}".format(second,game))

                    # 제한 시간 내에 성공, 실패
                    if game > timer:
                        print("{0}초 초과해 실패".format(game-timer))
                        print("[{0}] 인어: 휘..익 휙! ): 늦었다...".format(mermaid.name))
                        lose += 1
                  
                    elif game <= timer:
                        print("[{0}]: 휙! (; 청기를 내린다".format(mermaid.name))
                        win += 1
                        
            elif flag_act == 'b':
                print("[{0}]: 휙! :( 청기를 올린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'n':
                print("[{0}]: 휙! :( 백기를 올린다".format(mermaid.name))
                lose += 1
            elif flag_act == 'nn':
                print("[{0}]: 휙! :( 백기를 내린다".format(mermaid.name))                
                lose += 1
            else:
                print("[{0}] 인어: 휙! ): 뭔가 잘못올렸다.".format(mermaid.name))
                lose += 1

    return win


# 게임 모듈 (2) - 공격
# 아이들과의 게임 2 - 통아저씨 게임 / 3판2선승제
# 승리시 피해 없지만, 10코인을 덜 받는다.
def minigame2_2_att ():
    children1 = mini2_NPC("[진주 아이]", 0, 0, 0)
    knife = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    boom = random.choice(knife)

    print("Boom 번호: {0}".format(boom))
    print("\n[{0}] 인어: 저부터 시작할게요!".format(mermaid.name))

    for i in range(1, 16, 1):
        input("\n------------------------------------------------------------------------------\n")
        print("<<<{0}번째 턴>>>".format(i))

        # 인어 선택
        while True:
            mer_pick = int(input("\n[{0}] 인어:\n{1} 중 하나의 칼을 선택해주세요!\n".format(mermaid.name, knife)))

            # 숫자가 입력되었을 때
            if mer_pick in knife:
                if boom == int(mer_pick):
                    print("튕! 통아저씨가 튀어올랐습니다.\n[{0}] 인어 패배".format(mermaid.name))
                    return children1.name

                else:
                    print("[{0}] 인어 통과".format(mermaid.name))
                    knife.remove(mer_pick)

                    # 진주 아이 선택
                    child_pick = random.choice(knife)
                    print("\n[진주 아이]: 저는 {0}번 칼을 꽂아볼래요!".format(child_pick))

                    if boom == child_pick:
                        print("튕! 통아저씨가 튀어올랐습니다.\n[진주아이] 패배")
                        return mermaid.name
                    else:
                        print("[진주 아이] 통과")
                        knife.remove(child_pick)
                        continue
            else:
                print("다른 칼을 골라주세요!")
                continue

# 게임 모듈 (2) - 수비
def minigame2_2_def ():
    children1 = mini2_NPC("[진주 아이]", 0, 0, 0)
    knife = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    boom = random.choice(knife)
    print("Boom 번호: {0}".format(boom))

    for i in range(1, 16, 1):
        input("\n------------------------------------------------------------------------------\n")
        print("<<<{0}번째 턴>>>".format(i))

        # 진주 아이 선택
        child_pick = random.choice(knife)
        print("[진주 아이]: {0}번 칼을 꽂아볼게요!".format(child_pick))

        if boom == child_pick:
            print("튕! 통아저씨가 튀어올랐습니다.\n[진주아이] 패배")
            return mermaid.name
        else:
            print("[진주 아이] 통과")
            knife.remove(child_pick)

            while True:
                # 인어 선택
                mer_pick = int(input("[{0}] 인어:\n{1} 중 하나의 칼을 선택해주세요!\n".format(mermaid.name, knife)))

                if mer_pick in knife:
                    if boom == int(mer_pick):
                        print("튕! 통아저씨가 튀어올랐습니다.\n[{0}] 인어 패배".format(mermaid.name))
                        return children1.name

                    else:
                        print("[{0}] 인어 통과".format(mermaid.name))
                        knife.remove(mer_pick)
                        continue

                else:
                    print("다른 칼을 골라주세요!")
                    continue

# 게임 모듈 (3)
# 진주 잃은 조개가 쳐들어오는데 사장은 튀튀 = 인어 눈물을 잘 활용해보라고 이야기 함
# 지는 가위바위보로 달래주기 + 인어 눈물은 진주를 만들어내기 때문에 주기3은 미역 발견

def minigame2_3 ():
    print("지는 가위바위보")


# 신고 여부 모듈
# [조개들의 사연 이야기를 들을지 말지 - 안들으면 kill 포인트가 쌓임.]
# [신고할지 말지 - 신고안하면 kill 포인트 10 쌓임 | 신고하면 그들이 고맙다며 10코인을 줌]

def minigame2_4 ():
    print("조개 사연 들을지 말지")
    print("신고할지 말지")
