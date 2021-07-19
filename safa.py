""" 17679 """


def saf(z, f):
    for i in range(n):
        if (z[1] - 1) == i:
            if i < len(c):
                c[i] += sum(f[:m[2]])
            else:
                c.append(sum(f[:m[2]]))
            break
    return c


n, q = map(int, input().split(' '))
a, b, c, d = 0, [], [], []
for _ in range(q):
    m = list(map(int, input().split(' ')))
    if n == 1 and q == 1:
        print(0)
    if m[0] == 1:
        a += m[1]
        b.append(m[1])
    elif m[0] == 2:
        d = saf(m, b)
print(*d, sep='\n')