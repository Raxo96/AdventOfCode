mtrx = [[0 for n in range(0, 6060)] for x in range(0, 6060)]

row = [0]
column = 0
c = 20151125


def matrix_value(prev_value):
    return (prev_value * 252533) % 33554393


while mtrx[2946][3028] == 0:
    for r in row:
        mtrx[r][column] = c
        column += 1
        c = matrix_value(c)
        continue

    row.insert(0, column)
    column = 0

print(mtrx[2946][3028])
