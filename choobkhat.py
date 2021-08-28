""" 80645 """
""" Done """

n = int(input())
m = int(input())
a = int(input())
b = int(input())
k = 0

if min(n, m) >= max(a, b):
    k = min(n, m) / max(a, b)
    if k > (min(n, m) // max(a, b)):
        k += 1
    print(int(k))