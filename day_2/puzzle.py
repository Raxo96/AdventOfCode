with open('input.txt', 'r') as file:
    data = file.read().split('\n')

game_input = []

for r in data:
    game_input.append((r[0], r[2]))

parser = {
    ('A', 'X'): 3,
    ('A', 'Y'): 4,
    ('A', 'Z'): 8,
    ('B', 'X'): 1,
    ('B', 'Y'): 5,
    ('B', 'Z'): 9,
    ('C', 'X'): 2,
    ('C', 'Y'): 6,
    ('C', 'Z'): 7
}

result = 0

for game in game_input:
    result += parser[game]

print(result)
