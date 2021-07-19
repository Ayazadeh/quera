### 52542 ###
""" Done """

n = int(input())
group = input().split(' ')
group_list=[]
for j in range(n):
    group_list.append(int(group[j]))
   
for i in range(n):
    if 1<= group_list[i] <= 3:
        print('*'*group_list[i])
    else:
        print('*')
