""" 10327 """
""" Done """

n, code_t = input().split(' ')
result = []
for i in range(int(n)):
    codes = input()
    result.append('Yes') if sorted(set(codes)) == sorted(set(code_t))\
        else result.append('No')
print(*result, sep='\n')
