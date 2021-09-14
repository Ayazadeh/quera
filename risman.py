### 83360 ###
### Done ###

import re

str1 = input()
str2 = input()

if re.search(str1, str2):
    print(1)
else:
    print(0)