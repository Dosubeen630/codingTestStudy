# 4개의 수를 입력 받음. 첫번째 입력 받은 수는 햄버거의 종류, 두번째 입력 받은 수는 사이드 메뉴의 종류
# 세번째 입력받은 수는 음료수의 종류 , 네번째 입력 받은 수는 디저트의 종류를 의미한다.
# 각 입력 받은 수의 메뉴에 나온 칼로리를 모두 더하여 마지막에 총 칼로리를 보여주는 프로그램이다.


# 버거, 사이드 , 음료수, 디저트의 종류를 입력받는다.
burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

#버거의 종류가 1 이면,
if burger == 1:
    burger = 461
#버거의 종류가 2 이면,
elif burger == 2:
    burger = 431
#버거의 종류가 3 이면,
elif burger == 3:
    burger = 420
# 그 이외의 경우 이면,
else:
    burger = 0
# 사이드의 종류가 1이면,
if side == 1:
    side = 100
# 사이드의 종류가 2이면,
elif side == 2:
    side = 57
# 사이드의 종류가 3이면,
elif side == 3:
    side = 70
# 그 이외의 경우 이면,
else:
    side = 0
# 음료수의 종류가 1 이면,
if drink == 1:
    drink = 130
# 음료수의 종류가 2 이면,
elif drink == 2:
    drink = 160
# 음료수의 종류가 3 이면,
elif drink == 3:
    drink = 118
# 그 이외의 경우 이면,
else:
    drink = 0
# 디저트의 종류가 1 이면,
if dessert == 1:
    dessert = 167
# 디저트의 종류가 2 이면,
elif dessert == 2:
    dessert = 266
# 디저트의 종류가 3 이면,
elif dessert == 3:
    dessert = 75
# 그 이외의 경우 이면,
else:
    dessert = 0
# 총 칼로리는 버거와 사이드, 음료수, 디저트의 총 칼로리를 더해준다.
total_calorie = burger + drink + side + dessert
# 출력은 Your total Calorie count is "total_calorie".를 출력해준다.
print('Your total Calorie count is' + " " + str(total_calorie)+".")