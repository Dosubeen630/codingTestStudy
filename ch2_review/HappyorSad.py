# https://dmoj.ca/problem/ccc15j2
# 3 가지의 문자로 나타내는 기분 이모티콘: 해피 - :-) ,새드 - :-(
# 해피 새드 포함 하고 있지 얺으면 none, 두 개가 수가 동일 unsure, 해피가 많으면 해피, 새드가 많으면 새드

text = input()
if text.isdigit(): exit(f"{text} != digit")
if not 1 < len(text) < 255: exit(f"{text}의 범위 벗어남")

happy = ":-)"
sad = ":-("
mood = None

if text.count(happy) == 0:
    mood = "none"
elif text.count(happy) > text.count(sad):
    mood = "happy"
elif text.count(happy) < text.count(sad):
    mood = "sad"
else: # text.count(happy) = text.count(sad)
    mood = "unsure"

print(mood)