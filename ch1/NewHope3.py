# https://dmoj.ca/problem/wc15c2j1

# We can try to describe it by repeating the word far a certain number of times in the following sentence format:
# 다음 문장 형식 으로 단어 far 를 특정 횟수 만큼 반복 하여 설명 할 수 있습니다.
# A long time ago in a galaxy far, far away...
# N 번 만큼 반복 하여, far 단어를 나머지는 그대로 두고!
# There should be a comma right after each occurrence except for the last one.
# 마지막 항목을 제외 하고 각 항목 바로 뒤에는 쉽표가 있어야 합니다.
# 'far' 단어를 반복 할 횟수인 N이 입력 되면, N번 far가 반복된 문장을 출력해준다.

far_num = input()
if not far_num.isdigit(): exit(f"{far_num} != digit")
far_num = int(far_num)
if not 1 <= far_num <= 5: exit(f"{far_num}의 범위에 벗어 남")

if far_num != 1:
    # result = "A long time ago in a galaxy" + " " + ("far," + " " * far_num) + " " + "away..."
# far 라는 단어를 입력 받은 숫자 만큼 곱하여 출력해 준다. 문제는 1일때는 쉼표 없음. 나머지의 경우 쉼표 추가 해줘야함.
# 위의 경우 에는 far 라는 단어와 단어 사이에 공백을 주고자 추가 하였 더니 앞의 far만 출력 되고 나머지는 출력 안됨.
     # result = "A long time ago in a galaxy" + " " + ("far, " * far_num) + " " + "away..."
    # 위의 경우에는 far 단어 뒤에 공백을 추가만 해줌. 입력된 수 만큼 far 단어는 출력 잘 됨. 문제는 마지막 단어에는 쉼표가 출력되면 안됨.
    count = far_num-1
    result = "A long time ago in a galaxy" + " " + ("far, " * count ) + "far" + " " + "away..."
    # 유추 해보 자면, far 단어가 한번 있을 때도 쉼표가 출력이 안되게 해야 하니 그걸 응용 해야 할듯!

    print(result)
else: # 1일 경우
    result = "A long time ago in a galaxy" + " " + "far" + " " + "away..."
    print(result)