ship = [
    ['N', 'C', 'R', 'T', 'M', 'Z', 'P'],
    ['D', 'N', 'T', 'S', 'B', 'Z'],
    ['M', 'H', 'Q', 'R', 'F', 'C', 'T', 'G'],
    ['G', 'R', 'Z'],
    ['Z', 'N', 'R', 'H'],
    ['F', 'H', 'S', 'W', 'P', 'Z', 'L', 'D'],
    ['W', 'D', 'Z', 'R', 'C', 'G', 'M'],
    ['S', 'J', 'F', 'L', 'H', 'W', 'Z', 'Q'],
    ['S', 'Q', 'P', 'W', 'N']
]

test_ship = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]

with open('input.txt', 'r') as f:
    data = [(int(line.split()[1])*-1, int(line.split()[3])-1, int(line.split()[5])-1) for line in f.readlines()]

for command in data:
    from_ = command[1]
    to_ = command[2]
    what_ = ship[command[1]][command[0]:]

    ship[command[2]].extend(what_)
    ship[command[1]] = ship[from_][0:len(ship[from_])+command[0]]

for _ in ship:
    print(_[-1])
