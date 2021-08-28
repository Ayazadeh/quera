""" 17678 """
""" Done """


# def parse_input(line):
#     day_part, time_part, name_part = line[1:-1].split('|')
#     return {
#         'day': int(day_part.partition(":")[-1].strip()),
#         'time': time_part.partition(":")[-1].strip(),
#         'name': name_part.partition(":")[-1].strip()
#     }
def parse_input(line):
    return {
        'day': int(line[2]),
        'name': line[8]
    }


def names_in_every_day(i):
    inday_participants_filter = filter(lambda s: s['day'] == i, data)
    inday_participants = list(map(lambda s: s['name'], inday_participants_filter))
    return set(inday_participants)


def last(i):
    counter = 0
    for j in names_in_every_day(i):
        if j not in names_in_every_day(i + 1):
            counter += 1
    return counter


n, d = map(int, input().split())
data = []
for _ in range(n):
    line = input().split(' ')
    data.append(parse_input(line))

participants = set()
for _ in range(1, d + 1):
    new_participants_filter = filter(lambda d: d['day'] == _ and d['name'] not in participants, data)
    new_participants = set(map(lambda d: d['name'], new_participants_filter))
    participants = participants.union(new_participants)
    print(len(names_in_every_day(_)), len(new_participants), last(_))
