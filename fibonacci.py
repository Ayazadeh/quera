### 17675 ###
""" Done """

n = int(input())
a, b = 0, 1
fibonacci = []
while a < n+1:
    fibonacci.append(a)
    a, b = b, b + a

for i in range(1, n + 1):
    if i in fibonacci:
        print('+', end='')
    else:
        print('-', end='')

