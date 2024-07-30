inch_height = 170 / 2.54
feet = inch_height // 12
print(feet)

inch = inch_height % 12
print(inch)

centemeter = 90
inch = 2.54
transfer = centemeter / inch
print(transfer)
transfer2 = centemeter // inch
print(transfer2)

a = 5
b = 3
x = 7
y = x**2 + (b/a)*x + (b/(2*a))**2
print(y)

a= 5
b= 3
for x in range(10, 101, 10):
    y = x**2 + (b/a)*x + (b/(2*a)**2)
    print(x, "--> ", y)