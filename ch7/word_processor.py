# https://usaco.org/index.php?page=viewproblem2&cpid=987

input_file = open('word.in', 'r')
output_file = open('word.out', 'w')

lst = input_file.readline().split()
n = int(lst[0])
k = int(lst[1])
words = input_file.readline().split()

line = ''
char_on_line = 0

for word in words:
    if char_on_line + len(word) <= k:
        line = line + word + ' '
        char_on_line = char_on_line + len(word)
    else:
        output_file.write(line[:-1] + '\n')
        line = word + ' '
        char_on_line = len(word)

output_file.write(line[:-1] + '\n')

input_file.close()
output_file.close()