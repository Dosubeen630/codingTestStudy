# 정사각형 개수를 세는 함수
def count_squares(n):
    total_squares = 0
    for k in range(1, n+1):
        total_squares += (n - k + 1) ** 2
    return total_squares

# 입력 받기
n = int(input())

# 결과 계산
result = count_squares(n)
print(result)