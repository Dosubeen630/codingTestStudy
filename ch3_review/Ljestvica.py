# https://dmoj.ca/problem/coci12c5p1
# A-minor : A,D,E / C-major : C,F,G
# 악센트가 있는 성조( 각 소절의 첫번째 성조) 중 A단조 또는 C 장조의 기본 성이 더 있는지 계산 하여
# 작곡이 A단조 또는 C 장조로 작성 될 가능성이 더 높은지 결정 하는 프로 그램을 작성 합니다.

tones_set = "ABCDEFG|"
tones = input()
if tones[0] not in tones_set and tones[-1] not in tones_set:
    exit(" 악보 맨 앞과 맨 뒤는 음이 와야 합니다.")
if not 2 <= len(tones) <= 100: exit(f"범위 넘어감(2<= {tones} <= 100)")
for char in tones:
    if not char in tones :
        exit(f"{tones}의 입력 값은 ABCDEFG| 만 가능 합니다.")

A_minor = 0
C_major = 0

for i in range(len(tones)):
    if i == 0 or tones[i-1] == "|":
        if tones[i] in "ADE":
            A_minor += 1
        elif tones[i] in "CFG":
            C_major += 1


if A_minor > C_major:
    print("A-mol")
elif A_minor < C_major:
    print("C-dur")
elif A_minor == C_major and tones[-1] == "A":
    A_minor += 1
    print("A-mol")
elif A_minor == C_major and tones[-1] == "C":
    C_major += 1
    print("C-dur")
else:
    pass

