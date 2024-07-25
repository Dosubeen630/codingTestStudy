
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

isBroken = False
limit = 100000

seat = playCount = 0
while limit > 0 and not isBroken:
    limit -= 1
    coin -= 1
    playCount += 1
    if seat % 3 == 0:
        machine_state1 += 1
        if machine_state1 == PRIZE_COUNT1:
            coin += PRIZE1
            machine_state1 = 0
    elif seat % 3 == 1:
        machine_state2 += 1
        if machine_state2 == PRIZE_COUNT2:
            coin += PRIZE2
            machine_state2 = 0
    else: #seat % 3 == 2
        machine_state3 += 1
        if machine_state3 == PRIZE_COUNT3:
            coin += PRIZE3
            machine_state3 = 0
    seat += 1
    if coin == 0:
        isBroken = True

print(f"Martha plays {playCount} times before going broke.")

