""" 3029 """
""" Done """

x, y = map(int, input().split(' '))
x1, y1 = map(int, input().split(' '))

if x1 - x > 0:
    print('Right')
else:
    print('Left')