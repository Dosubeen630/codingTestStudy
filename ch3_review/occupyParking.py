# https://dmoj.ca/problem/ccc18j2
# 입장이 주차 관리인 임. 어제 오늘 연속 으로 파킹된 자리 찾기!

PARKING = "C"
EMPTY = "."
parking_space = input()
if not parking_space.isdigit(): exit(f"{parking_space} != digit")
parking_space = int(parking_space)
if not 1 <= parking_space <= 100: exit(f"{parking_space} 범위를 벗어남(1<=n<=100)")

yesterday = input()
if yesterday.count(PARKING) + yesterday.count(EMPTY) != parking_space:
    exit("잘못된 입력 값('C','.' 만 입력 가능, parking_space 만큼 입력 가능)")
today = input()
if today.count(PARKING) + today.count(EMPTY) != parking_space:
    exit("잘못된 입력 값('C','.' 만 입력 가능, parking_space 만큼 입력 가능)")

both_parking_space = 0

for i in range(parking_space):
    if yesterday[i] == PARKING and yesterday[i] == today[i]:
        both_parking_space += 1
    else:
        pass

print(both_parking_space)
