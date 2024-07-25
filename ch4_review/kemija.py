# https://dmoj.ca/problem/coci08c3p2
# 문장에 모음 ( a,e,i,o,u) 가 나오면 모음을 한번 더 반복 하고 p를 추가해 줌.
# 이렇게 변형 된 조건의 문장을 다시 원래의 문장 으로 돌리는 프로 그램 만들기
# 고민 해보기 : 입력 받은 문장을 체크 하여 모음 뒤에 p와 모음 반복 1번 해주기, 공백 체크
# 무슨 규칙이 있는지 찾아 보기 :어디에 while 을 사용 할 지 고민
# 모음이 발견 되면, 그 모음 뒤에 2개 인덱스에 해당 하는 알파벳을 삭제, 공백인지도 확인!

white_space = " "
vowel = "aeiou"
sentence = input()
if not sentence.islower(): exit(f"{sentence} != lower")
if not 1 <= len(sentence) <= 100: exit(f"범위 벗어남 (1 <= len({sentence} <= 100)")
i = 0
result = ""
while i < len(sentence):
    result = result + sentence[i]
    if sentence[i] in vowel and white_space:
        i += 3
    else:
        i += 1

print(result)


