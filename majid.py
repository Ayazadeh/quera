""" 9109 """
""" Done """

a = int(input())
list1 = list(map(int, input().split(' ')))
min1 = 100
list2 = []
for i in range(1, 102):
    list2.append(0)
for i in range(a):
    list2[list1[i]] += 1
sumation = 0
for i in range(len(list2)):
    if list2[i] != 0 and list2[i] < min1:
        min1 = list2[i]
        sumation = i
print(sumation)



