# 6가지의 수를 입력 받는다.
# 첫번째 라인 수는 애플 팀의 3점슛 성공횟수, 두번째 라인 수는 2점슛 성공횟수, 세번째 라인 수는 1점 자유투 성공횟수를 의미한다.
# 네번째 라인의 수는 바나나팀의 3점슛 성공횟수, 다섯번째 라인 수는 2점슛 성공횟수, 여섯번째 라인의 수는 1점 자유투 성공 횟수를 의미한다.
# 애플 팀의 총 점수와 바나나팀의 총 점수를 비교하여, 점수가 큰 팀을 출력해준다.

# 사과 팀의 3점슛,2점슛, 1점슛 성공 횟수 입력받음.
apple_three = int(input())
apple_two = int(input())
apple_one = int(input())
# 바나나 팀의 3점슛, 2점슛, 1점슛 성공 횟수 입력받음.
banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

# 사과팀의 최종 점수 계산
final_scoreA = apple_three * 3 + apple_two * 2 + apple_one * 1
# 바나나팀의 최종 점수 계산
final_scoreB = banana_three * 3 + banana_two * 2 + banana_one * 1
# 사과 팀의 총 점수가 바나나팀의 총 점수 보다 높을때,
if final_scoreA > final_scoreB:
    print('A')
# 바나나팀의 총 점수가 사과팀의 총 점수보다 높을때,
elif final_scoreB > final_scoreA:
    print('B')
# 두 팀의 점수가 동일 할때,
else:
    print('T')