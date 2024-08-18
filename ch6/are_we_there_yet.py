# https://dmoj.ca/problem/ccc18j3
# 직선 도로를 운전중. 이 길을 따라 5개의 도시가 있음. 연속된 각 도시 쌍 사이의 거리 기록.
# 내가 만난 두 도시 사이의 거리를 나타 내는 거리 테이블 을 계산 하려고 함.
# 입력 값은 인접한 두 마을 사이의 거리 차이 5마을 중 인접한 마을 간의 거리 차이니 입력 된 값은 4.
# 출력은 1번마을 에서 5번 마을 까지의 각 마을 간의 거리 차이로 총 5줄이 출력 되어야 함.
# 여기서 알수 있는 것은 행렬로 나타 낸다면, i와 j의 값이 같으면 숫자 0, ij = ji 이면 숫자가 같음.
# 연속 된 도시들 사이의 거리를 알고 있음. 모든 도시 사이의 거리를 계산 하려면 ->
# 도시 1 에서 도시 2, 도시2 에서 도시3, 그리고 도시3 에서 도시 4 까지의 거리를 모두 더하면 도시1과 도시 4의 거리를 알수 있음.
# 모든 도시 간의 거리를 표로 만들어 출력 하는 것이 목표임.

distance_difference = input().strip(" ")
#if not distance_difference.isdigit(): exit(f"{distance_difference}is not integer.")

# 입략 값이 4개의 숫자로 이루어 져 있는지 확인
distance_list = distance_difference.split()
if len(distance_list) != 4:
    exit(f"{len(distance_list)}개 입니다. 값은 4개 여야 합니다.")
#  각 값이 숫자 인지 확인 하고, 숫자로 변환
try:
    distances = [int(x) for x in distance_list]
except ValueError:
    exit(f"'{distance_difference}' 에는 정수가 아닌 값은 들어 갈 수 없습 니다.")


# 도시 간의 거리 테이블을 계산 하는 함수
def calculate_distance_table(distances):
    # 5*5 distance table  0 으로 초기화
    distance_table = [[0] * 5 for _ in range(5)]

    # 거리 계산 및 테이블 채우기
    for i in range(5):
        for j in range(i+1, 5):
            distance_table[i][j] = distance_table[i][j-1] + distances[j-1]
            distance_table[j][i] = distance_table[i][j] # 대칭 관계

    return distance_table

distance_table = calculate_distance_table(distances)
for row in distance_table:
    print(" ".join(map(str, row)))


