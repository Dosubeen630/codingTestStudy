# 두 수를 입력 받는다. 첫번째 입력은 달이고 두번째 입력은 날짜를 의미한다.
# 2월 18일은 특별한 날이다.
# 만약 2월18일 보다 전이면 'Before'를 출력하고, 2월18일 이후이면 'After'를 출력한다.
# 만약 입력 받은 수가 2월18일을 의미하면 'Special'을 출력하게 만든다.

# 월를 입력 받음
month = int(input())
# 날짜를 입력 받음
day = int(input())

# 만약 달이 2월 이거나 날짜가 18일이면
if month == 2 and day == 18:
    print("Special")
# 달이 2월보다 작거나 같고, 날짜가 18일 보다 적으면,
elif ((month < 2) or (month == 2) and (day < 18)):
    print("Before")
# 그 외의 경우에
else:
    print("After")