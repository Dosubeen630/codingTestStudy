# 수열의 사칙 연산

# 완성된 식을 계산한 결과가 원래 수를 거꾸로 나열한 숫자
# 351  -> 3 * 51 = 153 , 621 -> 6 * 21 = 126 , 886 -> 8 * 86 = 688

import re

op = ["*" , ""]
for i in range(1000, 10000):
    c = str(i)
    for j in range(0, len(op)):
        for k in range(0, len(op)):
            for l in range(0,len(op)):
                val = c[3] + op[j] + c[2] + op[k] + c[1] + op[1] + c [0]