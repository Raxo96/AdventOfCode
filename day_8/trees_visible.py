with open('input.txt', 'r') as file:
    f = [[[int(x), False] for x in line.replace('\n', '').split(',')[0]] for line in file.readlines()]


def part_1(forest):
    visible_trees = 2 * len(forest[0]) + 2 * (len(forest[0]) - 2)
    row_max = len(forest[0])

    def right_and_left(current_forest, counter):
        for row in current_forest[1:-1]:
            i = 0
            current_height = row[i][0]
            while i < row_max - 2:
                if row[i + 1][0] > current_height and not row[i + 1][1]:
                    counter += 1
                    row[i + 1][1] = True
                if row[i + 1][0] > current_height:
                    current_height = row[i + 1][0]
                i += 1

        for row in current_forest[1:-1]:
            i = row_max - 1
            current_height = row[-1][0]
            while i > 1:
                if row[i - 1][0] > current_height and not row[i - 1][1]:
                    counter += 1
                    row[i - 1][1] = True
                    current_height = row[i - 1][0]
                if row[i - 1][0] > current_height:
                    current_height = row[i - 1][0]
                i -= 1

        return counter, current_forest

    def transpose(base_forest):
        t_forest = []
        row = []
        for i in range(0, row_max):
            for _ in base_forest:
                row.append(_[i])
            t_forest.append(row)
            row = []
        return t_forest

    visible_trees, forest = right_and_left(forest, visible_trees)
    forest = transpose(forest)
    visible_trees, forest = right_and_left(forest, visible_trees)
    print(visible_trees)


def part_two(_forest):
    def look_right(forest, start_row, start_column):
        max_step = len(forest[0]) - start_column
        start_tree_value = forest[start_row][start_column][0]
        count = 0
        for i in range(1, max_step):
            if forest[start_row][start_column + i][0] < start_tree_value:
                count += 1
            else:
                count += 1
                break

        return count

    def look_left(forest, start_row, start_column):
        start_tree_value = forest[start_row][start_column][0]
        count = 0
        for i in range(1, start_column + 1):
            if forest[start_row][start_column - i][0] < start_tree_value:
                count += 1
            else:
                count += 1
                break

        return count

    def look_down(forest, start_row, start_column):
        max_step = len(forest[0]) - start_row
        start_tree_value = forest[start_row][start_column][0]
        count = 0
        for i in range(1, max_step):
            if forest[start_row + i][start_column][0] < start_tree_value:
                count += 1
            else:
                count += 1
                break

        return count

    def look_up(forest, start_row, start_column):
        start_tree_value = forest[start_row][start_column][0]
        count = 0
        for i in range(1, start_row + 1):
            if forest[start_row - i][start_column][0] < start_tree_value:
                count += 1
            else:
                count += 1
                break

        return count

    def count_score(forest, r, c):
        return look_up(forest, r, c) * look_down(forest, r, c) * look_left(forest, r, c) * look_right(forest, r, c)

    results = []
    row_length = len(f[0])
    for i in range(0, row_length):
        for j in range(0, row_length):
            results.append(count_score(f, i, j))

    print(max(results))
