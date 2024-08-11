# https://dmoj.ca/problem/ccc99s1
# 카드 한벌로 플레이 하는 간단한 2인 게임의 점수를 기록 하는 프로 그램 작성
# 덱에는 52장의 카드가 있고, 13개의 가능한 이름 중 유형당 4장.
# 잭, 퀸, 킹, 에이스 라고 표시된 카드를 통칭 하여 하이 카드 라고 합니다.
# 플레이어 A는 맨 위 카드를 뒤집어 더미 위에 놓습니다. 그런 다음 플레이어 B는 맨 위 카드를 뒤집어 더미 위에 놓습니다. 데크가 소진될 때까지 A와 B가 번갈아 가며 나타납니다. 게임은 다음과 같이 채점됩니다.
# ace -> 최소 4장 뒤집 어야 하는 카드 남음. 남은 카드는 하이 카드, 4점 획득
# king -> 최소 3장 뒤집어 야 할 카드 남음. 다음 카드는 없음. 3장의 카드는 높은 카드. 3점 획득
# queen -> 최소 2장 뒤집어 야 할 카드 남음. 다음 카드 없음. 2장의 카드는 높은 카드. 2점 획득
# jack -> 최소 1장 뒤집어 야 할 카드 남음. 다음 카드 없음.  다음 카드가 높은 카드가 아닐 경우. 1점 득점
# 입력 52줄 카드의 이름을 포함. 소문자. 첫번째 줄은 뒤집어 질 첫번째 카드 나타냄. 다음 줄은 다음 카드 등등
# 출력은
# Player A: n point(s).
# Player B: m point(s). 마지막 두줄은 각 플레 이어의 최종 점수를 출력 해줌.
# 함수로 만들 어야 하는것 -> 몇장의 카드 남았 는지, 높은 카드는 없는지 확인 하는것 합수로 구현.

# 높은 카드가 있는지 확인 하는 함수
def check_high_card(card_name_list, index, required_cards):
    """
    주어진 카드 리스트 에서 특정 위치의 카드 이후에 하이 카드(ace,king,queen,jack)가
    있는지 확인 합니다.
    index 는 현재 카드의 위치를 나타 내고, required_cards 는 검사 해야할 카드의 개수를 의미 합니다.
    높은 카드가 존재 하지 않으면 True를 반환 합니다.
    """
    high_card = ["ace", "king", "queen", "jack"]
    if index + required_cards < len(card_name_list):
        if all(card not in card_name_list[index+1:index+1+required_cards] for card in high_card):
            return True
    return False

# 점수를 계산 하는 함수
def calculate_score(card_name_list, index):
    """
    특정 위치의 카드가 하이 카드(ace,king,queen,jack)인지 확인 하고, 'check_high_card' 함수를
    호출 하여 점수를 계산 합니다.
    ace,king,queen,jack 에 대해 각각 4,3,2,1점을 반환 합니다.
    해당 카드가 없으면 0점을 반환 합니다.
    :param card_name_list:
    :param index:
    :return 0:
    """
    if card_name_list[index] == "ace":
        if check_high_card(card_name_list, index, 4):
            return 4
    elif card_name_list[index] == "king":
        if check_high_card(card_name_list, index, 3):
            return 3
    elif card_name_list[index] == "queen":
        if check_high_card(card_name_list, index, 2):
            return 2
    elif card_name_list[index] == "jack":
        if check_high_card(card_name_list, index, 1):
            return 1
    return 0

# 각 플레 이어의 점수를 출력 하는 함수
def print_individual_scores(card_name_list):
    """
    각 플레 이어의 차례에 따라 점수를 계산 하고, 해당 점수를 출력 합니다.
    플레 이어 A와 B의 전체 점수를 반환 합니다.
    :param card_name_list:
    :return a_score, b_score:
    """
    a_score = 0
    b_score = 0

    for i in range(len(card_name_list)):
        if i % 2 == 0:  # Player A's turn
            points = calculate_score(card_name_list, i)
            a_score += points
            if points > 0:
                print(f"Player A scores {points} point(s).")
        else:  # Player B's turn
            points = calculate_score(card_name_list, i)
            b_score += points
            if points > 0:
                print(f"Player B scores {points} point(s).")

    return a_score, b_score

# 최종 점수를 출력하는 함수
def print_final_scores(a_score, b_score):
    """
    print_individual_scores 함수 에서 반환된 최종 점수를 받아 최종 결과를 출력 합니다.
    :param a_score:
    :param b_score:
    :return:
    """
    print(f"Player A: {a_score} point(s).")
    print(f"Player B: {b_score} point(s).")

# 카드 입력 받기
VALID_CARDS = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]

card_name_list = []

for i in range(52):
    while True:
        card_name = input().strip().lower()
        if card_name in VALID_CARDS:
            card_name_list.append(card_name)
            break
        else:
            print("유효하지 않은 카드 이름입니다. 다시 입력해주세요.")

# 각 플레이어의 점수를 계산 및 출력
a_score, b_score = print_individual_scores(card_name_list)

# 최종 점수 출력
print_final_scores(a_score, b_score)







