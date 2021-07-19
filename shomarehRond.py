""" 91713 """
""" Done """


def two_condition(s1):
    flag = False
    for k in range(len(s1) - 2):
        if s1[k] == s1[k + 1] and s1[k] == s1[k + 2] or \
                s1.count(s1[k]) >= 4:
            flag = True
    return flag


t = int(input())
result = []
for i in range(t):
    s = input()
    if s[:4] == s[:3:-1] or two_condition(s):
        result.append('Ronde!')
    else:
        result.append('Rond Nist')

print(*result, sep='\n')
