### 4065 ###
### Done ###

a, b, l = map(int, input().split())

a1 = 1
b1 = 0

while True:
    if a1 > b1:
        n = a1 * a + b1 * b
        b1 += 1
    elif a1 == b1:
        n = a1 * a + b1 * b
        a1 += 1
    l -= 1
    if l == 0:
        break
print(n)
