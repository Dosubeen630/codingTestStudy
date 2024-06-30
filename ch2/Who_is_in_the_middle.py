Bowl_one = int(input())
Bowl_two = int(input())
Bowl_three = int(input())


if Bowl_one < Bowl_two:
    large_number = Bowl_two
    middle_number = Bowl_one
    small_number = Bowl_three

elif Bowl_two < Bowl_three:
    large_number = Bowl_three
    middle_number = Bowl_two
    small_number = Bowl_one

    num_compare = [large_number,middle_number,small_number]

print(middle_number)