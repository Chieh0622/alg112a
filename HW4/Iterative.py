# x^2 - 3x + 1 = 0

f1 = lambda x: 3 - 1/x
f2 = lambda x: (x - 1)**2
f3 = lambda x: (x**2 + 1)/3

x1 = x2 = x3 = 1

for i in range(20):
    x1, x2, x3 = f1(x1), f2(x2), f3(x3)
    print('x1:', x1, 'x2', x2, 'x3', x3)