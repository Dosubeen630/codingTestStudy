# Trik
moves = input()

if moves.count('A') + moves.count('B') + moves.count('C') != len(moves):
    exit("입력한 값이 'A','B','C' 가 아닙니다.")

cups = '1,2,3'

for move in moves:
    if move == 'A': # 123 -> 213
        cups = cups[1] + cups[0] + cups[2]
    elif move == 'B': # 123 -> 132
        cups = cups[0] + cups[2] + cups[1]
    else: # 'C ' 123-> 321
        cups = cups[2] + cups[1] + cups[0]

print(cups.find('1') + 1)

# Magnus

words = input()
if not words.isalpha():
    exit(f"{words}의 형식이 잘못 되었습니다. 문자로 입력 해주세요.")
if not words.isupper():
    exit(f"{words}가 잘못 되었습니다. 대문자로 입력 해주세요.")
if not 1 <= len(words) <= 100000:
    exit(f"{words}의 범위에 벗어 났습니다.")

count = 0
prev = None
for char in words:
    if char == 'H' and (prev == 'I' or prev is None):
        prev = 'H'
    elif char == 'O' and prev == 'H':
        prev = 'O'
    elif char == 'N' and prev == 'O':
        prev = 'N'
    elif char == 'I' and prev == 'N':
        prev = 'I'
        count += 1
    else:
        pass

print(count)

# Occupy parking
PARKED = 'C'
EMPTY = '.'

space = input()
if not space.isdigit():
    exit(f"{space}는 숫자로 입력 부탁.")
space = int(space)
if not 1 <= space <= 100:
    exit(f"{space}의 범위를 벗어남.")
yesterday = input()
if yesterday.count(PARKED) + yesterday.count(EMPTY) != space:
    exit(f"{yesterday}에는 PARKED,EMPTY 형식만 입력 가능, space 범위를 벗어남.")
today = input()
if today.count(PARKED) + today.count(EMPTY) != space:
    exit(f"{today}에는 PARKED,EMPTY 형식만 입력 가능, space 범위를 벗어남.")

countinus_day = 0

for i in range(space):
    if yesterday[i] == PARKED and today[i] == PARKED:
        countinus_day += 1
    else:
        pass

print(countinus_day)





