# https://dmoj.ca/problem/coci08c1p2
# 아드리안, 브루노, 고란 3명의 학생 답안 패턴을 만들어 정답과 비교
# 맞은 갯수를 세고, 가장 많이 맞춘 학생 이름과 갯수 출력. 맞춘 개수가 같다면 이름은 순서대로 출력

Adrian = "ABC"
Bruno = "BABC"
Goran = "CCAABB"

answer_num = input()
if not answer_num.isdigit(): exit(f"{answer_num} != digit")
answer_num = int(answer_num)
if not 1 <= answer_num <= 100: exit(f"( 1 <= {answer_num} <= 100")
answer = input()
#if not answer in "ABC": exit(f" {answer} != ABC")
i = 0
Adrian_count = 0
Bruno_count = 0
Goran_count = 0

while i < len(answer):
    Adrian_answer = Adrian [i % len(Adrian)]
    Bruno_answer = Bruno [i % len(Bruno)]
    Goran_answer = Goran [i % len(Goran)]

    i += 1

    if answer[i] == Adrian_answer:
        Adrian_count += 1
    elif answer[i] == Bruno_answer:
        Bruno_count += 1
    else: # answer[i} == Goran_answer
        Goran_count += 1

    max_answer = Adrian_count# 정답을 많이 맞춘 사람 갯수를 아드리안 이라고 정하고
    max_name = None
    if max_answer < Bruno_count :
        max_answer = Bruno_count
        max_name = Bruno
    elif max_answer < Goran_count:
        max_answer = Goran_count
        max_name = Goran
    else:
        max_answer = Adrian_count
        max_name = Adrian


    print(max_answer)
   # print(max_name)

