# https://dmoj.ca/problem/ccc11s2
# Your teacher likes to give multiple choice tests.
# 당신의 선생님은 다양한 선택지가 있는 시험을 좋아한다.
# One benefit of giving these tests is that they are easy to mark, given an answer key.
# 이런 시험들이 주는 한 가지 이점이 있다면, 그것들은 표시 하기 쉬우며, 답을 준다.
# The other benefit is that students believe they have a one-in-five chance of getting the correct answer, assuming the multiple choice possibilities are A, B, C, D or E.
# 또 다른 이점은 학생들이 바른 정답으로 가기 위한 한번에서 다섯번의 기회가 주어진다. A,B,C,D,E 라는 다양한 선택지가 추정을 가능하게 한다.
# Write a program that your teacher can use to grade one multiple choice test.
# 당신의 선생님이 점수를 주기 위한 한가지의 다양한 선택지가 있는 시험을 만드는 프로그램을 적어보아라.
# The input will contain the number N(0<N<10000) followed by 2N lines.
# 입력란에는 N이라는 숫자가 포함되어 있고, 뒤이어 2N의 라인이 주어진다.
# The 2N lines are composed of N lines of student responses (with one of A, B, C, D or E on each line), followed by N lines of correct answers_key (with one of A, B, C, D or E on each line), in the same order as the student answered the questions (that is, if line
# i is the student response, then line N+i will contain the correct answer to that question).
# 2N 라인은 N 라인의 문제의 개수, 두번째 줄에는 N개의 정답, 세번째 줄에는 학생의 답안이 주어진다.
# Output the integer C(0<=C<=N) which corresponds to the number of questions the student answered correctly.
# 출력란에는 정수 C, 학생이 올바르게 답한 질문 수에 해당합니다.

# 문제수 입력 받음.
problem_num = input()
if not problem_num.isdigit():
    exit(f"{problem_num}이 숫자가 아닙니다.")
problem_num = int(problem_num)
if not 0 < problem_num < 10000:
    exit(f"{problem_num}의 범위가 벗어납니다.")

student = ""
#student 가 입력한 답 입력 받음.
for i in range(problem_num):
    student = student + input()
    #print(student)
    #if not student.isalpha():
      # exit(f"{student}가 문자가 아닙니다.")
    if not student.isupper():
        exit(f"{student}가 대문자가 아닙니다.")
   # if student[i] in 'ABCDE':
       # exit(f"{student}의 입력이 잘못 되었습니다.")

answer_key = ""
# 정답 입력 받음.
for i in range(problem_num):
    answer_key = answer_key + input()
    #print(answer_key)
    #if not answer_key.isalpha():
     #   exit(f"{answer_key}가 문자가 아닙니다.")
    if not answer_key.isupper():
       exit(f"{answer_key}가 대문자가 아닙니다.")
    #if answer_key[i] in 'ABCDE':
        #exit(f"{answer_key}의 입력이 잘못 되었습니다.")

correct_num = 0
for i in range(problem_num):
    if student[i] == answer_key[i]: # 학생이 입력한 답과 정답이 일치할 경우 정답 개수를 1씩 증가 시켜준다.
        correct_num += 1
    else:
        pass

print(correct_num)






