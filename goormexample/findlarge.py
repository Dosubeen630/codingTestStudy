a,b = input().split()

def calculate_expression(expression):
    return eval(expression)

result_a = calculate_expression(a)
result_b = calculate_expression(b)

print(max(result_a, result_b))

#입력 받기

#첫 번째 줄에서 수식 a와 b를 입력 받습니다.
#input().split()을 사용하여 공백을 기준으로 두 수식을 나눕니다.
#수식 계산

#calculate_expression 함수는 eval 함수를 사용하여 주어진 수식을 계산합니다.
#eval 함수는 문자열로 된 수식을 실제 수식으로 계산해주는 함수입니다.
#더 큰 값 출력

#두 수식의 결과를 비교하여 더 큰 값을 출력합니다.