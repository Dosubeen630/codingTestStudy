# https://dmoj.ca/problem/coci06c5p1
# 프로그래머들이 그의 움직임을 기록 중 -> 컨텍스트
# output the index of the cup -> 목적
# 향후 도메인이 공의 위치가 아닌 공이 없는 컵을 고르거나 공을 추적할 가능 성 높음.

moves = input()
if moves.count("A") + moves.count("B") + moves.count("C") != len(moves):
    exit("문자열에 A,B,C 이외의 문자가 있음")

cups = "123"

for move in moves:
    if move == "A":
        cups = cups[1] + cups[0] + cups[2]
    elif move == "B":
        cups = cups[0] + cups[2] + cups[1]
    else: # move == "C"
        cups = cups[2] + cups[1] + cups[0]


print(cups.find('1')+1)