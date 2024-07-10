n , k = input().split()
arr = list(map(str , input().split()))
result = [s for s in arr if k not in s]
print(len(result))