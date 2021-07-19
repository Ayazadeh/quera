""" 17902 """
""" Done """

k = int(input())
ramz = input()
result = []
charkh = []
for i in range(k):
    argham = input()
    charkh.append(argham)
for i in range(k):
    index = charkh[i].index(ramz[i])
    if index <= 4:
        result.append(index)
    else:
        result.append(9-index)
print(sum(result))
