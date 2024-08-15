# 카드 종류는 하이 카드와 그외. 각 하이 카드는 획득 점수 만큼 하이 카드가 안 나와야 함.
# 숨겨진 논리 분석 으로 알아 내기: 사실 상 남은 카드 제약은 없어도 무방.
# 턴은 몇 번째 카드를 뽑았나 로 알 수 있음. 실제 유지 될 상태: 몇번째 턴, a,b 포인트 합계, 카운팅 중인 하이 카드, 몇장 째 카운팅
# 함수만 사용 하면서 순수 함수로 구성!
def setStack(state, index, stack, turn, a, b):
    """
    :param state: 하이 카드를 뽑았을 때, 0이 아님. 아니면 상태는 0
    :param index: 이번 턴에 뽑은 카드
    :param stack: 하이 카드가 아닌 것을 몇 장째 뽑고 있냐?
    :param turn: 누구 차례?
    :param a: 플레 이어 a의 포인트 합산
    :param b: 플레 이어 b의 포인트 합산
    :return:
    """
    # 카드를 뽑아서 나온 카드가 하이 카드 일때,
    if state != 0:
        # 얻어야 할 포인트 (리스트를 인덱스로 쓰기, 리니어 하게, 순차 정렬 가능)
        fullfill = state - 8
        # 하이 카드를 뽑은 이후에 나온 하이 카드가 아닌 카드 갯수 stack에 업데이트
        if index < 9:
            if stack + 1 == fullfill:
                # 누구 순서 였는지 확인 해주는 연산
                if (turn - fullfill) % 2 == 0:
                    player = "A"
                    a = a + fullfill
                else:
                    player = "B"
                    b = b + fullfill
                # side effect 따로 코드를 짜 줄수 있지만 번거로워 지고 코드가 길어짐.
                print(f"Player {player} scores {fullfill} point(s).")
                return 0, 0, a, b
            else:
                return state, stack + 1, a, b
        # 하이 카드를 뽑은 이후에 나온 카드의 인덱스가 하이 카드가 아닌 경우
        else:
            return index, 0, a, b
    else:
        # 뽑은 카드가 하이 카드 이고 다음 카드의 인덱스 가 하이 카드 일 경우
        if index > 8:
            return index, 0, a, b
        else: # 카드 인덱스 가 하이 카드가 아닐 경우
            return 0, 0, a, b

cards = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
         "jack", "queen", "king", "ace"]
drews = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
state = 0
stack = 0
turn = -1
a = 0
b = 0
for i in range(52):
    drew = input()
    index = cards.index(drew)
    if index == -1: exit(f"{drew} is not in cards")
    if drews[index] == 0: exit(f"{drew} drews 4")
    drews[index] -= 1
    remain = 52 - i - 1
    turn = turn + 1
    # 복잡한 녀석 들은 우선 함수로 모두 보내 해결.
    state, stack, a, b = setStack(state, index, stack, turn, a, b)

print(f"Player A: {a} point(s).")
print(f"Player B: {b} point(s).")

# 각 카드에 인덱스 값 부여
# cards = [0 = "two", 1 ="three", 2="four", 3="five", 4="six", 5="seven", 6="eight", 7="nine", 8="ten",
#         9 = "jack", 10 ="queen", 11 ="king", 12 ="ace"]


