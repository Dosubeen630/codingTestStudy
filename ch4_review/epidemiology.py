# https://dmoj.ca/problem/ccc20j2
# 주어 지는 정보는 타겟 인원 (대략 질병에 타겟 인원 만큼 걸리는데 얼마나 걸리는지 보려고),
# 감염률, 초기 감염자(전날 감염자) 중요 사항은 전날 감염자는 다시 감염 되지 않고 그 다음날 감염자를 구하는데 중요함.

target_people = input()
if not target_people.isdigit() : exit(f"{target_people} != digit")
target_people = int(target_people)
if not target_people <= 10**7: exit(f" 범위 벗어남 ({target_people} <= 10 **7)")

infected_people = input()
if not infected_people.isdigit(): exit(f"{infected_people} != digit")
infected_people = int(infected_people)
if not infected_people <= target_people: exit(f"({infected_people} <= {target_people})")

infection_rate = input()
if not infection_rate.isdigit() : exit(f"{infection_rate} != digit")
infected_rate = int(infection_rate)
if not infected_rate <= 10: exit(f"범위 벗어남({infection_rate} <= 10)")

isAllInfected = False
total_infected_people = infected_people
prev_infected_people = infected_people
target_day = 0
while not isAllInfected:

    if target_people < total_infected_people:
        isAllInfected = True
        break

    total_infected_people = total_infected_people + prev_infected_people * infected_rate
    prev_infected_people = prev_infected_people * infected_rate
    target_day += 1

print(target_day)



