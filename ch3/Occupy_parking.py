# https://dmoj.ca/problem/ccc18j2
# You supervise a small parking lot which has parking spaces.
# 당신은 작은 주차공간을 가진 주차장에 놀랍니다.
# Yesterday, you recorded which parking spaces were occupied by cars and which were empty.
# 어제, 당신은 어떤 주차공간이 사용되어지고, 어떤 주차공간이 비었는지 기록했습니다.
# Today, you recorded the same information.
# 오늘, 당신은 같은 정보를 가지고 있습니다.
# How many of the parking spaces were occupied both yesterday and today?
# 어제와 오늘 얼마나 많은 주차공간이 사용되어졌는지 알아보자.
# 입력 첫번째 줄에는 N(1<=N<=100)이 입력되어짐. 두번째, 세번째 줄에는 첫번째 줄에 입력된 N의 수만큼 C가 입력됨.
# 두번째 줄에는 어제 기록된 주차장 공간의 사용내역이 그리고 세번째 줄에는 오늘 기록된 주차장 공간의 사용내역을 의미한다.
# 각각의 2N은 C는 사용된 공간을, .은 빈 주차공간을 의미한다.
# 출력은 어제와 오늘 모두에서 사용된 주차공간의 수를 출력해야한다.

# 우선 주차공간 space, 어제 사용된 주차공간 yesterday_occupied, 오늘 사용된 주차공간 today_occupied 입력받음.
PARKED = 'C'
EMPTY = '.'  # 변하지 않는 값으로 상수로 선언!
space = input()
if not space.isdigit():
    exit("입력 값이 잘못 되었습니다.")
space = int(space)
if not 0 <= space <= 100:
    exit("범위를 벗어 납니다.(0 <= n <= 100)")

yesterday_occupied = input()
if yesterday_occupied.count(PARKED) + yesterday_occupied.count(EMPTY) != space:
    exit("입력 값이 잘못 되었습니다.('C','.'만 입력 가능, space만큼 입력 필요)")

today_occupied = input()
if today_occupied.count(PARKED) + today_occupied.count(EMPTY) != space:
    exit("입력 값이 잘못 되었습니다.('C','.'만 입력 가능, space만큼 입력 필요)")
# 어제, 오늘 모두 사용된 주차공간을 나타내는 변수
both_occupied = 0

for i in range(space):
    if yesterday_occupied[i] == PARKED and today_occupied[i] == PARKED:
        both_occupied += 1

print(both_occupied)
