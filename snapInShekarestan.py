""" 8938 """
""" Done """

n, m = map(int, input().split(' '))
list1 = []
result = 0
for i in range(n):
    list1.append(list(map(int, input().split(' '))))

for i in range(m):
    x, y = map(int, input().split(' '))
    result += list1[x - 1][y - 1]
print(result)
