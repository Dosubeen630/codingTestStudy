# https://dmoj.ca/problem/ccc11s2
# 입력 으로 우선 답의 개수 주어짐, 그 이후 답의 개수 만큼 나오는 것 정답, 그 이후 답의 개수 만큼 나온것은 학생 답
# 정답과 학생 답 비교 하여 맞춘 개수 출력 하는 프로 그램 만들기
# 생각 해볼 것! 우선 정답과 학생 의 답 비교 일치 하는 것 카운팅
# 변수명 지정 하기 어려움. 또 변수를 몆개 지정 해야 하는지 정하기 어려움.

MULTIPLE_CHOICE = "ABCDE"
answer_num = input()
if not answer_num.isdigit():exit(f"{answer_num} != digit")
answer_num = int(answer_num)
if not 0 < answer_num < 10000: exit(f"범위 벗어남(0 < {answer_num} < 10000)")

correct_answer = 0

answers_key = ""
for i in range(answer_num):
    answers_key = answers_key + input()
    if answers_key not in MULTIPLE_CHOICE:
        exit("잘못된 입력값(A,B,C,D,E)만 가능 합니다.")

student_answer = ""
for i in range(answer_num):
    student_answer = student_answer + input()
    if student_answer not in MULTIPLE_CHOICE:
        exit("잘못된 입력값(A,B,C,D,E)만 가능 합니다.")

for i in range(answer_num):
    if answers_key[i] == student_answer[i]:
        correct_answer += 1

print(correct_answer)

