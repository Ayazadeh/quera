""" 49535 """
""" Done """

n, k = map(int, input().split(' '))
lis = []
for i in range(n):
    lis.append(int(input()))

if sum(lis) >= k:
    print('YES')
else:
    print('NO')