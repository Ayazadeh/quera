### 2755 ###
### Done ###

def solve(n, m, k, r, c):
    # print n,m,k,r,c
    if k % 2 == 1:
        print(0)
        return
    if n * m <= k:
        print(-1)
        return
    for x in range(1, n + 1):
        for y in range(1, m + 1):
            fnd = False
            for i in range(k):
                if x == r[i] and y == c[i]:
                    fnd = True
                    continue
            if not fnd:
                print(1)
                print(x, y)
                return
    return


n, m, k = map(int, input().split())
r = []
c = []
for cas in range(k):
    ri, ci = map(int, input().split())
    r.append(ri)
    c.append(ci)

solve(n, m, k, r, c)
