# https://usaco.org/index.php?page=viewproblem2&cpid=855

# 세가지 맛 우유 있음. 각 우유를 섞어서 새로운 맛의 우유를 만들고자 함. 100회 섞고 난 후 각 양동이에 남은 우유의 양 출력
# 양동이 1 -> 양동이 2, 양동이 2 -> 양동이 3, 양동이 3 -> 양동이 1, 양동이 1 -> 양동이 2 이런 순서로 순환됨.
# 100번 우유를 섞고나면 1번 순환된 이후의 양동이 1-> 양동이 2로 우유 섞어 줬을때랑 남은 양 같음.

# 어느 양동이랑 어느 양동이가 섞이는 순서인지, 100번 섞는 것은 간단하게 모듈러 연산으로 처리.
# 각 양동이가 섞이면 그 양동이 안의 우유 양 구하기
NUM_BUCKETS = 3
def turn_buckets(input_file, NUM_BUCKETS):
    """
    input_file: 입력 파일 객체
    num_buckets: 양동이 의 개수

    각 양동이 의 (용량, 현재 우유 양)을 리스트 로 반환.
    """
    buckets = [(c1,m1), (c2,m2), (c3, m3)]
    for _ in range(NUM_BUCKETS):
        capacity_bucket = list(map(int, input_file.readline().split()))
        milk_amount = list(map(int, input_file.readline().split()))
        buckets.append(capacity_bucket)
        buckets.append(milk_amount) # (양동이 의 용량, 현재 우유 양)
    return buckets

def mix_milk(c1, m1, c2, m2, c3, m3, num_iterations=100):
    """
    buckets: 각 양동이 의 (용량, 현재 우유 양)을 담은 리스트
    num_iterations: 섞어 주는 횟수 (기본값: 100)

    각 양동이 에 남아 있는 우유의 양을 반환
    """
    for i in range(num_iterations):
        current_bucket = i % 3  # 현재 우유를 붓는 양동이 (순환)
        next_bucket = (i + 1) % 3  # 다음 양동이

        # 현재 양동이 에서 다음 양동이 로 부을 수 있는 최대 우유 양 계산
        pour_amount = min(buckets[current_bucket][1], buckets[next_bucket][0] - buckets[next_bucket][1])

        # 현재 양동이 에서 우유를 부음
        buckets[current_bucket] = (buckets[current_bucket][0], buckets[current_bucket][1] - pour_amount)
        # 다음 양동이 에 우유를 받음
        buckets[next_bucket] = (buckets[next_bucket][0], buckets[next_bucket][1] + pour_amount)

    return buckets[0][1], buckets[1][1],buckets[2][1]  # 각 양동이 에 남아 있는 우유의 양 반환

# 입력 파일 처리
input_file = open("mixmilk.in", "r")
c1, m1 = list(map(int,(input_file.readline().split())))
c2, m2 = list(map(int,(input_file.readline().split())))
c3, m3 = list(map(int,(input_file.readline().split())))

# 양동이 정보 읽어 오기
buckets = turn_buckets(input_file, NUM_BUCKETS)

# 우유 섞기 작업 수행
final_milk_amounts = mix_milk(c1,m1,c2,m2,c3,m3, num_iterations=100)

# 출력 파일 처리
output_file = open("mixmilk.out", "w")
for amount in final_milk_amounts:
    output_file.write(f"{amount}\n")

# 파일 닫기
input_file.close()
output_file.close()
