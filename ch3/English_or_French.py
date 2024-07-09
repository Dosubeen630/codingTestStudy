# https://dmoj.ca/problem/ccc11s1
# You would like to do some experiments in natural language processing.
# 당신은 자연어 처리 과정에서 약간의 실험을 하는 것을 좋아한다.
# Natural language processing (NLP) involves using machines to recognize human languages.
# 자연어 처리 과정 (NLP)는 기계를 사용하여 사람의 언어를 알아채는 것이다.
# Your first idea is to write a program that can distinguish English text from French text.
# 당신의 첫 아이디어는 프로그램에 적으면, 영어문자 부터 프랑스문자까지 구분하는 것이다.
# After some analysis, you have concluded that a very reasonable way of distinguishing these two languages is to compare the occurrences of the letters t and T to the occurrences of the letters s and S.
# 분석 후에 당신은 매우 합리적인 방법을 결론지었다. 이 두 언어들은 문자들을 비교할때, t and T, s and S 같은 경우에 발생시킨다.
# if the given text has more t and T characters than s and S characters, we will say that it is (probably) English text;
# 자세하게 이야기 해보자면, 만약 대문자 T와 소문자 t 가 대문자 S와 소문자 s 보다 많이 주어진다면 그것은 아마도 영어문장 일것이다.
# if the given text has more s and S characters than t and T characters, we will say that it is (probably) French text;
# 만약에 대문자 S와 소문자 s 가 대문자 T와 소문자 t 보다 더 많이 주어진다면 우리는 그 문장은 프랑스 문장이라고 말 할 수 있을 것이다.
# if the number of t and T characters is the same as the number of s and S characters, we will say that it is (probably) French text.
# 만약에 대문자 S와 소문자 s 와 대문자 T와 소문자 t 가 같은 수이라면 우리는 그 문장은 아마도 프랑스 문장이라고 말 할 수 있을 것이다.
# The input will contain the number N ( 0 < N < 10000) followed by N lines of text, where each line has at least one character and no more than 100 characters.
# 입력사항 구체적으로 : 첫번째에는 정확한 수(N)가 입력 될 것이다. N은 문장의 수를 의미한다. 그리고 각 문장은 적어도 1이상의 수와 100이하의 단어를 가지고 있어야한다.
# Your output will be one line. This line will either consist of the word English (indicating the text is probably English) or French (indicating the text is probably French).
# 출력사항 : 당신은 한줄을 출력해야한다. 이 줄에는 'English' 혹은 'French'라고 말이다.

line = input()
if not line.isdigit():
    exit("입력 형식을 잘못 되었습니다.")
line = int(line)
if not 0 < line < 10000:
    exit(" 입력한 단어의 수가 범위를 벗어 납니다.")

for n in range(line):
    # 입력된 값이 0이 아니면, 텍스트를 입력 받은 라인 수 만큼 입력 받는다.
    if line != 0:
        text = input()
    # 입력된 값이 0이면 아무 것도 입력 받지 않는다.
    else:
        pass
# 소문자 t의 개수를 세어서 저장할 변수 선언
t_num1 = text.count('t')
# 대문자 T의 개수를 세어서 저장할 변수 선언
t_num2 = text.count('T')
# 소문자 s의 개수를 세어서 저장할 변수 선언
s_num1 = text.count('s')
# 대문자 S의 개수를 세어서 저장할 변수 선언
s_num2 = text.count('S')
# 대문자, 소문자 T의 개수를 합한 값을 저장할 변수
t_sum = t_num1 + t_num2
# 대문자, 소문자 S의 개수를 합한 값을 저장할 변수
s_sum = s_num1 + s_num2

# 대소문자 T의 합과 대소문자 S의 합을 비교하여 t_sum이 더 크면,
if t_sum > s_sum:
    print("English")
# 대소문자 S의 합이 더 크면,
elif t_sum < s_sum:
    print("French")
else: # t_sum 과 s_sum의 수가 같을때
    print("French")
