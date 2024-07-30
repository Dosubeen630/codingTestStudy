# 앞뒤가 같은 10진수 만들기
num = 11

while True:
    num_10 = str(num)
    num_8 = oct(num).replace("0o", "")
    num_2 = bin(num).replace("0b", "") # 진법에 따른 변수 선언

    # 앞 뒤가 같은지 확인
    if num_10 == num_10[::-1]\
        and num_8 == num_8[::-1]\
        and num_2 == num_2[::-1]:
        print(num)
        break

    num += 2  # 홀수만 탐색 하므로 2씩 늘림

