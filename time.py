time = int(input("Enter your second's: "))
hour = time // 3600
time = time % 3600
minute = time // 60
second = time % 60
print(hour, minute, second, sep=':')
print(f"{hour}:{minute}:{second}")
