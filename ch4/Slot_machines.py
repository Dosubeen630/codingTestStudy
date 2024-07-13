# https://dmoj.ca/problem/ccc00s1
# Martha takes a jar of quarters to the casino with the intention of becoming rich.
# 마사는 부자가 되겠다는 목표로 동전 한병을 카지노에 가져갑니다.
# She plays three machines in turn. Unknown to her, the machines are entirely predictable.
# 그녀는 세대의 기계를 차례로 플레이 합니다. 그녀는 모르지만 기계는 완전히 예측 가능합니다.
# Each play costs one quarter. The first machine pays 30 quarters every 35th time it is played; the second machine pays 60 quarters every
#  100th time it is played; the third pays 9 quarters every 10th time it is played.
# 각 플레이 비용은 1/4입니다. 첫번째 기계는 35번째 플레이 마다 30쿼터를 지불합니다. 두번재 기계는 매 분기마다(100회 플레이가 되면) 60쿼터를 지불합니다. 100번째 재생 세번째 기계는 10번째 플레이 마다 9쿼터를 지불합니다.
# 입력 : Your program should take as input the number of quarters in Martha's jar (there will be at least one and fewer than 1000), and the number of times each machine has been played since it last paid.
# 프로그램은 마사의 병에 담긴 쿼터수(최소 1개에서 1000개 미만)와 마지막 지불이후 각 기계가 재생된 횟수를 입력 받아야합니다.
# 출력 : Your program should output the number of times Martha plays until she goes broke.
# 프로그램은 마사가 파산 할때 까지 플레이한 횟수를 출력 해야 합니다.
# 출력 예: Martha plays (66) times before going broke.

# 도메인 분석: 마사는 카지노에 부자가 되겠다는 목표를 가지고 간 도박꾼,
# 마사는 모르지만, 카지노 기계는 예측이 가능함. 마사가 가지고 있는 동전의 수는 모름.
# 첫번째 기계의 경우, 플레이 횟수가 35번째가 되면 30쿼터를 지불함, 두번째 기계의 경우 100번 플레이가 되면 60쿼터를 지불. 세번째 기계는 10번째 플레이 마다 9 쿼터를 지불해 줌.
# 여기서 생각해 볼 것, 마사는 자신이 가진 돈(알 수없음)과 3기계 에서 플레이를 하여 일정 플레이 횟수를 채우면 기계에서 정해진 금액 만큼 받게 되어 마사가 언제 파산 할지는 알 수 없음.
# 또, 첫번째 기계 -> 두번째 기계 -> 세번째 기계 순서로 플레이를 하고 세번째 기계에서 플레이를 마치고 마사가 여전히 돈을 가지고 있다면 다시 첫번째 머신으로 가서 플레이를 해야 한다는 규칙이 존재함.
# 사용자 에게 입력 받아야 할 사항 : 마사가 가지고 있는 동전 수(quarters), 마지막 지불 이후에 세 기계가 플레이된 횟수
# 출력 되어야 할 사항: 마사가 가지고 있는 동전이 없을 때 까지 플레이 한 횟수를 Martha plays (66) times before going broke.문장에 같이 출력 해야함.

# 사용자로 부터 받은 입력 값의 유효성 검사
quarts_num = input()
if not quarts_num.isdigit(): exit(f"{quarts_num}은 숫자로 입력 해 주세요.")
quarts_num = int(quarts_num)
if not 1 <= quarts_num <= 1000: exit(f"{quarts_num}의 범위가 큽니다.")
first_machine_after_play = input()
if not first_machine_after_play.isdigit(): exit(f"{first_machine_after_play}은 숫자로 입력 해 주세요.")
first_machine_after_play = int(first_machine_after_play)
if not 0 <= first_machine_after_play <= 35: exit(f"{first_machine_after_play}의 플레이 횟수 범위를 넘었습니다.")
second_machine_after_play = input()
if not second_machine_after_play.isdigit():exit(f"{second_machine_after_play}는 숫자로 입력 해 주세요.")
second_machine_after_play = int(second_machine_after_play)
if not 0 <= second_machine_after_play <= 100: exit(f"{second_machine_after_play}의 플레이 횟수 범위를 넘었습니다.")
third_machine_after_play = input()
if not third_machine_after_play.isdigit(): exit(f"{third_machine_after_play}는 숫자로 입력 해 주세요.")
third_machine_after_play = int(third_machine_after_play)
if not 0 <= third_machine_after_play <= 10: exit(f"{third_machine_after_play}의 플레이 횟수 범위를 넘었습니다.")

# 마르타가 플레이 한 횟수 저장 변수, 마르타가 플레이를 한 기계 번호 저장 할 변수 선언, 0으로 초기화 해줌.
total_play = 0
machine = 0

# 마르타가 가진 쿼터가 0이 될때까지 반복문이 돌아가게 설정
while quarts_num >= 1:
    quarts_num -= 1

    if machine == 0:
        first_machine_after_play += 1
        if first_machine_after_play == 35:
            first_machine_after_play = 0
            quarts_num = quarts_num + 30

    elif machine == 1:
        second_machine_after_play += 1
        if second_machine_after_play == 100:
            second_machine_after_play = 0
            quarts_num = quarts_num + 60

    elif machine == 2:
        third_machine_after_play += 1
        if third_machine_after_play == 10:
            third_machine_after_play = 0
            quarts_num = quarts_num + 9

    total_play += 1 # 마르타가 플레이 한 횟수 증가
    machine += 1    # 마르타가 방금 전에 플레이 했던 기계의 번호도 증가( 다음 플레이 할 기계를 알기 위해)
    if machine == 3: # 세번째 기계에서 플레이를 마친 후에는 다음번 기계 순서가 3이 되면 다시 첫번째 머신으로 가서 플레이한다.
        machine = 0

print(f"Martha plays {total_play} times before going broke.")



