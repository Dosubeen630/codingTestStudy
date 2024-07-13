# https://dmoj.ca/problem/ccc20j2
# People who study epidemiology use models to analyze the spread of disease. In this problem, we use a simple model.
# 역학을 연구하는 사람들은 모델을 사용하여 질병의 확산을 분석 합니다. 이 문제에서는 간단한 모델을 사용 합니다.
# When a person has a disease, they infect exactly R other people but only on the very next day.
#  사람이 질병에 걸리면 그들은 정확히 R 만큼의 다른 사람들을 다음 날에 감염시킵니다.
# No person is infected more than once. We want to determine when a total of more than P people have had the disease.
# 한 번 이상 감염 되는 사람은 없습니다. 우리는 총 P명 이상의 사람들이 언제 질병에 걸렸는지 확인하고 싶습니다.
# (This problem was designed before the current coronavirus outbreak, and we acknowledge the distress currently being experienced by many people worldwide because of this and other diseases.
# 이 문제는 현재 코로나 바이러스 가 발생 하기 전에 고안 되었으며, 우리는 현재 이 질병과 다른 질병으로 인해 전 세계 많은 사람들이 고통을 겪고 있음을 인정합니다.
# We hope that including this problem at this time highlights the important roles that computer science and mathematics play in solving real-world problems.)
# 이 번에 이 문제를 포함 시키면 컴퓨터 과학과 수학이 실제 문제를 해결 하는데 중요한 역할을 한다는 점을 강조 할 수 있기를 바랍니다.
# There are three lines of input. Each line contains one positive integer. The first line contains the value of P.
# 입력 라인은 3개 입니다. 각 줄에는 하나의 양의 정수가 포함 됩니다. 첫번째 줄에는 다음 값이 포함 됩니다.
# The second line contains N, the number of people who have the disease on Day 0.
#  두번째 줄에는 0일째에 질병에 걸린 사람의 수인 N이 포함 됩니다.
#  The third line contains the value of R. Assume that P <= 10의7승 and N <= P and R <= 10.
# 세번째 줄에는 R 값이 포함 되어 있습니다. P <= 10의 7승 및 N <= P 및 R <= 10 이라고 가정 합니다.
# Output the number of the first day on which the total number of people who have had the disease is greater than P.
# 질병에 걸린 총 사람의 수가 다음 보다 큰 첫날의 수를 출력 하십시오.
# 도메인 분석: 질병 확산을 분석 하는 모델임. 사람이 질병에 걸리면 정확히 R을 감염시킴. 다른사람들은 걸린 다음날에 감염 시킴.
# 한번 이상 감염된 사람은 없음. 총 P명의 사람들이 언제 질병에 걸렸는지 알고 싶어함.
# 사용자 에게 입력 받는 것 -  P, day 0 에 걸린 사람 N, 질병에 걸린 사람들이 감염 시키는 수 R
target_people = input() #P
if not target_people.isdigit(): exit(f"{target_people}의 입력 형태는 숫자 입니다. 숫자로 입력 해 주세요.")
target_people = int(target_people)
if not target_people <= 100000000: exit(f"{target_people}의 범위에 벗어 났습니다.")
day0_infection = input() # day0 질병을 가지고 있는 사람 수 N
if not day0_infection.isdigit(): exit(f"{day0_infection}의 입력 형태는 숫자 입니다. 숫자로 입력 해 주세요.")
day0_infection = int(day0_infection)
if not day0_infection <= target_people: exit(f"{day0_infection}의 범위에 벗어 났습니다.")
infect_r = input() #R
if not infect_r.isdigit(): exit(f"{infect_r}의 입력 형태는 숫자 입니다. 숫자로 입력 해 주세요.")
infect_r = int(infect_r)
if not infect_r <= 10: exit(f"{infect_r}의 범위에 벗어 났습니다.")

# 슬롯머신 문제와 비슷한 점 - 가지고 있는 동전 수, 기계 3개를 순서 대로 플레이, 각 머신마다 특정 플레이 횟수에 다다르면 상금을 지불해 줌. 그 돈으로 추가 플레이 가능.
# 이 문제는 총 감염돌 것으로 예측된 사람들 수, 첫번째 날 감염자, 그 이후 한명당 감염 시키는 사람 수 타켓인원보다 감염자가 많아지는 날 구하기

after_day = 1
days_total = day0_infection


while days_total <= target_people:
       days_total = day0_infection* infect_r
       day0_infection = day0_infection + days_total * infect_r
       after_day += 1


print(after_day)













