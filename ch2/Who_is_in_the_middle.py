# 세 가지 수를 입력 받아서 (그 수의 범위는 1에서 100까지수, 양의 숫자 범위)
# 가장 가벼운 무게 밥그릇은 아기곰, 중간 무게 밥그릇은 엄마 곰, 가장 무거운 밥그릇은 아빠 곰 밥그릇
# 입력 받은 수 중에서 중간의 숫자를 출력하는 문제

Bowl_one = int(input())
Bowl_two = int(input())
Bowl_three = int(input())

# 첫 번째는  one 이 middle 인지 찾는 것
if (Bowl_one > Bowl_two and Bowl_one < Bowl_three) or (Bowl_one < Bowl_two and Bowl_one > Bowl_three) :
    middle_number = Bowl_one
# 두 번째는 two 가 middle 인지 찾는 것
elif (Bowl_two > Bowl_one and Bowl_two < Bowl_three) or (Bowl_two < Bowl_one and Bowl_two > Bowl_three):
    middle_number = Bowl_two
# 세 번째는 three 가 middle 인지 찾는 것
else:
    middle_number = Bowl_three

print(middle_number)

# print(Bowl_one, Bowl_two, Bowl_three)