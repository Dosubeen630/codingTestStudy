# https://dmoj.ca/problem/coci18c3p1

text = input()
if not text.isupper():exit(f"{text} != upper")
if not 1 <= len(text) <= 100000: exit(f"범위 벗어남 (1<= {len(text)} <= 100000)")

prev = None
honi_blocks = 0

for char in text:
    if char == 'H' and (prev == 'I'or prev is None):
       prev = 'H'
    elif char == 'O'and prev == 'H':
        prev = 'O'
    elif char == 'N'and prev == 'O':
        prev = 'N'
    elif char == 'I' and prev == 'N':
        prev = 'I'
        honi_blocks += 1
    else:
        pass

print(honi_blocks)


