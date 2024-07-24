# https://dmoj.ca/problem/coci13c3p1
# 큰 화면과 한 개의 버튼이 있는 재미있는 기계가 있음. 버튼을 누르면  A -> B, B->BA 규칙 발견
# 입력에는 버튼을 누른 횟수 출력에는 두개의 공백을 사이에 두고 A and B의 글자 수
# 중요한 사항은 A,B의 개수만 필요. 이전 A는 B로 바뀌고, B는 BA로 바뀌는 것을 갯수로 치환
# 이번 A는 이전의 B의 개수, 이번 B는 이전 A와 B의 합

press_button = input()
if not press_button.isdigit() :exit(f"{press_button} != digit")
press_button = int(press_button)
if not 1 <= press_button <= 45 : exit(f"범위에 벗어남.(1 <= {press_button} <= 45)")

now_a = 1  # 처음 화면에 A가 나와 있었 으니, 1로 시작
now_b = 0
for i in range(press_button):
    prev_a = now_a
    prev_b = now_b
    now_a = prev_b
    now_b = prev_a + prev_b

print(str(now_a) + "  " + str(now_b)) # 두 칸의 공백을 두고 A,B 값이 출력 되게!


