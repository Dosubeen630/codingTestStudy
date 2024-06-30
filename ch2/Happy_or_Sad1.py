# 이모티콘을 포함한 문장에는 우리의 기분이 표현되어 있다.
# happy는 ":-)" , sad는 ":-(" 로 나타내는데, 그 이모티콘의 수를 세어서
# happy가 sad 보다 이모티콘의 수가 많으면 happy를 출력, happy와 sad의 수가 같으면, unsure 출력
# happy나 sad 이모티콘이 하나도 없으면 none을 출력, sad가 happy 보다 수가 더 많으면 sad를 출력하는 프로그램

mood_emoticon = input() # 내 기분 입력받음.
happy_emoticon = mood_emoticon.count(":-)") #happy 이모티콘 개수 세기
sad_emoticon = mood_emoticon.count(":-(")# sad 이모티콘 개수 세기

# happy and sad 이모티콘 개수가 같을때,
if happy_emoticon == 0 and sad_emoticon == 0:
    print("unsure")
# happy 이모티콘이 개수가 더 많을때,
elif happy_emoticon > sad_emoticon:
    print("happy")
# sad 이모티콘 개수가 더 많을때,
elif sad_emoticon > happy_emoticon:
    print("sad")
# happy and sad 이모티콘이 하나도 없을 때,
else:
    print("none")