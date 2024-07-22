# https://dmoj.ca/problem/ccc06j1
# 입력란 첫번째 줄은 햄버거 선택, 둘째 줄은 사이드, 셋째 줄은 음료, 넷째 줄은 디저트
# 숫자 입력 1~4 가능 각 메뉴 에서 칼로리 계산 하여 총 칼로리 출력 해서 보여 주는 프로 그램

burger = input()
if not burger.isdigit(): exit(f"{burger} != digit")
burger = int(burger)
if not 1 <= burger <= 4: exit(f"{burger}의 범위 벗어남")
side = input()
if not side.isdigit(): exit(f"{side} != digit")
side = int(side)
if not 1 <= side <= 4: exit(f"{side}의 범위 벗어남")
drink = input()
if not drink.isdigit(): exit(f"{drink}!= digit")
drink = int(drink)
if not 1 <= drink <=4 : exit(f"{drink}의 범위 벗어남")
dessert = input()
if not dessert.isdigit(): exit(f"{dessert} != digit")
dessert = int(dessert)
if not 1 <= dessert <= 4: exit(f"{dessert}의 범위에 벗어남")

total_colorie = 0
if burger == 1:
    burger = 461
elif burger == 2:
    burger = 431
elif burger == 3:
    burger = 420
else:
    burger = 0

if side == 1:
    side = 100
elif side == 2:
    side = 57
elif side == 3:
    side = 70
else:
    side = 0

if drink == 1:
    drink = 130
elif drink == 2:
    drink = 160
elif drink == 3:
    drink = 118
else:
    drink = 0

if dessert == 1:
    dessert = 167
elif dessert == 2:
    dessert = 266
elif dessert == 3:
    dessert = 75
else:
    dessert = 0

total_colorie = burger + side + drink + dessert

print("Your total Calorie count is " + f"{total_colorie}.")


