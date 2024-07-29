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
    if answer[i] == Adrian [i % len(Adrian)]:
        Adrian_count += 1
    if answer[i] == Bruno [i % len(Bruno)]:
        Bruno_count += 1
    if answer[i] == Goran [i % len(Goran)]:
        Goran_count += 1

    i += 1

max_count = max(Adrian_count, Bruno_count, Goran_count)
winners = []
if Adrian_count == max_count:
    winners.append("Adrian")
if Bruno_count == max_count:
    winners.append("Bruno")
if Goran_count == max_count:
    winners.append("Goran")


print(max_count)
for winner in sorted(winners):
    print(winner)

