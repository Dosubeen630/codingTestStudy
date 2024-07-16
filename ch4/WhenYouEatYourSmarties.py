# https://dmoj.ca/problem/ecoo15r1p1
# When I eat my Smarties I always eat the red ones last.
# 나는 스마티를 먹을때 항상 빨간 것을 제일 나중에 먹는다.
# I separate them into their color groups and I start by eating the orange ones, then blue, green, yellow, pink, violet, brown and finally red.
# 나는 그것 들을 색상 그룹 으로 나누고 오렌지 색 부터 시작 하여 파란색, 녹색, 노란색, 분홍색, 보라색, 갈색, 마지막 으로 빨간색을 먹습 니다.
# The red ones are the best, so I eat them slowly one at a time. The other colors I eat quickly by the handful (my hand can hold a maximum of 7 Smarties).
# 빨간색이 제일 맛있어서 천천히 하나씩 먹습니다. 다른 색상은 한 줌씩 빠르게 먹습니다.( 내 손에 최대 7개의 스마티를 담을 수 있습니다.)
# I always finish all the Smarties of one color before I move on to the next, so sometimes the last handful of a color isn't a full one.
# 나는 항상 한 색상의 스마티들을 모두 마친 후 다음 색상으로 넘어 가기 때문에 마지막 색상이 전체 색상이 아닐 때도 있습니다.
# But wait, there's more! I have turned my Smartie-eating into a science.
# 하지만 더 많은 것이 있습니다. 나는 스마티 먹는 것을 과학으로 만들었습니다.
# I know it always takes me exactly 13 seconds to eat a handful of non-red Smarties and I adjust my chewing rate so that I always take 13 seconds even if my hand is not completely full.
# 빨간 색이 아닌 스마티 한 줌을 먹는데는 항상 정확히 13초가 걸린다는 것을 알고 있으며, 손에 가득 차지 않더라도 항상 13초가 걸리도록 씹는 속도를 조정 합니다.
# When I eat the red Smarties I like to take my time, so it takes me exactly 16 seconds to eat each one.
# 빨간 스마티는 천천히 먹는 걸 좋아해서 한 개 먹는데 정확히 16초가 걸린다.
# I have a big box of Smarties. After I've finished sorting the colors, how long will it take me to eat them?
# 나는 스마티들의 큰 상자를 가지고 있습니다. 색깔별로 분류 한 뒤, 먹는데 까지 얼마나 걸리나요?
# The input will contain 10 test cases. Each test case will start with N lines (50 <= N <= 200), where each line holds the color of a single Smartie in lower case.
# 입력 에는 10개의 테스트 케이스가 포함 됩니다. 각 테스트 케이스 에는 N라인 으로 시작하며, 각 라인은 단일 스마티의 색상을 소문자로 유지 합니다.
# Then the last line will read end of box meaning there are no more Smarties in the box for that test case.
# 그런 다음 마지막 줄에는 해당 테스트 사례의 상자에 더이상 스마티들이 없음을 의미 하는 상자 끝이 표시 됩니다.
# Your program should output a single line for each test case indicating how long (in seconds) it will take me to eat the entire box according to the rules given above.
# 귀하의 프로 그램은 위에 주어진 규칙에 따라 상자 전체를 먹는데 걸리는 시간(초)을 나타 내는 각 테스트 사례에 대해 한 줄을 출력해야 합니다.
# Note that the sample input below only contains 1 test case, but the real data files will contain 10.
# 아래 샘플 입력 에는 테스트 사례가 1개만 포함 되어 있지만 실제 데이터 파일 에는 10개가 포함 됩니다.

# 오렌지 -> 파란 -> 녹색 -> 노란 -> 분홍 -> 보라 -> 갈색 -> 빨강
# 빨강 16초, 나머지 색은 13초 먹는데 걸림 /한손에 최대 7개 쥘수 있음. 소문자로! 데이터 파일에는 10개씩!

for datafile in range(10):
    orange_num = 0
    blue_num = 0
    green_num = 0
    yellow_num = 0
    pink_num = 0
    violet_num = 0
    brown_num = 0
    red_num = 0

   # finish = False

   # while not finish:
    while True:
        smarties_color = input()
        if not smarties_color.islower(): exit(f"{smarties_color} != lower")
       # if not 50 <= len(smarties_color) <= 200: exit(f" 50 <= {smarties_color} <= 200")

        if smarties_color == 'orange':
            orange_num += 1
        elif smarties_color == 'blue':
            blue_num += 1
        elif smarties_color == 'green':
            green_num += 1
        elif smarties_color == 'yellow':
            yellow_num += 1
        elif smarties_color == 'pink':
            pink_num += 1
        elif smarties_color == 'violet':
            violet_num += 1
        elif smarties_color == 'brown':
            brown_num += 1
        elif smarties_color == 'red':
            red_num += 1
       # elif smarties_color == 'end of box':
         #   finish = True
        else:
            break

    # 나머지 연산자 처리를 모를 경우 나머지는 최대 0-6까지 나오기 때문에, 한 손에 최대 7개 쥘 수 있는데
    # 8개 일 경우나, 13개 일 경우 결국에는 똑같이 버림을 하면 올바른 먹는 시간을 구할 수가 없음.
    # 6을 더해 주는 것은 약간 올림을 해 줄수 있게 하기 위한 치트키 같아 보임. (저자의 답안 분석 결과)
    handfuls = ((orange_num +6)// 7 + (blue_num + 6)// 7 +
                (green_num+ 6) // 7 + (yellow_num+6) //7+
                ( pink_num+6) // 7+ (violet_num +6)// 7+
                (brown_num+ 6) // 7 )
    print(handfuls*13 + red_num * 16) # 빨강은 너무 좋아 해서 한개씩 먹고 시간은 16초 걸림.
    # 나머지는 한 줌에 먹고 13초 라고 문제 에서 말했음. 그래서 한 줌은 최대 7개이니 7개라고 가정 후 한 줌당 13초로 계산해 줌.
    # 총 먹는 시간을 구하기 위하여 그 둘을 더해 줌.

    # 만약 if 문으로 이걸 구현 해 본다면?
    # - 스마티 갯수가 빨강이 아닌 다른 색깔이 8개에서 13개의 경우 올림을 구현 해 주려면?
    # 스마티 빨강이 아닌 다른 색의 8-13 사이 개수 구간에 더하기 1(+13초)을 해서 올림 처럼 만들어 보면 어떨까?
    handfuls =((orange_num // 7) +( blue_num // 7) +
                (green_num // 7) + (yellow_num // 7) +
               (pink_num // 7) + (violet_num // 7) +
               (brown_num // 7))
    # 시도 1: 저자와 같이 한 줌에 빨강을 제외 한 다른 색상의 스마티들을 다 묶어서 한번에 처리 하면 좋을거 같은데 방법 모르겠음.













# red 8. 16*8 128

# brown 9. 13*2 = 26
# violet 4. 13*1 13
# blue 6. 13*1 13
# pink 7. 13*1 13
# yellow 4. 13*1 13
# orange 8. 13*2 26
# green 4. 13*1 13
