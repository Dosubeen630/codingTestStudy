# https://dmoj.ca/problem/wc16c1j1
# But just how spooky is this demonic festival? Its spookiness level can, in fact, be measured and represented as a single intege S(2<=S<=20).
# 하지만 이 악마의 축제는 얼마나 으스스 한가요? 실제로 그 으으스함 수준은 단일 정수로 측정 되고 표현 될 수 있습니다.
# Given the integer S, can you cast a spooky incantation on your computer to have it produce the corresponding spooky word?
# 정수 S가 주어 지면 컴퓨터에 으스스한 주문을 걸어 해당 으으스한 단어가 생성 되도록 할수 있나요?
#  입력에 정수 S가 주어 지면, 출력에 S의 수만큼 o가 추가 되어 spooky가 출력되게 하시오.

spooky_num = input()
if not spooky_num.isdigit(): exit(f"{spooky_num} != digit")
spooky_num = int(spooky_num)
if not 2 <= spooky_num <= 20: exit(f"{spooky_num}의 범위가 아닙니다.")

result = "sp" + spooky_num * "o" + "ky"

print(result)