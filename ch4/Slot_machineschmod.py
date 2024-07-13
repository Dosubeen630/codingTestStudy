
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

# 같은 코드를 가지고 mod 연산자를 사용하여 더 간단화 시켜봄.
# 마르타가 플레이 한 횟수 저장 변수, 마르타가 플레이를 한 기계 번호 저장 할 변수 선언, 0으로 초기화 해줌.
total_play = 0
# machine = 0

# 마르타가 가진 쿼터가 0이 될때까지 반복문이 돌아가게 설정
while quarts_num >= 1:

    machine = total_play % 3 # mod연산자 사용하여 기계 순서를 순서대로 바꾸어줌.
    quarts_num -= 1 # 플레이 할때마다 마르타가 가진 쿼터수를 하나씩 감소 시켜줘야 함.

    if machine == 0:
        first_machine_after_play += 1
       # if first_machine_after_play == 35:
        if first_machine_after_play % 35 == 0:
           # first_machine_after_play = 0
            quarts_num = quarts_num + 30

    elif machine == 1:
        second_machine_after_play += 1
      #  if second_machine_after_play == 100:
        if second_machine_after_play % 100 == 0 :
           # second_machine_after_play = 0
            quarts_num = quarts_num + 60

    elif machine == 2:
        third_machine_after_play += 1
        #if third_machine_after_play == 10:
        if third_machine_after_play % 10 == 0:
            #third_machine_after_play = 0
            quarts_num = quarts_num + 9
# 모드 연산자를 사용하여 플레이 할 기계 순서를 차례대로 정해주고, 각 머신마다 상금을 지불해야할 순서가 되면 상금을 지불하고 일일이 플레이 횟수를 초기화 시키던 것을 생략 가능.
    total_play += 1 # 마르타가 플레이 한 횟수 증가
   # machine += 1    # 마르타가 방금 전에 플레이 했던 기계의 번호도 증가( 다음 플레이 할 기계를 알기 위해)
   # if machine == 3: # 세번째 기계에서 플레이를 마친 후에는 다음번 기계 순서가 3이 되면 다시 첫번째 머신으로 가서 플레이한다.
    #    machine = 0

print(f"Martha plays {total_play} times before going broke.")



