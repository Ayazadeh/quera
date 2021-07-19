""" 6580 """
""" Done """

x, y = map(int, input().split(' '))
r = int(input())
dx, dy = map(int, input().split(' '))

if x <= dx <= x+r and y-r <= dy <= y:
    print('Mahdi')
else:
    print('Parsa')