""" 72878 """
""" Done """

t, a, b = map(int, input().split(' '))
counter_ar = 0
counter_ma = 0

while t > 0:
    t = t - 1 - a
    counter_ar += 1
    if t > 0:
        t = t - 1 - b
        counter_ma += 1

print(counter_ar, counter_ma)
