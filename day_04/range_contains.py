with open('input.txt', 'r') as f:
    data = [line.replace('\n', '').split(',') for line in f.readlines()]


def are_ranges_contains(r1, r2):
    r1 = [int(n) for n in r1.split('-')]
    r2 = [int(n) for n in r2.split('-')]
    if r1[0] <= r2[0] <= r1[-1]:
        print(r1, r2)
        return True
    elif r2[0] <= r1[0] <= r2[-1]:
        print(r1, r2)
        return True
    else:
        return False


count = 0

for line in data:
    if are_ranges_contains(line[0], line[1]):
        count += 1

print(count)
