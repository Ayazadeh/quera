""" 3411 """
""" Done by hamid """

import math


def findTrailingZeros(z):
    count = 0
    while z >= 5:
        z //= 5
        count += z
    return count


n = int(input())
a = math.factorial(n) // 10 ** findTrailingZeros(n)
print(a % 10)
