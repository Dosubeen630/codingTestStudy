# 문제 주소: https://dmoj.ca/problem/coci18c3p1
# Magnus lost a game of chess to Kile so he found comfort in competitive programming.
# 마그너스는 체스게임에서 카일에게 졌고, 그래서 그는 경쟁적인 프로그램에 어울리는 것을 찾았다.
# Very soon, he heard of the iconic COCI competition and decided to try his luck there.
# 곧, 그는 상징적인 COCI 시합에 대하여 들었고, 그는 그의 운을 그곳에서 시도해보기로 결장했다.
# He wrote a mail to Kile: "Dear Kile, please, prepare me for COCI. Magnus".
# 그는 카일에게 메일을 보냈다. 카일에게 나랑 COCI를 제발 같이 준비해줘. 마그너스가
# Kile replied: "You want to participate in COCI? All right, here's your warm-up task.
# 카일이 보낸 답장에는: 네가 나랑 COCI에 함께 참여 하기를 원한다고? 좋아 그럼 여기 내가 너에게 몸풀기 미션을 줄게.
# A series of four consecutive letters of some word that make up the subword HONI (Croatian acronym for COCI) is called the HONI-block.
# 4개의 연속적인 단어종류가 있어, 몇 단어는 하위단어로 HONI라고(크로아티아어의 두문자어), 그것은 HONI-block이라고 불리워진다.
# I will send you the word of length and you will throw out as many letters as you want (it might be none as well) so that in the end there are as many HONI-blocks as possible in the word. Kile".
# 나는 너에게 N 이라는 단어의 길이 그리고, 너는 많은 단어들을 네가 원하는 만큼 버릴 것이고,(그것을 아무것도 없게해도 된다.)
# 그래서 마지막으로 거기에는 가능한한 많은 HONI-blocks이 있게 해줘. 카일이
# Magnus was very worried and asked you, COCI competitive scene, for help.
# 마그너스는 매우 걱정되어 당신에게 물어봅니다. COCI 시합의 장면을 도움을 바라며.
# Help him determine the maximum number of HONI-blocks he can get in the final word.
# HONI-blocks의 가장 많은 수를 측정하여 그가 마지막 단어를 가질수 있게 그를 도와주자.
# 입력창 The first line contains a word of length N( 1<= N <= 100,000),consisting of uppercase letters of the English alphabet.
# 첫번째 줄에는 N이라는 단어의 길이를 포함하고 있어야하며, 영어 대문자 알파벳을 포함하고 있어야한다.
# In the first and only line, print out the required number of HONI-blocks.
# 출력창에는 호니블럭의 수가 나와야한다.

# 단어를 입력받음.
words = input()
# 호니블록즈에 호니 라는 단어가 나온 수를 저장할 용도로 만든 변수 선언. 0으로 초기화 해줌.
honi_blocks = 0

if not words.isalpha():
    exit("입력값이 잘못되었습니다. 알파벳 문자를 입력해주세요.")
if not len(words) <= 100000:
    exit("입력한 문자의 길이가 너무 큽니다.")
if not words.isupper():
    exit("입력값이 대문자가 아닙니다.")
prev = None
# 입력받은 단어 중에서 반복문을 돌려라
for char in words:
    print(char)
    if char == 'H' and (prev is None or prev == 'I'):
        prev = 'H'
    elif char == 'O' and prev == 'H':
        prev = 'O'
    elif char == 'N' and prev == 'O':
        prev = 'N'
    elif char == 'I' and prev == 'N':
        prev = 'I'

        honi_blocks = honi_blocks + 1
        print(honi_blocks)
    else:
        pass

print(honi_blocks)




