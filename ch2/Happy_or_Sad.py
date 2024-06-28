def solution(mood_emoticon):
    happy_emoticon = mood_emoticon.count(":-)")
    sad_emoticon = mood_emoticon.count(":-(")

   # print(happy_emoticon, sad_emoticon)

    if happy_emoticon == 0 and sad_emoticon == 0:
        return "none"
    elif happy_emoticon > sad_emoticon:
        return "happy"
    elif sad_emoticon > happy_emoticon:
        return "sad"
    else:
        return "unsure"


mood_emoticon = input()
# mood_emoticon = "How are you :-) doing :-( today :-) :-(?"
#mood_emoticon = ":)"
result = solution(mood_emoticon)
print(result)
