# 두 수를 입력 받음. 첫 번째 입력 받은 수는 정수로 (1<W<3) 피자 의 넓이
# 나머지 다른 수는 (0<= C <= 100)으로 정수, 피자를 둘러싸고 있는 치즈의 양
# 입력 받은 수에 따라 C.C. is "M" satisfied with her pizza. M에 알맞은 글자를 넣어 출력한다.
# 피자의 너비가 3조각 이고 치즈의 양이 적어도 95퍼센트 이상이면 "M"에 absolutely를 출력
# 피자의 너비가 1조각 이고 치즈의 양이 50퍼센트 이상이면 "M"에 fairly를 출력
# 그 외에 나머지 조건의 피자는 "M"에 very 를 출력한다.

w = int(input())
c = int(input())

# 피자 너비가 3이고 피자 치즈의 양이 95% 이상 일때,
if w == 3 and ((c > 95) or (c == 95)):
    print("C.C. is absolutely satisfied with her pizza.")
# 피자 너비가 1이고 피자 치즈의 양이 50% 이상 일때,
elif w == 1 and ((c < 50) or (c == 50)):
    print("C.C. is fairly satisfied with her pizza.")
# 그 이외의 경우에
else:
    print("C.C. is very satisfied with her pizza.")




