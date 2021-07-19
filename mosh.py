""" 26962 """

x1, x2 = map(int, input().split(' '))
if x1 == x2:
    print('Saal Noo Mobarak!')
c = (x2 - x1)
d = (x1 - x2)
if c > 0:
    print('R' * c)
elif c < 0:
    print('L' * d)