# https://dmoj.ca/problem/coci16c1p1
# 페로는 매달 X 메가 바이트의 데이터를 제공 받는다. 사용하고 남은 데이터는 이월가능 -> 좋은 조건, 바뀔 가능성 있음.
# 첫째 줄은 매달 제공 받는 데이터양, 둘째 줄은 사용 한 달과 그 달에 사용한 데이터 양을 보여줌.
# 출력은 다음 달에 사용 할 수 있는 데이터의 총양

mbPerMonth = input()
if not mbPerMonth.isdigit():exit(f"{mbPerMonth} != digit")
mbPerMonth = int(mbPerMonth)
if not 1 <= mbPerMonth <= 100:exit(f"범위 벗어남(1 <= {mbPerMonth} <= 100)")

spendMonths = input()
if not spendMonths.isdigit():exit(f"{spendMonths}!= digit")
spendMonths = int(spendMonths)
if not 1 <= spendMonths <= 100: exit(f"범위 벗어남 (1 <= {spendMonths} <= 100)")

availableMb = mbPerMonth * (spendMonths + 1)

for i in range(spendMonths):
    spendMb = input()
    if not spendMb.isdigit():exit(f"{spendMb} != digit")
    spendMb = int(spendMb)
    if not 0 <= spendMb <= 10000: exit(f" 범위를 벗어남 (0<= {spendMb}<= 10000)")
    availableMb -= spendMb
    if availableMb < 0: exit("사용 가능한 데이터가 없습니다.")
print(availableMb)




