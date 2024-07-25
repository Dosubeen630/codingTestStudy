# https://dmoj.ca/problem/ccc00s1
# 가진 돈을 모두 써야 플레이가 끝! 머신은 3대 순서대로 플레이
# 코인 1개를 사용하면서 플레이 횟수 추가. 머신 마다 정해진 플레이 횟수를 채우면 상금이 주어짐.

PRIZE1 = 30
PRIZE_COUNT1 = 35
PRIZE2 = 60
PRIZE_COUNT2 = 100
PRIZE3 = 9
PRIZE_COUNT3 = 10

coin = input()
if not coin.isdigit(): exit(f"{coin} != digit")
coin = int(coin)
if not 1 <= coin <= 1000 : exit(f" 범위 벗어남 ( 1 <= {coin} <= 1000)")

machine_state1 = input()
if not machine_state1.isdigit() : exit(f"{machine_state1} != digit")
machine_state1 = int(machine_state1)
if not 0 <= machine_state1 <= PRIZE_COUNT1:
    exit(f"machine_state1 범위 벗어남 ( 0 <= {machine_state1} <= {PRIZE_COUNT1})")

machine_state2 = input()
if not machine_state2.isdigit(): exit(f"{machine_state2} != digit")
machine_state2 = int(machine_state2)
if not 0 <= machine_state2 <= PRIZE_COUNT2:
    exit(f"machine_state2 범위 벗어남 ( 0 <= {machine_state2} <= {PRIZE_COUNT2})")

machine_state3 = input()
if not machine_state3.isdigit() : exit(f"{machine_state3} != digit")
machine_state3 = int(machine_state3)
if not 0 <= machine_state3 <= PRIZE_COUNT3:
    exit(f"machine_state3 범위 벗어남 ( 0 <= {machine_state3} <= {PRIZE_COUNT3})")
# 걀정론에 의한 불변식
isBroken = False
limit = 10000
seat = playCount = 0
while limit > 0 and not isBroken:
    limit -= 1
    base = coin + seat # (new one) maybe 기계가 상금에 주는 플레이 횟수에 다다르면 이미 가지고 있는 코인에 상금 코인을 추가 해주기 때문에 새로 만든 변수
    a = int(base / 3) # 코딩 할때는 실무 에서는 약간 간단히 코딩 하기 편하게 간단한 변수로 선언해 주는 듯
    b = base % 3 # 몫 연산자와 나머지 연산자를 왜 둘 다 사용 하는지 조금 궁금??
    machine_state1 += a
    machine_state2 += a
    machine_state3 += a
    if b == 1:
        if seat == 0: machine_state1 += 1
        elif seat == 1: machine_state2 += 1
        else: machine_state3 += 1
    elif b == 2:
        if seat == 0:
            machine_state1 += 1
            machine_state2 += 1
        elif seat == 1:
            machine_state2 += 1
            machine_state3 += 1
        else:
            machine_state3 += 1
            machine_state1 += 1
playCount += coin
seat = (seat + coin) % 3
coin = 0

if machine_state1 >= PRIZE_COUNT1:
    coin += int(machine_state1 / PRIZE_COUNT1) * PRIZE1
    machine_state1 = machine_state1 % PRIZE_COUNT1
if machine_state2 >= PRIZE_COUNT2:
    coin += int(machine_state2 / PRIZE_COUNT2) * PRIZE2
    machine_state2 = machine_state2 % PRIZE_COUNT2
if machine_state3 >= PRIZE_COUNT3:
    coin += int(machine_state3 / PRIZE_COUNT3) * PRIZE3
    machine_state3 = machine_state3 % PRIZE_COUNT3

if coin == 0: isBroken = True
print(f"Martha plays {playCount} times before going broke.")

#play = seat = 0

#while coin >= 1:
    #coin -= 1
   # play += 1
   # if seat % 3 == 0:
        #machine_state1 += 1
        #if machine_state1 == PRIZE_COUNT1:
        #    coin += PRIZE1
       #     machine_state1 = 0
    #elif seat % 3 == 1:
     #   machine_state2 += 1
      #  if machine_state2 == PRIZE_COUNT2:
       #     coin += PRIZE2
        #    machine_state2 = 0
   # elif seat % 3 == 2:
     #   machine_state3 += 1
      #  if machine_state3 == PRIZE_COUNT3:
      #      coin += PRIZE3
       #     machine_state3 = 0

   # seat += 1

