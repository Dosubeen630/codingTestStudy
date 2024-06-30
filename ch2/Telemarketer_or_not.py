# 네가지 수를 입력 받는다.
# 첫번째 수는 8 또는 9이다. 두번째와 세번째 수는 동일하다.
# 네번째 수는 8 또는 9이다. 전화번호가 텔레마케터의 번호이면 ignore가 출력,
# 그렇지 않으면 answer가 출력된다.

# 한 줄 마다 숫자를 입력 받는다. 총 네개의 수를 입력받음.
first_number = int(input())
second_number = int(input())
third_number = int(input())
four_number = int(input())

# 만약 첫번째 수가 8 이나 9이고, 두번째 수는 세번째 수와 동일하며, 네번째 수가 8 또는 9 일때,
if ((first_number == 8 or first_number == 9) and
    (second_number == third_number) and
    (four_number == 8 or four_number == 9)):
    print("ignore")
# 그 이외의 경우일때,
else:
    print("answer")





