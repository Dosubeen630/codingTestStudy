# https://dmoj.ca/problem/dmopc14c5p1
# 시몬이 가진 드릴의 지름r 과 높이 h를 알고 있다. 그 드릴의 부피를 구하는 프로그램 작성
# 입력 첫 줄에는 정수r (1<=r<=100), 두번째 줄에는 정수 h(1<=ㅗ<=100)
# 출력은 시몬의 드릴의 부피( 절대 또는 상대 오류 내에 있는 경우 출력이 허용 됨)

radius = input()
if not radius.isdigit(): exit(f"{radius} != digit")
radius = int(radius)
if not 1 <= radius <= 100: exit(f"{radius} 범위에 벗어남.")
height = input()
if not height.isdigit() : exit(f"{height} != digit")
height = int(height)
if not 1 <= height <= 100: exit(f"{height} 범위에 벗어남")

PI = 3.14159
volume = (PI* radius**2 * height) / 3
formatted_volume = f"{volume:.2f}" # f-string 으로 소수 둘째 짜리 까지 출력 가능
rounded_volume = round(volume, 2) # round는 소수점 n 자리에서 반올림 합니다.

print(volume)
print(formatted_volume)
print(rounded_volume)
# 출력이 47.123850000000004 가 됨. 소수점 둘째 까지만 출력 하는 방법은?
