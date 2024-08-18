# https://dmoj.ca/problem/ccc02j2
# 자음과 모음 뒤에 or -> our 변경. y는 모음 으로 취급.
# kemija 와 비슷 하게 해결해 보면 어떨까?  종료어 quit! 나오면 프로 그램 종료
# 단어에 4개 이상의 문자가 있고, 자음과 or로 구성된 접미사가 있는 경우 미국식 철자 이고, 위의 규칙을 적용 가능. 저 조건에 해당 되지 않으면 원래 단어 그대로 출력 해야함.
import re

VOWEL = "aeiouy"
isStop = False
AMERICAN = "or"
CANADIAN = "our"
CHANGE = " "
CONSONANT = "bcdfghjklmnpqrstvwxyz"
while isStop:

    word = input()

    if len(word) >= 4 and not VOWEL + AMERICAN in word:
        CHANGE = word + CANADIAN
        print(CHANGE)
    elif len(word) < 4 and not VOWEL + AMERICAN in word:
        print(word)

    elif word == "quit!":
        isStop = True
        break



word = input()
for c in CONSONANT:
    word = word.replace(f"{AMERICAN}",CANADIAN)
print(re.sub(r'(CONSONNANT + [or])\1', r'([our])\1'), word)

