### 80651 ###
### Done ###

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())
team = 0
if a1 <= b1:
    team += a1
elif b1 < a1:
    team += b1
if a2 <= b2:
    team += a2
elif b2 < a2:
    team += b2
if a3 <= b3:
    team += a3
elif b3 <= a3:
    team += b3

print(team)
