with open('input.txt', 'r') as f:
    data = f.readlines()

data = [l.split() for l in data]
breakpoints = [x for x in range(20, 221, 40)]

x = 1
cycle = 0
strengths = []

password_lines = [["" for _ in range(0, 40)] for _ in range(0, 6)]
row = 0
trigger = 40


def update_password(sprite_pos, c):
    if c % 40 in range(sprite_pos-1, sprite_pos + 2):
        password_lines[row][c % 40] = '#'
    else:
        password_lines[row][c % 40] = '.'


def check_breakpoint(c, x):
    if c in breakpoints:
        strengths.append(c * x)


for command in data:
    if command[0] == 'noop':
        update_password(x, cycle)
        cycle += 1
    elif command[0] == 'addx':
        update_password(x, cycle)
        cycle += 1
        if cycle >= trigger:
            row += 1
            trigger += 40
        update_password(x, cycle)
        cycle += 1
        x += int(command[1])
    if cycle >= trigger:
        row += 1
        trigger += 40

for _ in password_lines:
    print(''.join(_))
