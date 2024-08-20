# https://usaco.org/index.php?page=viewproblem2&cpid=916
# 농부 존에겐 n개의 목초지 가 있음. 목초지 는 숫자가 매겨져 있음.
# m 마리의 소를 키우고 있음. 풀의 유형 범위 1-4
# 소들은 각자 좋아 하는 목초지 가 2개 있음. 소의 건강을 위해 두가지 목초지 에는 서로 다른 풀이 있어야 함.
# 그 목초지 를 좋아 하는 소는 최대 3마리 이하.

def read_cows(input_file, num_cows):
    """
    input_file 은 읽기 모드로 열려 있는 파일 입니다. 읽기를 시작 하면 소의 정보가 읽혀야 합니다.
    :param input_file: 입력 파일( 소가 좋아 하는 목초지 를 읽음.)
    :param num_cows: 소들의 수
    :return: 각 소가 좋아 하는 목초지 들의 리스트 반환. 리스트 내 각 항목은 한 마리의 소가 가장 좋아 하는 두 개의 목초지 를 가진 리스트 임.
    """
    favorites = []
    for i in range(num_cows):
        lst = input_file.readline().split()
        lst[0] = int(lst[0])
        lst[1] = int(lst[1])
        favorites.append(lst)
    return favorites
def cows_with_favorite(favorites, pasture):
    """
    :param favorites: read_cows 함수가 반환한 각 소가 좋아 하는 목초지 의 리스트
    :param pasture: 목초지 번호
    :return: 현재 목초지 를 좋아 하는 소들의 리스트 반환
    """
    cows = []
    for i in range(len(favorites)):
        if favorites[i][0] == pasture or favorites[i][1] == pasture:
            cows.append(i)
    return cows
def type_used(favorites, cows, pasture_types):
    """
    :param favorites: read_cows 함수가 반환한 소가 좋아 하는 목초지 의 리스트
    :param cows: 현재 목초지 를 좋아 하는 소들의 리스트
    :param pasture_types: 지금 까지 각 목초지 에 대해 선택된 풀 유형의 리스트
    :return: 소가 좋아 하는 목초지 를 기반 으로 이미 사용된 풀 유형의 리스트 를 반환
    """
    used = []
    for cow in cows:
        pasture_a = favorites[cow][0]
        pasture_b = favorites[cow][1]
        if pasture_a < len(pasture_types):
            used.append(pasture_types[pasture_a])
        if pasture_b < len(pasture_types):
            used.append(pasture_types[pasture_b])
    return used
def smallest_available(used):
    """
    :param used: 사용 된 풀 유형 들을 담은 리스트
    :return: 사용 되지 않은 가장 작은 번호의 풀 유형을 반환
    """
    grass_type = 1
    while grass_type in used:
        grass_type = grass_type + 1
    return grass_type
def write_pastures(output_file, pasture_types):
    """
    :param output_file: 쓰기 모드로 열려 있는 파일
    :param pasture_types: 목초지 에 심을 풀들의 유형이 정수로 담긴 리스트
    :return: pasture_types 를 output_file 에 씁니다.
    """
    pasture_types_str = []
    for pasture_type in pasture_types:
        pasture_types_str.append(str(pasture_type))
    output = ''.join(pasture_types_str)
    output_file.write(output + '\n')

input_file = open('revegetate.in', 'r')
output_file = open('revegetate.out', 'w')

lst = input_file.readline().split()
num_pastures = int(lst[0])
num_cows = int(lst[1])
favorites = read_cows(input_file, num_cows)

pasture_types = [0] # 미리 가상 인덱스 추가, 다음 입력 된 수는 1부터 시작 됨.

for i in range(1, num_pastures + 1):
    cows = cows_with_favorite(favorites, i)

    eliminated = type_used(favorites, cows, pasture_types)

    pasture_type = smallest_available(eliminated)
    pasture_types.append(pasture_type)

pasture_types.pop(0)
write_pastures(output_file, pasture_types)

input_file.close()
output_file.close()