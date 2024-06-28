# 문자열 연산자
a ='hello' + 'there'
print(a)
b = 'hello ' + 'there'
print(b)
c = '' * 3
print(c)

'hello'.upper()
print('hello'.upper())

'    abd'.strip()
print('    abd'.strip())

'    abc    '.strip()
print('    abc    '.strip())

'abc'.strip()
print('abc'.strip())

'abc'.strip('a')
print('abc'.strip('a'))

'abca'.strip('a')
print('abca'.strip('a'))

'abca'.strip('ac')
print('abca'.strip('ac'))

#문자열 호출 함수 counter

z = 'abc' .count('a')
print(z)

y = 'abc' .count('q')
print(y)

x = 'aaabcaa' . count('a')
print(x)

h = 'aaabcaa' . count('ab')
print(h)

#인자가 겹쳐서 나타나는 경우 첫번째로 발견 된 것만 카운트됨.
k = 'ababa' . count('aba')
print(k)

r = "this is a string with a few words" .count(' ')
print(r)

(5).bit_length()
print((5).bit_length())

s= (100).bit_length()
print(s)

j = (999999).bit_length()
print(j)

# 할당문
dollars = 250
print(dollars)

dollars + 10
print(dollars)

purchase_price1 = 58
purchase_price2 = 9
c = purchase_price1 + purchase_price2
print(c)