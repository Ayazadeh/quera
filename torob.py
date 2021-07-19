### 62451 ###
""" Done """

x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())

if x2 > x1 and v2 > v1 or x1>x2 and v1>v2:
    print('BORO BORO')
elif v1 == v2:
    print('WAIT WAIT')
elif x2>x1 and v1>v2 or x1>x2 and v2>v1:
    print('SEE YOU')