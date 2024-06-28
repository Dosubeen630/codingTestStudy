apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

final_scoreA = apple_three * 3 + apple_two * 2 + apple_one * 1
final_scoreB = banana_three * 3 + banana_two * 2 + banana_one * 1

if final_scoreA > final_scoreB:
    print('A')
elif final_scoreB > final_scoreA:
    print('B')
else:
    print('T')