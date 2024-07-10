def count_valid_numbers(n, k, numbers):
    valid_numbers = [num for num in numbers if k not in str(num)]
    return len(valid_numbers)

# 입력 받기
n, k = input().split()
n = int(n)
numbers = list(map(int, input().split()))

# 유효한 숫자의 개수 계산
result = count_valid_numbers(n, k, numbers)
print(result)