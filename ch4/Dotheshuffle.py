# https://dmoj.ca/problem/ccc08j2
# Those tiny music machines that play your digital music are really computers that keep track of and play music files.
# 디지털 음악을 재생하는 작은 음악기계는 실제로 음악 파일을 추적하고 재생하는 컴퓨터 입니다.
#  The CCC music player (C3MP) is currently in development and will be hitting the stores soon! In this problem, you have to simulate a C3MP.
# CCC 뮤직 플레이어(C3MP)는 현재 개발 중이며 곧 출시 될 예정입니다. 이 문제에서는 C3MP를 시뮬레이션 해야합니다.
# The C3MP music player will hold 5 songs in memory, whose titles will always be "A", "B", "C", "D" and "E".
# C3MP 음악 플레이어는 5개의 노래를 메모리에 저장하며 제목은 항상 "A", "B", "c","D", "ㅌ" 입니다.
# The C3MP also keeps track of a playlist, which is an ordering of all the songs.
# C3MP는 또한 모든 노래의 순서를 나타내는 재생 목록을 추적 합니다.
# The C3MP has 4 buttons that the user will press to rearrange the playlist and play the songs.
# C3MP 에는 사용자가 재생 목록을 재정렬 하기 위해 누르는 버튼은 4개가 있습니다.
# Initially, the C3MP playlist is "A, B, C, D, E". The 4 control buttons do the following:
# 처음에 C3MP 재생 목록은"A"B"C""D""E" 입니다. 4개의 제어 버튼은 다음을 수행 합니다.
# Button 1: move the first song of the playlist to the end of the playlist.
# For example: "A, B, C, D, E" will change to "B, C, D, E, A".
# 버튼 1: 재생 목록의 첫번째 노래를 재생 목록을 끝으로 이동 합니다. 예를 들어, "A, B, C, D, E"는 "B, C, D, E, A"로 변경 됩니다.
# Button 2: move the last song of the playlist to the start of the playlist.
# For example, "A, B, C, D, E" will change to "E, A, B, C, D".
# 버튼 2: 재생 목록의 마지막 노래를 재생 목록의 시작 부분 으로 이동 합니다. 예를 들어 "A, B, C, D, E"는 "E, A, B, C, D"로 변경 됩니다.
# Button 3: swap the first two songs of the playlist.
# For example, "A, B, C, D, E" will change to "B, A, C, D, E".
# 버튼 3: 재생 목록의 처음 두 곡을 바꿉니다. 예를 들어, "A, B, C, D, E"는 "B, A, C, D, E"로 변경됩니다.
# Button 4: stop rearranging songs and output the playlist.
# 버튼 4: 노래 재배열을 중지 하고 재생 목록을 출력 합니다.
# You need to write a program to simulate a CCC music player. Your program should repeatedly ask for two positive integers b and n.
# Here b represents the button number that the user wants to press, 1 <= b < 4, and n represents the number of times that the user wants to press button b.
# CCC 뮤직 플레이어 를 시뮬레이션 하려면 프로그램을 작성 해야 합니다. 프로그램은 두 개의 양의 정수 b and n을 반복적 으로 요청 해야 합니다.
# 여기서 b는 사용자가 누르려는 버튼 번호를 나타내고, 1 <=b <= 4 이며, n은 사용자가 b버튼을 누르 려는 횟수를 나타 냅니다.
# You can assume that n always satisfies 1 <= n <= 10.
# n은 항상 1 <= n <= 10을 만족한다고 가정할 수 있습니다.
# The input will always finish with the pair of inputs ( b=4, n=1) when this happens, you should print the order of songs in the current playlist and your program should end.
# 입력은 항상 입력 쌍 (b=4, n=1)으로 완료 됩니다. 이 경우 현재 재생 목록에 있는 노래의 순서를 인쇄해야 하며 프로그램이 종료 되어야 합니다.
# You can assume that the user will only ever press button 4 once.
# 사용자가 버튼 4를 한번 만 누른다고 가정 할 수 있습니다.

# 도메인 분석 :  플레이 리스트 : "A,B,C,D,E'가 있습니다. 버튼은 4가지가 있고 버튼 1을 누르면 노래 리스트의 첫번째가 리스트의 마지막으로 이동합니다.
# 버튼 2를 누르면 노래 리스트의 마지막이 리스트의 맨 앞으로 이동 합니다. 버튼 3을 누르면 리스트의 앞,과 바로 뒤의 위치가 바뀐다.
# 버튼 4를 누르면 리스트 정렬을 그만 하고 노래 목록 리스트를 출력 합니다.
# 버튼을 누른 횟수에 따라서 각 버튼이 수행하는 일을 차례대로 수행한다. 버튼 4를 누르면 반복 작업을 종료하고 리스트를 출력하며 마친다.

music_playlist = "ABCDE"
button_num = 0
while button_num != 4: # 4번 버튼을 누른 것이 아니면 아래와 같은 작업을 반복 수행한다.
# 입력값 유효성 체크
    button_num = input()
    if not button_num.isdigit(): exit(f"{button_num} != digit")
    button_num = int(button_num)
    if not 1 <= button_num <= 4: exit(f" 1 <= {button_num} <= 4")

    push_button = input()
    if not push_button.isdigit(): exit(f"{push_button} != digit")
    push_button = int(push_button)
    if not 1 <= push_button <= 10: exit(f" 1 <= {push_button} <= 10")

    for i in range(push_button):
        if button_num == 1:
            music_playlist = music_playlist[1]+ music_playlist[2]+music_playlist[3]+music_playlist[4]+music_playlist[0]

        elif button_num == 2:
            music_playlist = music_playlist[4]+ music_playlist[0]+ music_playlist[1]+ music_playlist[2]+music_playlist[3]

        elif button_num == 3:
            music_playlist = music_playlist[1]+ music_playlist[0] + music_playlist[2]+ music_playlist[3]+music_playlist[4]

        else: # button == 4 # music_playlist를 그대로 출력하면 공백이 나오지 않음. 그 문제를 for문과 if문 사용하여 공백 추가하여 출력
            result = None
            for c in music_playlist:
                if result is None:
                    result = c
                else:
                    result += " " + c
            print(result)

