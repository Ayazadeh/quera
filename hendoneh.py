### 35253 ###
### Done ###

n = int(input())
weight = input().split(' ')
weight1 = []

for f in range(n):
    weight1.append(int(weight[f]))

for i in range(n):
    if max(weight1) == weight1[i]:
        print(i+1)