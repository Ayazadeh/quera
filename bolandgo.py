""" 3430 """
""" Done """

string = input()

for i in range(len(string)):
    for j in range(i):
        string = string.replace(string[j], string[i], 1)
    print(string)