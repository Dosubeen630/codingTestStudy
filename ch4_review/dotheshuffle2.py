
list = "ABCDE"
limit = 100
while limit > 0:
    limit -= 1
    button = input()
    if not (len(button)== 1 and button in "1234"): exit(f"len({button}) != 1 or {button} != 1,2,3,4")

    count = input()
    if not count.isdigit() : exit(f"{count} != digit")
    count = int(count)
    if not 1 <= count <= 10: exit(f"범위 벗어남 ( 1<= {count} <= 10)")

    if button == "1":
        c = count % 5
        list = list[c] + list[(c+1)%5] + list[(c+2)%5] + list[(c+3)%5] + list[(c+4)%5]
    elif button == "2":
        c = count % 5
        list = list[-c] + list[-(-c-1)] + list[-(-c-2)] + list[-(-c-3)] + list[-(-c-4)]
    elif button == "3":
        if count % 2 == 1:
            list = list[1] + list[0] + list[2:]
    else: # button == "4"
        break

print(" ".join(list))



