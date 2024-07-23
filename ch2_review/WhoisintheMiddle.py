# https://dmoj.ca/problem/ccc07j1
# 3명의 곰 가족의 밥그릇, 가장 무거운 밥그릇이 아빠 곰 것, 중간 밥그릇이 엄마 곰그릇, 가장 가벼운 그릇이 아기곰 그릇으로 무게로 정렬
# 3가지 무게를 읽고 엄마 곰 그릇의 무게를 출력하는 프로그램 작성. 모든 가중치가 100보다 작은 양의 정수라고 가정 할 수 있다.
# 3 값 중  크기 비교 , 중간값 찾기

first_bowl = input()
if not first_bowl.isdigit():exit(f"{first_bowl} != digit")
first_bowl = int(first_bowl)
second_bowl = input()
if not second_bowl.isdigit():exit(f"{second_bowl} != digit")
second_bowl = int(second_bowl)
third_bowl = input()
if not third_bowl.isdigit():exit(f"{third_bowl} != digit")
third_bowl = int(third_bowl)

medium = None
# 두번째 그릇이 중간 이라는 가정
if (first_bowl >= second_bowl and second_bowl >= third_bowl) or (first_bowl <= second_bowl and second_bowl <= third_bowl):

     medium = second_bowl

# 첫번째 그릇이 중간 이라는 가정
elif (second_bowl >= first_bowl and first_bowl >= third_bowl) or (second_bowl <= first_bowl and first_bowl <= third_bowl):

    medium = first_bowl

else:
    medium = third_bowl

print(medium)