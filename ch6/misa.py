#https://dmoj.ca/problem/coci13c2p2
# 주어진 좌석 배치에서 사람이 앉을 최적의 위치를 찾아 손을 잡는 횟수 계산
# 미르코가 가능한 많은 사람과 악수 할 수 있는 곳을 찾는 것
# 이웃의 정의 -> 좌우, 상하, 대각선 방향 모두 포함. 손 잡기는 상호적. 중복 계산 방지를 위해 답에서 나중에 2를 나눠 줘야함.
# 최적화 된 자리 찾기 위해서 가장 많은 이웃이 있는 빈좌석 찾기!
# 좌석 배열로 인한 경계 처리도 중요!

# 좌석 주변의 인접한 'o'의 개수를 세는 함수
def count_handshakes(grid, row, col):
    """
    direction 은 8방향을 의미. (1,0)은 한칸 아래, (0,1)은 한칸 오른쪽.
    이 코드는 각 방향 으로 이동한 자리에 사람이 있으면('o') 손을 잡을 수 있으니 count 를 1씩 더함.
    :param grid: 좌석의 배치 정보
    :param row: 앉은 자리의 위치 행
    :param col: 앉은 자리의 위치 열
    :return: count 몇 몇과 손을 잡을 수 있는지 숫자를 반환
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    count = 0
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] == 'o':
                count += 1
    return count

# Mirko가 앉을 좌석을 찾는 함수
def find_best_seat(grid):
    best_row, best_col = -1, -1
    max_handshakes = -1

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # 각 빈 자리에 대해 count_handshakes 함수를 사용 해서 몇 명과 손을 잡을 수 있는지 계산
            if grid[row][col] == '.':
                handshakes = count_handshakes(grid, row, col)
                # 그 중에서 가장 많은 손을 잡을 수 있는 자리를 best_row와 best_col에 저장.
                if handshakes > max_handshakes:
                    max_handshakes = handshakes
                    best_row, best_col = row, col

    return best_row, best_col # 마지막에 미르코가  앉을 자리와 좌표를 반환

# 전체 손을 잡는 횟수를 계산하는 함수
def total_handshakes(grid):
    """ 사람이 앉아 있는 자리('o')만 살펴서 그 사람과 이웃 하는 사람들과 손을 잡은 횟수를 total에 더함."""
    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 'o':
                total += count_handshakes(grid, row, col)
    return total // 2  # 서로 손을 잡는 것이 중복되므로 2로 나눔

# 입력 처리
r, s = map(int, input().split())
if not 1 <= r <= 50 and 1 <= s <= 50: exit(f" 범위 벗어남 (1 <= {r},{s} <= 50).")
grid = []

for i in range(r):
    row_input = input().strip()  # 좌석 정보를 입력 받음

# 입력된 좌석 정보가 정확히 s개의 문자 인지 확인
    if len(row_input) != s:
        raise ValueError(f"{i+1}번째 행에 {s}개의 문자가 입력되어야 합니다. 현재 입력된 문자 수: {len(row_input)}")

    # 각 문자가 유효 한지 확인 ('o' 또는 '.' 만 가능)
    for char in row_input:
        if char not in ('o', '.'):
            raise ValueError(f"유효하지 않은 문자 '{char}'가 입력되었습니다. 'o' 또는 '.'만 사용하세요.")

    # 유효한 입력만 grid에 추가
    grid.append(list(row_input))

# Mirko 가 앉을 좌석을 찾고 그 좌석에 앉음
mirko_row, mirko_col = find_best_seat(grid)
if mirko_row != -1 and mirko_col != -1:
    grid[mirko_row][mirko_col] = 'o'

# 전체 손을 잡는 횟수를 계산 하고 출력
print(total_handshakes(grid))
