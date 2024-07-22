# https://dmoj.ca/problem/ccc15j1
# February 18 is a special date for the CCC this year.
# 2월18일 이전 이면 Before, 이후 이면 After, 2월 18일이면 Special 을 출력
# 첫번째 줄은 달, 두번재 줄은 일
# You can assume that the day of the month will be valid for the given month.
# 해당 월의 날자가 해당 달에 유효 하다고 가정 할 수 있습 니다.

month = input()
if not month.isdigit(): exit(f"{month}!= digit")
month = int(month)
if not 1 <= month <= 12: exit(f"{month}의 범위 벗어남")
day = input()
if not day.isdigit(): exit(f"{day}!= digit")
day = int(day)
if not 1 <= day <= 31: exit(f"{day}의 범위 벗어남")

if 3 <= month <= 12 and 1 <= day <= 31:
    print("After")
elif 2 < month or day <= 31:
    print("Before")
elif month == 2 and day < 17:
    print("Before")
else: # month == 2 and day == 18
    print("Special")
