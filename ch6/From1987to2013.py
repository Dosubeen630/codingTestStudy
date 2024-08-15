# https://dmoj.ca/problem/ccc13s1
# 1987년 이후 각 년도에 나오는 숫자가 반복 없이 고유한 숫자를 가진 년도는 2013년도
# 입력 으로 주어진 년도 이후에 바로 다음 번 고유한 숫자를 가진 년도를 출력 하는 프로 그램
# 입력된 년도를 각 자리 별 숫자로 나누어 주고 그 수가 중복이 되는 것이 없는지 체크. 입력한 년도 이후 각 자리 별 숫자가 중복이 안되는 년도 출력하게 만들기

def checkYearNum(input_str, min_val, max_val):
    """
    사용자가 입력한 값이 숫자 인지, 그리고 주어진 범위 내에 있는지 확인 하는 함수
    :param str: 입력 받은 년도를 문자로 처리 하나씩 분리
    :param min: 입력한 값의 최소 범위
    :param max: 입력 한 값의 최대 범위
    :return num_str:
    """
    num_str = input_str.strip()
    if not num_str.isdigit(): exit(f"{num_str} is not digit.")
    num_str = int(num_str)
    if not min_val <= num_str <= max_val: exit(f"범위 에서 벗어남. ({min_val}<= {num_str} <= {max_val})")
    return num_str

starting_year = checkYearNum(input(), 0, 10000)

# 중복 되지 않은 연도 찾기
next_year = starting_year + 1
# 연도를 문자 열로 변환 한후, set()을 사용해, 중복된 숫자를 제거 하고, 원래의 문자열 길이와 집합의 길이를 비교. 길이가 같으면 중복된 숫자가 없는 것.
while True:
    year_str = str(next_year)
    if len(year_str) == len(set(year_str)):
        break
    next_year += 1

print(f"{next_year}")








