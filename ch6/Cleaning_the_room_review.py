def checkNumber(str, min, max):
    num = str.strip()
    if not num.isdigit(): exit(f"{num} is not num")
    num = int(num)
    if not min <= num <= max: exit(f"{min} <= {num} <= {max}")
    return num

boxCount = checkNumber(input(), 1 ,100)
boxSet = []
for i in range(boxCount):
    box = input().strip().split(" ")
    fCount = checkNumber(box[0], 0, 100)
    box = [checkNumber(x,1, 10000) for x in box[1:]]
    if box != sorted(box):
        print("NO")
        exit()
    boxSet.append([box[0], box[-1]])
boxSet.sort(key= lambda x: x[0])
for i in range(1, boxCount):
    if boxSet[i][0] < boxSet[i-1][1]:
        print("NO")
        exit()
print("YES")