# https://dmoj.ca/problem/coci13c3p1
# One day, little Mirko came across a funny looking machine!
# 어느날, 작은 마르코는 우연히 재미 있는 기계를 찾아 냈습니다.
# It consisted of a very very large screen and a single button.
# 그것은 매우 큰 화면과 하나의 버튼으로 구성되었습니다.
# When he found the machine, the screen displayed only the letter A.
# 그가 기계를 찾았을때 화면에는 문자 A만 표시 되었습니다.
# After he pressed the button, the letter changed to B.
# 버튼을 누르면 문자가 B로 바뀌었습니다.
# The next few times he pressed the button, the word transformed from B to BA, then to BAB, then to BABBA.
# 다음에 그가 버튼을 몇번 눌렀을때, 단어는 B에서 BA로, 그 다음에는 BAB로, 그 다음에는 BABBA로 바뀌었습니다.
# When he saw this, Mirko realized that the machine alters the word in a way that all the letters B get transformed to BA and all the letters A get transformed to B.
# 이것을 보았을때 마르코는 기계가 모든 문자 B를 BA로 변환하고 모든 문자 A를 B로 변환하는 방식으로 단어를 변경한다는 것을 깨달았습니다.
# Amused by the machine, Mirko asked you a very difficult question! After K times of pressing the button, how much letters A and how much letters B will be displayed on the screen?
# 기계를 보며 즐거워하는 마르코가 당신에게 매우 어려운 질문을 했습니다. K번 이루 버튼을 여러번 누르면 화면에 A라는 글자와 B라는 글자가 몇 번이나 나타날까요?
# The first line of input contains the integer K ( 1<= K <= 45), the number of times Mirko pressed the button.
# 입력의 첫번째 줄에는 마르코가 버튼을 누른 횟수인 정수 K가 포함됩니다.
# The first and only line of output must contain two space-separated integers, the number of letters A and the number of letters B.
# 출력의 첫번재 이자 유일한 줄에는 공백으로 구분된 두개의 정수, 즉 문자수 A와 문자수 B가 포함 되어야 합니다.
# In test data worth 20% of total points, K will be less or equal to 10.
# 총점의 20%에 해당하는 테스트 데이터에서 K는 10보다 작거나 같습니다.

# 도메인 분석 : 규칙- 문자 A -> B , B -> BA로 바뀜. 변화의 소지가 있음. (유지보수 쉽게!)
# 원하는 것은? 버튼을 누른 횟수만큼 A and B가 화면에 나타난 횟수? 여기서 돈이 되는 것? 무엇 일까?  생각해보기
# 총 포인트의 테스트 데이터 20% K는 10보다 작거나 같을 것이다?? -> 총 점수 중 20%의 버튼을 누른 횟수인 K가 10보다 작거나 같은 경우이다?

pressed_button = input()
if not pressed_button.isdigit():
    exit("f{pressed_button}" "입력 값 형태가 잘못 되었습니다.""숫자로 입력해주세요.")
pressed_button = int(pressed_button)
if not 1 <= pressed_button <= 45:
    exit("입력값의 범위가 큽니다.(1<=pressed_button<=45)")

a = 1
b = 0

# 버튼을 누르면 그 때부터 A와 B가 카운팅 되어 저장됨. A -> B, B -> BA / 이전 A는 B, B는 BA로 치환됨
# 다음번 A의 경우 이전 B, B의 경우 이전 A와 이전 B의 합
for i in range(pressed_button):
    prev_a = a
    prev_b = b
    a = prev_b
    b = prev_a + prev_b

print(a,b)





