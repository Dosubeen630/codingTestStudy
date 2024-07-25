target_people = input()  # P
if not target_people.isdigit(): exit(f"{target_people} != digit")
target_people = int(target_people)
if not target_people <= 100000000: exit(f"{target_people} <= 100000000")
day0_infection = input()  # day0 질병을 가지고 있는 사람 수 N
if not day0_infection.isdigit(): exit(f"{day0_infection} != digit")
day0_infection = int(day0_infection)
if not day0_infection <= target_people: exit(f"{day0_infection} <= {target_people}")
infect_r = input()  # R
if not infect_r.isdigit(): exit(f"{infect_r} != digit")
infect_r = int(infect_r)
if not infect_r <= 10: exit(f"{infect_r} <= 10")

after_day = 0
total_infection = day0_infection
prev_infection = day0_infection

while True:
    if total_infection > target_people:
        break

    total_infection = total_infection + prev_infection * infect_r
    prev_infection = prev_infection * infect_r

    after_day += 1
   # print(after_day, prev_infection, total_infection)

print(after_day)
