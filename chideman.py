""" 2534 """
""" Done """

list1 = [0] * 10001
rate, sum1 = 0, 0
n = int(input())
for i in range(n):
    list1[i] = int(input())
for j in range(n):
    rate += list1[j]
rate = rate // n
print(rate)
for k in range(n):
    sum1 += abs(list1[k] - rate)
sum1 = sum1 // 2
print(sum1)