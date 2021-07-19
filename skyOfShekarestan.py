""" 6082 """
""" Done """

n, m = map(int, input().split(' '))
star = 0
for i in range(n):
    f = input()
    star += f.count('*')
print(star)
