def find_kth_number(n, k, numbers):
    # 2진수에서 1의 개수를 세는 함수
    def count_ones(num):
        return bin(num).count('1')

    # 정렬 기준 설정: 2진수의 1의 개수 -> 원래 숫자
    sorted_numbers = sorted(numbers, key=lambda x: (count_ones(x), x), reverse=True)

    # k번째 수 반환 (0-index이므로 k-1 사용)
    return sorted_numbers[k-1]

# 입력 받기
n, k = map(int, input().split())
numbers = list(map(int, input().split()))

# k번째 수 찾기
result = find_kth_number(n, k, numbers)
print(result)