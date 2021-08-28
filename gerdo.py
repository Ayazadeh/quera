""" 3540 """
""" Done """

n, x, y = map(int, input().split())
i = 0
while i * x <= n:
    if (n - i * x) % y == 0:
        print(i, int((n - i * x) / y))
        break
    i += 1
if not i * x <= n:
    print(-1)
