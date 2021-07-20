### 49028 ###
""" Done """ 

def light(n):
    counter = 0
    status = []
    for i in range(n):
        status.append(int(input()))
    for j in range(1,n):
        if status[j] - status[j-1] !=0:
            counter += 1
    return counter

n = int(input())
print(light(n))
