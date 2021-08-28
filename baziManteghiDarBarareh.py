""" 10164 """
""" Done """

row = []
for i in range(7):
    row.append(list(input()))
counter = 0
for i in range(7):
    for j in range(7):
        if i > 1 and row[i][j] == '.' and row[i-1][j] == 'o' and row[i-2][j] == 'o':
            counter += 1
        if i < 5 and row[i][j] == '.' and row[i+1][j] == 'o' and row[i+2][j] == 'o':
            counter += 1
        if j > 1 and row[i][j] == '.' and row[i][j-1] == 'o' and row[i][j-2] == 'o':
            counter += 1
        if j < 5 and row[i][j] == '.' and row[i][j+1] == 'o' and row[i][j+2] == 'o':
            counter += 1
print(counter)

""" another ansower """
# arr = []
# for i in range(7):
#     arr.append(list(input()))
# s = 0
# for i in range(7):
#     for j in range(7):
#         if arr[i][j] == ".":
#             s += (i > 1) and arr[i - 1][j] == "o" and arr[i - 2][j] == "o"
#             s += (i < 5) and arr[i + 1][j] == "o" and arr[i + 2][j] == "o"
#             s += (j > 1) and arr[i][j - 1] == "o" and arr[i][j - 2] == "o"
#             s += (j < 5) and arr[i][j + 1] == "o" and arr[i][j + 2] == "o"
# print(s)
