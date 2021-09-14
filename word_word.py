### 108665 ###
### Done ###

string = input()

l = ['a', 'u', 'i', 'o', 'e']
count = 1
for i in string:
    if i in l:
        count = count * 2

print(count)
