### 87176 ###
### Done ###

def game(number):
    a, b = str(number)
    maximum = max(a, b)
    minimum = min(a, b)
    return int(maximum) - int(minimum)


