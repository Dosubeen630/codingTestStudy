# https://dmoj.ca/problem/coci18c4p1
# After having watched all eight Harry Potter movies in a week, Nikola finally realized how the famous Elder Wand changes the wizard it obeys.
# 일주일 동안 해리포터 영화를 8편을 모두 본후, 니콜라는 유명한 딱총나무 지팡이가 자신이 따르는 마법사를 어떻게 변화 시키는지 마침내 깨달았습니다.
# If wizard A, whom the wand is currently obeying, is defeated by wizard B in a duel, then the wand will start obeying the wizard B.
# 현재 지팡이가 복종하고 있는 마법사 A가 결투에서 마법사 B에게 패배하면 지팡이는 마법사 B에게 복종하기 시작합니다.
# Nikola is now wondering what would happen if 26 wizards labeled with uppercase letters of the English alphabet from A to Z began fighting in duels for the fondness of the Elder Wand.
# 니콜라는 이제 A부터 Z까지 영어 알파벳 대문자로 표시된 26명의 마법사가 딱총 나무 지팡이를 좋아하기 위해 결투를 벌이기 시작하면 어떤 일이 일어날지 궁금해 하고 있습니다.
# If we know the label of the wizard that the wand had obeyed before all duels and the outcomes of all N duels that were held one after another, answer_num the following questions:
# 모든 결투 전에 지팡이가 순종했던 마법사의 낙인 과 모든 결투의 결과를 안다면 결투가 연달아 열리면 다음의 질문에 답하시오.
# Which wizard did the wand obey after all N duels?
# n번의 결투를 모두 마친 후 지팡이는 어느 마법사에게 복종했습니까?
# How many different wizards did the wand obey?
# 지팡이는 몇 명의 다른 마법사에게 복종했습니까?
# The first line contains an uppercase letter of the English alphabet, the label of the wizard that the wand obeyed at the beginning.
# 첫번째 줄에는 지팡이가 처음에 복종했던 마법사의 라벨인 영어 알파벳의 대문자가 포함되어 있습니다.
# The second line contains an integer number N (1<= N<= 100), the number of duels from the text of the task.
# 두번째 줄에는 작업 텍스트의 결투 횟수인 정수 n이 포함됩니다.
# In the next N rows there are two different uppercase letters of the English alphabet Z1 and Z2 separated by a space, whereas the wizard with the label Z1
#  defeated the wizard with the label Z2 in the ith duel.
# 다음 n 행에는 공백으로 구분된 두 개의 서로 다른 영어 알파벳 대문자 z1,z2가 있는 반면, 레이블z1이 있는 마법사는 i번째 결투에서 라벨 z2의 마법사를 물리쳤습니다.
# In the first line print an uppercase letter of the English alphabet, answer_num to the first question from the task description.
# 첫번째 줄에는 영어 알파벳의 대문자를 인쇄하고 작업설명 첫번째 질문에 답하시오.
# In the second line print an integer number, answer_num to the second question from the task description.
# 두번째 줄에는 정수를 인쇄하고 작업설명의 두번째 질문에 답하시오.
# scoring : Correct answer_num to the first question is worth 2 points and the correct answer_num to the second question is worth 3 points. If you do not know how to solve some part of the task, then print any value in the corresponding line.
# 점수 : 첫번째 질문의 정답은 2점, 두번째 질문의 정답은 3점입니다. 작업의 일부를 해결하는 방법을 모를경우 해당 줄에 값을 인쇄하십시오.

# 입력 받아야 할 것들 : 처음 지팡이 소유한 마법사, 결투횟수, 결투한 마법사들
wizard = input()
if not wizard.isalpha():
    exit("입력값 형태가 잘못 되었습니다. 문자로 입력해주세요.")
if not wizard.isupper():
    exit("대문자로 입력해주세요.")
duel = input()
if not duel.isdigit():
    exit("숫자의 형태로 입력 해주세요.")
duel = int(duel)
if not 1<= duel <= 100:
    exit("입력한 값의 범위가 벗어났습니다.")
# 결투 에서 이겨 지팡이를 소유한 마법사 변수 선언, 지팡이가 복종을 한 마법사 수
z1 = 0
winner_wizard = wizard
# 우선은 입력 받은 결투 횟수에 근거한 사용자 에게 결투에 참여한 마법사 이름을 받을 수 있게 구현
for n in range(duel):
    duel_fight = input() # 결투 횟수 입력 받음.
    winner_wizard = duel_fight[0] # 결투에서 이긴 마법사는 리스트 의 맨 처음에 넣어줌.
    loser_wizard = duel_fight[2] # 결투에서 진 마법사는 리스트의 마지막에 넣어줌.

    if duel_fight[0] == wizard: # 결투에서 이긴 마법사가 원래 지팡이를 소유한 마법사 일때,
        winner_wizard = wizard
        print(winner_wizard)

    elif duel_fight[0] != wizard: # 결투에서 이긴 마법사가 원래 지창이를 소유한 마법사가 아닐때,
        winner_wizard = duel_fight[0]
        z1 += 1
        print(winner_wizard)

    else: #not winner_wizard in duel_fight: # 결투에서 이긴 마법사가 지팡이 소유와 상관이 없을때,
        winner_wizard = duel_fight[1]
        print(winner_wizard)

# 결투에 참여한 마법사 중, 이긴 사람이 앞에 위치, 이긴 사람과 지팡이 소유자 비교


print(winner_wizard)
print(z1)






