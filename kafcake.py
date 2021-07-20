""" 51866 """
""" Done """

n, k = map(int, input().split(' '))
m = list(map(int, input().split(' ')))
if k == 1:
    print(max(m))
elif k >= 3:
    print(min(m))
elif k == 2:
    print(min([m[0], m[-1]]))
