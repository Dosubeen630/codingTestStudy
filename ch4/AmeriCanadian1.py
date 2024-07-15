# https://dmoj.ca/problem/ccc02j2
# Americans spell differently from Canadians. Americans write neighbor and color while Canadians write neighbour and colour.
# 미국인은 캐나다인과 철자가 다릅니다. 미국인은 neighbor 과 color 를 쓰고 캐나다인은 neighbour 과 colour 을 씁니다.
#  Write a program to help Americans translate to Canadian.
# 미국인이 캐나다인 으로 번역 하는데 도움이 되는 프로 그램을 작성 하세요.
# Your program should interact with the user in the following way.
# 프로그램은 다음과 같은 방식 으로 사용자과 상호 작용 해야 합니다.
# The user should type a word (not to exceed 64 letters) and if the word appears to use American spelling, the program should echo the Canadian spelling for the same word.
# 사용자는 단어 (64자를 초과 하지 않음)를 입력 해야 하며 해당 단어가 미국식 철자를 사용 하는 것으로 나타 나면 프로 그램은 동일한 단어에 대해 캐나다 철자를 반영 해야 합니다.
#  If the word does not appear to use American spelling, it should be output without change. When the user types quit! the program should terminate.
# 단어가 미국식 철자를 사용 하지 않는 것으로 나타 나면 변경 없이 출력 되어야 합니다. 사용자가 종료를 입력하면! 프로 그램이 종료 되어야 합니다.
# The rules for detecting American spelling are quite naive: If the word has more than four letters and has a suffix consisting of a consonant followed by or, you may assume it is an American spelling, and that the equivalent Canadian spelling replaces the or by our.
# 미국식 철자를 감지하는 규칙은 매우 간단합니다. 단어에 4개 이상의 문자가 있고 자음과 or로 구성된 접미사가 있는 경우 미국식 철자이고 이에 상응하는 캐나다 철자가  or을 our로 대체한다고 가정 할 수 있습니다.
# Note: you should treat the letter y as a vowel.
# 참고 :  문자 y를 모음으로 처리해야 합니다.

finish = False

while not finish:
    words = input()
    if words.isdigit(): exit(f"{words}의 입력 형식은 문자 입니다.")
    if not len(words) <= 64: exit(f"{words}의 범위는 64개 이하 여야 합니다.")

    if len(words) > 4 and not (words[-3] in 'aeiouy') and words[-2:] == 'or':
        print(words[:-2] + 'our')
    elif words == 'quit!':
        finish = True
    else: # 단어 글자 수가 4개 이상이 아니면 단어 변형 안함.
        print(words)





