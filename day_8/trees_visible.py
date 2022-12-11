with open('test_input.txt', 'r') as f:
    forest = [[[int(x), False] for x in line.replace('\n', '').split(',')[0]] for line in f.readlines()]


for x in forest:
    print(x)

visible_trees = 2**(len(forest[0])-1)
row_max = len(forest[0])

for row in forest[1:-1]:
    i = 0
    current_height = row[0][0]
    while i < row_max - 2:
        if row[i + 1][0] > current_height and not row[i + 1][1]:
            visible_trees += 1
            row[i + 1][1] = True
            current_height = row[i+1][0]
        i += 1
print(visible_trees)

for x in forest:
    print(x)

for row in forest[1:-1]:
    i = row_max - 1
    current_height = row[-1][0]
    while i > 1:
        if row[i - 1][0] > current_height and not row[i - 1][1]:
            visible_trees += 1
            row[i - 1][1] = True
            current_height = row[i - 1][0]
        i -= 1

print(visible_trees)

for x in forest:
    print(x)