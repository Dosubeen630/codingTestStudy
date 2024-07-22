# https://dmoj.ca/problem/dmopc16c1p0
# One summer evening, while curled up with her beloved Cheese-kun plushie, C.C. begins craving pizza.
# 어느 여름날 저녁, 사랑하는 치즈군 봉제인형 C.C. 와 함께 웅크리고 있던 중 피자를 갈망하기 시작합니다.
# Although she would really like a large, extra-cheesy pizza, her stomach is willing to settle for anything.
# 그녀는 크고 치즈가 듬뿍 들어간 피자를 정말 좋아하지만, 그녀의 배는 무엇이든 기꺼이 만족합니다.
# absolutely는 3 조각의 너비와 추가 치즈가 최소한 95% 이상
# fairly는 1 조각의 너비 와 추가 치즈가 최대 50%
# very는 그녀가 받는 다른 피자에 만족할때 사용
# W는 정수로 (1<=W<=3) 너비, C도 정수로 (0<=C<=100) 추가 치즈의 양
# C.C. is M satisfied with her pizza. M에 absolutely, fairly or very 에 넣어준다.

width = input()
if not width.isdigit():exit(f"{width}!= digit")
width = int(width)
if not 1 <= width <= 3: exit(f"{width}의 범위에 벗어남")
extra_cheese = input()
if not extra_cheese.isdigit(): exit(f"{extra_cheese} != digit")
extra_cheese = int(extra_cheese)
if not 0 <= extra_cheese <= 100: exit(f"{extra_cheese}의 범위 벗어남")

status = None
if width == 3 and 95 <= extra_cheese :
    status = "absolutely"
elif width == 1 and extra_cheese <= 50:
    status = "fairly"
else:
    status = "very"

print("C.C. is" + " " + status + " " + "satisfied with her pizza.")
