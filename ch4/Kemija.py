# https://dmoj.ca/problem/coci08c3p2
# Luka is fooling around in chemistry class again! Instead of balancing equations he is writing coded sentences on a piece of paper.
# 루카가 화학 시간에 또 장난을 치고 있어요. 그는 방정식의 균형을 맞추는 대신 종이에 코드화된 문장을 쓰고 있습니다.
#  Luka modifies every word in a sentence by adding, after each vowel (letters a, e, i, o and u), the letter p and then that same vowel again.
# 루카는 각 모음(문자 a,e,i,o,u) 뒤에 문자 p를 추가하고 동일한 모음을 다시 추가하여 문장의 모든 단어를 수정 합니다.
# For example, the word kemija becomes kepemipijapa and the word paprika becomes papapripikapa.
# 예를들어, kemija 라는 단어는 kepemipijapa 가 되고, paprika 라는 단어는 papapripikapa 가 됩니다.
# 선생님은 암호화된 문장이 적힌 루카의 논문을 가져가서 해독하고 싶어 하셨습니다.
# Write a program that decodes Luka's sentence.
# 루카의 문장을 해독하는 프로그램을 작성 하세요.
# The coded sentence will be given on a single line. The sentence consists only of lowercase letters of the English alphabet and spaces.
# 코딩 된 문장은 한 줄에 제공 됩니다. 문장은 영문 소문자와 공백 만으로 구성됩니다.
# The words will be separated by exactly one space and there will be no leading or trailing spaces. The total number of characters will be at most 100.
# 단어는 정확히 공백 하나로 구분되며 선행 또는 후행 공백이 없습니다. 총 문자수는 최대 100자 입니다.
# Output the decoded sentence on a single line.
# 디코딩된 문장을 한줄로 출력 합니다.

sentence = input()
result = ' ' # 단어 원문을 저장 하기 위한 변수
if not sentence.islower(): exit(f"{sentence} != lower")
if not len(sentence) <= 100: exit(f"{len(sentence)} <= 100")
#if not sentence.isspace(): exit(f"{sentence}에는 단어와 단어 사에에 공백이 필요 합니다.")

i = 0
while i< len(sentence):
    result = result + sentence[i]
    if sentence[i] in 'aeiou': # 단어에 모음이 포함 되어 있는 경우, (p와 모음이 한번더 붙는 방식)
        i += 3 # 다음 단어가 모음인 경우 두 자리를 건너뛴 3을 더해 주어 그 다음 단어를 저장 해줌.

    else: # 다음 단어가 모음이 아닌 경우,
        i += 1 # 바로 다음 단어를 결과값 문장인 result 에 바로 저장 해준다.

print(result)


