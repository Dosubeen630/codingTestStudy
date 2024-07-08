# https://dmoj.ca/problem/coci06c5p1 문제 링크
# 도메인 분석 :
# Jealous of Mirko's position as head of the village ,
# Borko stormed into his tent and tried to demonstrate Mirko's incompetence for leadership with a trick.
# Mirko 는 마을의 대장,  Borko 는 무방비한 Mirko의 텐트를 속임수를 써서 무너뜨리려는 시도를 한다.
# Borko puts three opaque cups onto the table next to each other (opening facing down) and a small ball under the leftmost cup.
# 보르코는 3개의 opaque cups을 테이블 위에서 서로 옆에 두게 놔두고, 컵을 젖혀서 작은 숫자가 적힌 공을 왼쪽의 컵 안에 넣는다.
# He then swaps two cups in one of three possible ways a number of times.
# 그는 많은 방법으로 두 컵의 위치를 바꿀 수 있다.
# Mirko has to tell which cup the ball ends up under.
# 마르코는 컵의 위치가 바뀐 것이 끝난 다음에 어느 컵에 공이 있는지 말할 수 있다.
# What Borko does not know is that programmers in the back are recording all his moves and will use a simple program to determine where the ball is.
# 보르코는 프로그래머가 뒤에서 모든 그의 움직임을 녹화 하고 있는 것을  모르고 있다. 그리고 간단한 프로그램을 사용하여 어느 곳에 공이 있는지 알수 있는 것을 모른다.
# Write that program.
# 그 프로그램을 써보아라.
# 입력 란에 한 줄만 50개 문자 넘으면 안됨. 보르코의 움직임은 각각 A,B or C로 나타냄.
# 출력란에서 볼이 있는 컵의 인덱스가 출력 되어야함.
# 1은 왼쪽 컵 아래에 볼이 있으면, 2는 가운데 컵에 볼이 있으면, 3은 오른쪽 컵에 볼이 있으면을 나타냄.

Borko_moves = input()
if not Borko_moves.isalpha():
    exit("입력값이 잘못 되었습니다.")
if len(Borko_moves) > 50:
    exit("입력값의 개수가 너무 큽니다.")


left_cup_under = 1
middle_cup_under = 2
right_cup_under = 3

# 볼의 위치
small_ball_location = left_cup_under

# 보르코의 움직임 (컵 위치 변경 경우)
# Borko_move_type = 'A' == left_cup and middle_cup swap
# Borko_move_type = 'B' == middle_cup and right_cup swap
# Borko_move_type = 'C' == right_cup  and left_cup swap

# 보르코의 움직임 중에서
for Borko_moves_type in Borko_moves:
    if Borko_moves_type == 'A':
        if small_ball_location == 1:
            small_ball_location = 2
        elif small_ball_location == 2:
            small_ball_location = 1
        else: # 3
            pass
    elif Borko_moves_type == 'B':
        if small_ball_location == 1:
            pass
        elif small_ball_location == 2:
            small_ball_location = 3
        else: # 3
            small_ball_location = 2
    else: # C
        if small_ball_location == 1:
            small_ball_location = 3
        elif small_ball_location == 2:
            pass
        else: # 3
            small_ball_location = 1

print(small_ball_location)


