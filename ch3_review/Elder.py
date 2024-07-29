# https://dmoj.ca/problem/coci18c4p1
# 지팡이가 대결을 통해 이기면 주인이 바뀜. 지팡이는 결국 어느 마법사 에게 복종을 했는가?
# 지팡이는 몇 명의 다른 마법사 에게 복종 했을까?
# 입력 받는 값 처음은 지팡이 소유자, 두번째는 대결 횟수, 나머지는 앞에 있는 사람이 대결에서 우승자
# 주의사항 한번 지팡이를 소유했었던 사람이 대결을 통해 이겨서 지팡이 소유권을 가져도 카운팅 하지 않는다.
# 출력은 첫번째 줄은 최종 지팡이 소유자, 지팡이가 섬긴 마법사 수
# 지팡이 소유 여부 관련 코드로 짜는 것, 대결 중 이겨도 지팡이 소유 여부와 관련 없을때 처리 여부


current_obey = input()
obeyed = current_obey

if not current_obey.isupper(): exit(f"{current_obey} != upper")

duels = input()
if not duels.isdigit(): exit(f"{duels} != digit")
duels = int(duels)
if not 1 <= duels <= 100: exit(f"범위 벗어남(1 <= {duels} <= 100)")

for char in range(duels):
    duel = input()
    if not len(duel) == 3: exit(f"{duel} != len(3)")
    if not (duel[0].isupper() and duel[1] == " " and duel[2].isupper()):
        exit(f"{duel} != [A-Z][" "] [A-Z]")

    winner = duel[0]
    looser = duel[2]

    # if duel[2] == obeyed[-1] :
    if looser == current_obey:
        #obeyed += duel[0]
        current_obey = winner

        if obeyed.count(winner) == 0:
            obeyed += winner

print(current_obey)
print(obeyed)
print(len(obeyed))



