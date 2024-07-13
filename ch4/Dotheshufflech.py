# https://dmoj.ca/problem/ccc08j2
# 문자열 자르기 사용하여 바꾼 버젼
music_playlist = "ABCDE"
button_num = 0
while button_num != 4: # 4번 버튼을 누른 것이 아니면 아래와 같은 작업을 반복 수행한다.
# 입력값 유효성 체크
    button_num = input()
    if not button_num.isdigit(): exit(f"{button_num}의 입력 형식은 숫자 입니다. 숫자로 입력 해 주세요.")
    button_num = int(button_num)
    if not 1 <= button_num <= 4: exit(f"{button_num}의 범위가 벗어 났습니다.")

    push_button = input()
    if not push_button.isdigit(): exit(f"{push_button}의 입력 형식은 숫자 입니다. 숫자로 입력 해 주세요.")
    push_button = int(push_button)
    if not 1 <= push_button <= 10: exit(f"{push_button}의 범위가 벗어 났습니다.")

    for i in range(push_button):
        if button_num == 1:
            music_playlist = music_playlist[1:]+music_playlist[0]

        elif button_num == 2:
            music_playlist = music_playlist[-1]+ music_playlist[:-1]

        elif button_num == 3:
            music_playlist = music_playlist[1]+ music_playlist[0] + music_playlist[2:]

        else: # button_num == 4 # music_playlist를 그대로 출력하면 공백이 나오지 않음. 그 문제를 for문과 if문 사용하여 공백 추가하여 출력
            result = None
            for c in music_playlist:
                if result is None:
                    result = c
                else:
                    result += " " + c
            print(result)

