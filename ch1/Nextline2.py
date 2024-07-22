# https://dmoj.ca/problem/ccc13j1
# 3명의 자식이 있음. 제일 어린아이 나이와 중간아이의 나이를 보고 제일 나이 많은 아이 나이 출력하기
#  youngest child (0<=Y<=50) ,  middle child (Y<=M<=50)

youngest_age = input()
if not youngest_age.isdigit(): exit(f"{youngest_age} != digit")
youngest_age = int(youngest_age)
if not 0<= youngest_age <= 50: exit(f"{youngest_age}의 범위 벗어남")
middle_age = input()
if not middle_age.isdigit(): exit(f"{middle_age}!= digit")
middle_age = int(middle_age)
if not youngest_age <= middle_age <= 50: exit(f"{middle_age}의 범위 벗어남")

gap = middle_age - youngest_age
oldest_age = middle_age + gap
print(oldest_age)