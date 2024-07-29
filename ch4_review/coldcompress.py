# https://dmoj.ca/problem/ccc19j3
# 당신이 휴대폰 문자에 보내는 모든 문자에 대해 요금을 청구 하는 휴대폰 요금제
# 압축 기술 - 각 기호에 대해 연속 적으로 나타 나는 횟수를 기록, 다음 기호 자체를 기록 실행 길이 인코딩
# 공식 적으로 블록은 가능한 한 긴 동일한 기호의 하위 문자열. 블록은 해당 블록의 길이와 그 뒤에 해당 블록의 기호로 압축 된 형식으로 표시 됨.
# 문자 열의 인코딩은 문자 열에 나타 나는 순서 대로 문자 열의 각 블록을 표현 하는 것임.
# 일련의 문자가 주어 지면 이를 이 형식 으로 인코딩 하는 프로 그램을 작성 해라.
# 심볼을 카운트 해서 찍어 준다. 현재 문자가 다른 심볼로 바뀌면 또 다시 카운트 해준다. 출력시 공백을 하나씩 추가 해준다.

text_num = input()
if not text_num.isdigit(): exit(f"{text_num} != digit")
text_num = int(text_num)

for i in range(text_num):
    encodings_sentence = input()
    if not 1 <= len(encodings_sentence) <= 80: exit(f" 입력 가능 범위 벗어남( 1<= {encodings_sentence} <=80)")

    previous_char = encodings_sentence[0]
    count = 0
    result = ''

    for char in encodings_sentence:
        if char == previous_char:
            count += 1

        elif char != previous_char:

            result = result + f"{count} {previous_char} "
            previous_char = char
            count = 1

    result = result + f"{count} {previous_char} "
    print(result)




























