current_obey = input()

if not current_obey.isalpha():
    exit("입력값 형태가 잘못 되었습니다. 문자로 입력해주세요.")
if not current_obey.isupper():
    exit("대문자로 입력해주세요.")

duel = input()
if not duel.isdigit():
    exit("숫자의 형태로 입력 해주세요.")
duel = int(duel)
if not 1 <= duel <= 100:
    exit("입력한 값의 범위가 벗어났습니다.")

obeyed = current_obey
for n in range(duel):
    duel_fight = input()
    winner_wizard = duel_fight[0]
    loser_wizard = duel_fight[2]

    if loser_wizard == current_obey:
        current_obey = winner_wizard

        if obeyed.count(winner_wizard) == 0:
            obeyed += winner_wizard

print(current_obey)
print(len(obeyed))
