### 3409 ###
### Done ###

n = int(input())

mul = []
for i in range(n):
    raw = []
    for j in range(1, n + 1):
        raw.append((i + 1) * j)
    mul.append(raw)
    print(' '.join(map(str, mul[i])))
