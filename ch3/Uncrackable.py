# https://dmoj.ca/problem/wc17c3j3
# You'd like to register an account on an extremely entertaining website.
# 당신은 웹사이트에 계정을 등록하려고 한다.
#  You've already selected a username, but it seems that the requirements for choosing a password are quite strict,
# 당신은 이미 유저네임은 골라두었다. 그러나, 비밀번호는 엄격한 규칙을 요구하고 있다.
# in order to completely protect your account from being hacked into.
# 당신은 당신의 계정을 해킹 당하는 것으로부터 보호하려면
# The password must be a string between and
# characters long (inclusive), such that every character is either a lowercase letter (a … z), uppercase letter (A … Z), or digit (0 … 9).
# 비밀번호는 8~12개 사이의 문자 길이로, 모든 문자는 소문자와 대문자, 숫자를 포함하고 있어야한다.
# Furthermore, it must contain at least three lowercase letters, at least two uppercase letters, and at least one digit.
# 게다가 그 비밀번호는 최소한 3개의 소문자와, 2개의 대문자를 포함 해야하며 적어도 1개의 숫자도 포함되어야한다.
# You've got a potential password in mind, a non-empty string made up of at most
#  characters, each of which is a lowercase letter, uppercase letter, or digit.
# 당신은 잠재적인 비밀번호를 마음 속에 가지고 있다. 빈 문자열이 아니면서 최소한 100개의 문자 각각 소문자와,대문자, 혹은 숫자로 이루어진
# Rather than entering the password into the site and risking rejection, you'd like to determine for yourself whether or not your password would validly satisfy all of the rules.
# 게다가 사이트에 접속하기 위해서 비밀번호는 거절의 위험, 당신은 당신의 비밀번호가 모든 조건에 만족하기를 원한다.

password = input()

# 저번 수업 시간에 배운 입력값 관련 이슈를 if not 구문과 exit로 사용하려고 했더니 밑에 문제랑 겹치는 거 같아서 패스!!

# 패스워드에 들어간 대문자,소문자, 숫자 개수를 세기 위한 변수 선언( 처음 상태는 0으로 초기화 시킨 상태)
lower = 0
upper = 0
digit = 0

for char in password:
    # 소문자가 있는지 체크하고 있으면 1개를 lower라는 변수에 더해줌.
    if char.islower():
        lower = lower + 1
    # 대문자가 있는지 체크하고 있으면 1개를 upper라는 변수에 더해줌.
    elif char.isupper():
        upper = upper + 1
    # 숫자가 있는지 체크하고 있으면 1개를 digit라는 변수에 더해줌.
    elif char.isdigit():
        digit = digit + 1
         # password 의 길이가 8보다 크고 12랑 같거나 작을때,
        if len(password) > 8 or len(password) <= 12:
            # password가 소문자가 3개인지, 대문자가 2개인지 , 숫자가 1개 포함되었는지 검사
            if password.islower() == 3 and password.isupper() == 2 and password.isdigit() == 1:
                print("Valid")
        # 숫자가 1개 없을때,
            elif password.islower() == 3 and password.isupper() == 2 and password.isdigit() == 0:
                print("Invalid")
        # 대문자가 2개가 아닐때,
            elif password.islower() == 3 and password.isupper() != 2 and password.isdigit() == 1:
                print("Invalid")
        # 소문자가 3개가 아닐때,
            elif password.islower() != 3 and password.isupper() == 2 and password.isdigit() == 1:
                print("Invalid")
        else: # password 가 8개 이하 이거나 12개보다 길이가 길때
            print("Invalid")








