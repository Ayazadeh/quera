### 33045 ###
### Done ###

n = int(input())
counter = 0
sum = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
            sum += j

print(counter, sum)
