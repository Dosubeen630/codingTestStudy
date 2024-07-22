# https://dmoj.ca/problem/dmopc15c7p2

# 이 문제의 목적에 따라 단어는 공백이 아닌 문자의 최대 연속 그룹 입니다.
# 텍스트에서 읽어야 하는 단어 수를 세면 됩니다.
# 입력은 오직 소문자와 공백만 포함된 텍스트 입니다. 유일한 제약은 전체 텍스트의 길이가 80자를 넘지 않는 다는것!
# 출력은 텍스트 안에 단어의 수

word= input()
if not word.islower(): exit(f"{word} != islower")

result = word.count(' ') + 1

print(result)