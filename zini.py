### 33023 ###
### Done ### 

n, m = input().split()
n = int(n)
m = int(m)
res = [input().split() for i in range(n)]
adad = 0

for f in range(1, n - 1):
    for k in range(1, m - 1):
        if res[f][k + 1] > res[f][k] > res[f + 1][k] < res[f][k - 1] and res[f][k] > res[f - 1][k]:
            adad += 1
        elif res[f + 1][k] > res[f][k] > res[f][k + 1] > res[f][k - 1] and res[f][k] < res[f - 1][k]:
            adad += 1
print(adad)
