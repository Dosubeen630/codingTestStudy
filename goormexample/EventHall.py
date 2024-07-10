def max_events(n, events):
    # 종료 시간과 시작 시간을 기준으로 정렬
    events.sort(key=lambda x: (x[1], x[0]))

    count = 0
    last_end_time = -1

    for start, end in events:
        if start > last_end_time + 1:
            count += 1
            last_end_time = end

    return count

# 입력 받기
# n = int(input())
# events = [tuple(map(int, input().split())) for _ in range(n)]

# n = 6
# events = [(1,2),(2,3),(3,6),(4,5),(1,10),(11,13)]
n = 7
events = [(1,2),(3,3),(3,5),(4,10),(5,6),(7,9),(10,11)]
# 최대 행사 개수 계산
result = max_events(n, events)
print(result)