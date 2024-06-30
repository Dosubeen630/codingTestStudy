Bowl_one = int(input())
Bowl_two = int(input())
Bowl_three = int(input())

# 첫번째 수와 두번째 수가 같지 않다는 가정, 남는 수는 가장 큰수에 우선 집에 넣어둠.
# (여기서 세 수 처리를 해야 할거 같은데 어떻게 해야 할지 잘 모르겠음.)
# 첫번째 입력 받은 수와 두번째 입력 받은 수 비교, 큰 수를 미들에 넣고, 작은 수는 스몰에 넣음.
if Bowl_one != Bowl_two and (Bowl_one < Bowl_two):
    large_number = Bowl_three
    middle_number = Bowl_two
    small_number = Bowl_one
else:
    large_number = Bowl_three
    middle_number = Bowl_one
    small_number = Bowl_two

# 위에서 비교한 수 중, 작은 수 인 첫번째 입력 받은 수와 마지막 남은 세번째 입력 받은 수를 비교 한다.
# 그래서 첫번째 입력 받은 수가 세번째 입력 받은 수 보다 작을 경우 가장 큰 수에는 세번째 입력 받은 수를 지정
# 가장 작은 수를 첫번째 입력 받은 값으로 지정 하여 자연히 남는 두번째 수가 중간 크기의 수가 되게 한다.

if Bowl_one != Bowl_three and (Bowl_one < Bowl_three):
    large_number = Bowl_three
    middle_number = Bowl_two
    small_number = Bowl_one

else:
    large_number = Bowl_two
    middle_number = Bowl_one
    small_number = Bowl_three


num_compare = [large_number,middle_number,small_number]

print(num_compare)
print(middle_number)

# 저의 의도는 두 번의 if 문을 거쳐서 숫자 비교를 통해서 중간 수를 찾는 다는 의도 입니다.
# 그리하여 나온 결과를 리스트에 넣어주고 그 중에 중간 숫자를 출력하라고 프린트문으로 찍어보니 답이 틀리네요.

