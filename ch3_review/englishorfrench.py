# https://dmoj.ca/problem/ccc11s1
# 대소문자 t and 대소문자 s의 개수로 영어 인지 프랑스어 인지 판별!

text_num = input()
if not text_num.isdigit():exit(f"{text_num} != digit")
text_num = int(text_num)
if not 0 < text_num < 10000: exit(f"범위 벗어남 ( 0 < N < 10000)")
t_total_count = 0
s_total_count = 0
for i in range(text_num):
    text = input()

    t_total_count = t_total_count + text.count('T') + text.count('t')
    s_total_count = s_total_count + text.count('S') + text.count('s')

if t_total_count > s_total_count :
    print("English")
elif t_total_count < s_total_count:
    print("French")
else: # t_total_count = s_total_count
    print("French")