# https://dmoj.ca/problem/ccc19j1
# Points are scored by a 3-point shot, a 2-point field goal, or a 1-point free throw.
# You know the number of each of these types of scoring for the two teams: the Apples and the Bananas. Your job is to determine which team won, or if the game ended in a tie.
# 1-3번재 줄은 애풀 팀의 3,2,1점 슛 기록, 4-6번째 줄은 3,2,1 점 슛 기록
# If the Apples scored more points than the Bananas, output A. If the Bananas scored more points than the Apples, output B. Otherwise, output T, to indicate a tie.

apple_shot = input()
if not apple_shot.isdigit():exit(f"{apple_shot} != digit")
apple_shot = int(apple_shot)
if not 0 <= apple_shot <= 100: exit(f"{apple_shot}의 범위 벗어남")
apple_field_goal = input()
if not apple_field_goal.isdigit(): exit(f"{apple_field_goal} != digit")
apple_field_goal = int(apple_field_goal)
if not 0 <= apple_field_goal <= 100: exit(f"{apple_field_goal}의 범위 벗어남")
apple_free_throw = input()
if not apple_free_throw.isdigit(): exit(f"{apple_free_throw} != digit")
apple_free_throw = int(apple_free_throw)
if not 0 <= apple_free_throw <= 100 : exit(f"{apple_free_throw}의 범위 벗어남")

banana_shot = input()
if not banana_shot.isdigit(): exit(f"{banana_shot} != digit")
banana_shot = int(banana_shot)
if not 0 <= banana_shot <= 100: exit(f"{banana_shot}의 범위 벗어남")
banana_field_goal = input()
if not banana_field_goal.isdigit(): exit(f"{banana_field_goal} != digit")
banana_field_goal = int(banana_field_goal)
if not 0 <= banana_field_goal <= 100: exit(f"{banana_field_goal}의 범위 벗어남")
banana_free_throw = input()
if not banana_free_throw.isdigit(): exit(f"{banana_free_throw} != digit")
banana_free_throw = int(banana_free_throw)
if not 0 <= banana_free_throw <= 100: exit(f"{banana_free_throw}의 범위 벗어남")

AshotPoint = apple_shot * 3
AfieldGoalPoint = apple_field_goal * 2
AFreeThrowPoint = apple_free_throw

BshotPoint = banana_shot * 3
BfieldGoalPoint = banana_field_goal * 2
BFreeThrowPoint = banana_free_throw

a_total_point = AshotPoint + AfieldGoalPoint + AFreeThrowPoint
b_total_point = BshotPoint + BfieldGoalPoint + BFreeThrowPoint

if a_total_point > b_total_point:
    print("A")
elif a_total_point < b_total_point:
    print("B")
else: # 동점
    print("T")

