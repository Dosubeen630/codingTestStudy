# https://dmoj.ca/problem/wc17c3j3
# 매우 재미난 웹사이트에 가입 하고 싶음. 아이디는 정해둠 비밀 번호를 정해야함.
# 비밀 번호 규칙 엄격함. 비밀 번호는 문자열 이어야 하며, 긴문자 포함 8~12, 대문자, 소문자, 숫자를 포함 하여야 함.
# 소문자 3개이상, 대문자 2개 이상, 숫자 1개 이상을 포함 하여야 함.

lower_characters = "abcdefghijklmnopqrstuvwxyz"
upper_characters = lower_characters.upper()
digit_characters = "0123456789"

password = input()

lower_characters_count = 0
upper_characters_count = 0
digit_characters_count = 0

for char in password:
    if char in lower_characters:
        lower_characters_count += 1
    elif char in upper_characters:
        upper_characters_count += 1
    else: # char in digit_characters
        digit_characters_count += 1

if not 8 <= len(password) <= 12:
    print("Invalid")
elif lower_characters_count >= 3 and upper_characters_count >= 2 and digit_characters_count >= 1:
    print("valid")
else:
    print("Invalid")