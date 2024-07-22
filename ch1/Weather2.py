# https://dmoj.ca/problem/wc17c1j2
# 도씨가 주어 지면 화씨로 계산 되어 출력 되는 프로 그램 만들기
# convert temperatures measured in degrees Celsius to Fahrenheit instead.
# It's guaranteed that C will be chosen such that F will come out to exactly an integer, but you may output it with  0 or more digits after the decimal point.
# F가 정확히 정수로 나오 도록 C를 선택 하는 것은 보장 되지만, 소수점 이하 0자리 이상 으로 출력 해도 된다.


celsius = input()
if not celsius.isdigit(): exit(f"{celsius}!= digit")
celsius = int(celsius)
if not -40 <= celsius <= 40: exit(f"{celsius}의 범위에 벗어남")


fahrenheit = int(((9* celsius) + 160) / 5)

print(fahrenheit)

