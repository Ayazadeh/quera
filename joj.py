### 72875 ###
### Done ###

n = int(input())
arr = list(map(int, input().split(' ')))

if len(arr) == n:
    flag = False
    for i in range(1, n - 1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            flag = True
    if flag:
        print('Ey baba :(')
    else:
        print('Bah Bah! Ajab jooji!')
