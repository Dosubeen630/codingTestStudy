# https://acm.timus.ru/problem.aspx?space=1&num=2144

# 엄마가 lena에게 방 청소를 시켰고, 마지막 으로 남은 일은 액션 피규어가 담긴 상자를 모두 선반에 놓는 것
# 레나는 1부터 n까지 번호가 매겨진 n개의 상자를 가지고 있음.
# 상자 번호 i에는 각각 고유한 크기의 aij를 가진 ki 액션 피규어가 들어 있습니다.
# 레나는 빨리 끝내기를 원하지만 모든 그림을 크기에 따라 감ㅅ소하지 않는 순서로 배치하는 것이 매우 중요.
# 불가능 하다면 청소가 완료 될 수 없음. 레나는 상자가 꽤 많아서 그걸 다 할수 있을지 확신이 없음.
# 포장을 찢어야 하기 때문에 절대 열지 않고, 모든 인물 감상 하는 것을 좋아해서 상자에는 투명한 한쪽면만 있으므로 상자를 압뒤로 배치하는 것은 불가
# Lena가 엄마에게 대포 청소가 끝났다고 말할 수 있는지, 아니면 가능하고 어쨌든 선반에 상자를 정리해야 하는지 확인하도록 도와주세요.

def read_boxes(n):
    """
    입력 받은 상자의 개수 n에 따라 각 상자의 피규어 크기 정보를 리스트로 입력 받아
    'boxes'에 저장 함.
    :param n:
    :return boxes:
    """
    boxes = []
    for i in range(n):
        data = input().split()
        figures = []
        for j in range(1, len(data)):
            figures.append(int(data[j]))
        boxes.append(figures)
    return boxes

def check_all_boxes_sorted(boxes):
    """
    각 상자 안의 피규어 들이 오름차순 으로 정렬 되어 있는지 확인 하는 함수
    하나 라도 정렬 되어 있지 않으면 'False'를 반환 하고 모든 상자가 정렬 되어 있으면
    'True'를 반환.
    :param boxes:
    :return True:
    """
    for box in boxes:
        for i in range(len(box) - 1):
            if box[i] > box[i + 1]:
                return False
    return True

def create_box_edges_list(boxes):
    """
    각 상자의 첫번 째 피규어와 마지막 피규어의 크기를 튜플로 만들어
    'first_last_list'에 저장
    이 함수는 상자 양 끝에 있는 액션 피규어의 높이를 기반으로 새로운 리스트를 생성함.
    :param boxes:
    :return first_last_list:
    """
    first_last_list = []
    for box in boxes:
        first_figure = box[0]
        last_figure = box[-1]
        first_last_list.append((first_figure, last_figure))
    return first_last_list

def is_sorted_by_edges(box_edges):
    """
    create_box_edges_list 함수 에서 얻은 리스트를 첫 번째 피규어의 크기 순서 대로 정렬.
    정렬된 리스트를 사용하여 상자들이 크기 순서대로 연결 될 수 있는 지 확인
    :param box_edges:
    :return True:
    """
    # 첫 번째 피규어의 크기 순서대로 박스들을 정렬
    for i in range(len(box_edges) - 1):
        for j in range(i + 1, len(box_edges)):
            if box_edges[i][0] > box_edges[j][0]:
                # 정렬
                temp = box_edges[i]
                box_edges[i] = box_edges[j]
                box_edges[j] = temp

    # 정렬된 상자들이 잘 연결되는지 확인
    for i in range(len(box_edges) - 1):
        if box_edges[i][1] > box_edges[i + 1][0]:
            return False
    return True

# 프로그램 실행
n = int(input())
if not 1 <= n <= 100:
    exit(f"상자의 개수는 1에서 100 사이여야 합니다. 입력된 값: {n}")
else:
    boxes = read_boxes(n)

    if not check_all_boxes_sorted(boxes):
        print("NO")
    else:
        box_edges = create_box_edges_list(boxes)
        if is_sorted_by_edges(box_edges):
            print("YES")
        else:
            print("NO")
