import random
import time





'''
now = datetime.datetime.now()
print(now)          # 2018-07-28 12:11:32.669083

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)      # 2018-07-28
 
nowTime = now.strftime('%H:%M:%S')
print(nowTime)      # 12:11:32
 
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)  # 2018-07-28 12:11:32
'''
class minigame(stagenum):
    def stage1_game():
       #second = 현재 시간을 받는거임
        s= time.ctime()
        second =int(s[17])*10+int(s[18])+60
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
