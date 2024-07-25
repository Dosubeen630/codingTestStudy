# https://dmoj.ca/problem/ccc08j2
# 음악 플레이 해주는 기계 : "A,B,C,D,E" 다섯 가지 노래만 저장 되어 있음.
# 기계 에는 4가지 버튼 있음. 버튼 1: A가 플레이 리스트 맨 마지막 으로 감.
# 버튼 2: 플레이 리스트 맨 끝 E가 맨 앞으로 옴. 버튼 3: 플레이 리스트의 처음 두개의 위치가 바뀜.
# 버튼 4는 플레이 리스트 재정렬을 멈추고 플레이 리스트를 출력 해줌.
# 버튼 넘버가 먼저 오고 그 다음 줄에는 그 버튼을 누른 횟수가 나옴. 4번 버튼은 무조건 1번만 누르고 그러면 종료 됨.
# 4를 제외한 모든 버튼은 5번 누르면 제자리로 돌아옴.

play_list = "ABCDE"
button_num = 0
while button_num != 4:

    button_num = input()
    if not button_num.isdigit() : exit(f"{button_num} != digit")
    button_num = int(button_num)
    if not 1 <= button_num <= 4: exit(f"범위 벗어남 ( 1<= {button_num} <= 4)")

    press_time = input()
    if not press_time.isdigit() : exit(f"{press_time} != digit")
    press_time = int(press_time)
    if not 1 <= press_time <= 10: exit(f"범위 벗어남 ( 1<= {press_time} <= 10)")

    #if button == 4 and count == 1: exit(f" 4번 버튼은 오직 1번만 누를 수 있습 니다.")
    for i in range(press_time):
        if button_num == 1 :
            play_list = play_list[1:] + play_list[0]
        elif button_num == 2 :
            play_list = play_list[-1] + play_list[:-1]
        elif button_num == 3 :
            play_list = play_list[1] + play_list[0]+ play_list[2:]
        else:
            result = None
            for c in play_list:
                if result is not None:
                    result += " " + c
                else:
                    result = c
            print(result)



