""" 6374 """
""" Done """

# s = int(input(), 16) + 1
# print(hex(s)[2:].upper())

k = lambda x: hex(x)[2:].upper()
print(k((int(input(), 16) + 1)))
