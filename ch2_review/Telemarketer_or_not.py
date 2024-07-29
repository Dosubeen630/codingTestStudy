# https://dmoj.ca/problem/ccc18j1
# Concerned Citizens of Commerce (CCC)
# we have noted that telemarketers like to use seven-digit phone numbers where the last four digits have three properties.
# 우리는 텔레 마케터 들이 마지막 4자리에 3가지 속성이 있는 7자리 전화 번호를 사용 하는 것을 좋아한 다는 것을 알고 있습 니다.
# 마지막 4자리 에서 이런 속성을 가지고 있음. 첫번째 자리는 8 이나 9, 마지막 번호도 8 이나 9,  두번 째나 세번째 수는 동일
# 4가지 입력 받음 순서 대로 마지막 네자리 번호 임. 텔레 마케터 번호 이면  ignore, 아니면 answer_num 출력

PNumLastFirst = input()
if len(PNumLastFirst) != 1: exit(f"{PNumLastFirst} == 1")
if not PNumLastFirst.isdigit(): exit(f"{PNumLastFirst} != digit")

PNumLastSecond = input()
if len(PNumLastSecond) != 1: exit(f"{PNumLastSecond} ==1")
if not PNumLastSecond.isdigit(): exit(f"{PNumLastSecond} != digit")

PNumLastThird = input()
if len(PNumLastThird) != 1: exit(f"{PNumLastThird} == 1")
if not PNumLastThird.isdigit() : exit(f"{PNumLastThird} != digit")

PNumLastFourth = input()
if len(PNumLastFourth) != 1: exit(f"{PNumLastFourth} == 1")
if not PNumLastFourth.isdigit() : exit(f"{PNumLastFourth} != digit")

if not PNumLastFourth in "89":
    exit("answer_num")
if not PNumLastSecond == PNumLastThird:
    exit("answer_num")
if not PNumLastFirst in "89":
    exit("answer_num")

else:
    print("ignore")