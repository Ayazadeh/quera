""" 2636 """
""" Done """

mohreh = [1, 1, 2, 2, 2, 8]
mohreh1 = list(map(int, input().split(' ')))
for i in range(6):
    print(mohreh[i] - mohreh1[i], end=' ')