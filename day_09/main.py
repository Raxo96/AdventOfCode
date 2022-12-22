from copy import copy
from math import sqrt
import matplotlib.pyplot as plt

visited_pos = [[0, 0]]


class Segment:
    def __init__(self, name):
        self.name = name
        self.current_pos = [0, 0]
        self.prev_pos = [0, 0]
        self.prev_segment = None

    def update_pos(self):
        if sqrt((self.prev_segment.current_pos[0] - self.current_pos[0]) ** 2 + (
                self.prev_segment.current_pos[1] - self.current_pos[1]) ** 2) > sqrt(2):
            self.prev_pos = self.current_pos
            self.current_pos = self.prev_segment.prev_pos


segments = [Segment(i) for i in range(0, 10)]
for i, s in enumerate(segments[1:]):
    s.prev_segment = segments[s.name - 1]


def update_visited_list(visited, current):
    if current not in visited:
        visited.append(current)
    return visited


def visualize():
    x = [p.current_pos[0] for p in segments]
    y = [p.current_pos[1] for p in segments]
    plt.scatter(x, y)
    for i in x:
        plt.annotate(f"{i} :{x[i], y[i]}", (x[i],y[i]))
    plt.show()


head = segments[0]
tail = segments[-1]


with open('test_input.txt', 'r') as f:
    commands = [line.replace('\n', '') for line in f.readlines()]

commands = [l.split() for l in commands]

for command in commands:
    direction, step = command[0], int(command[-1])
    if direction == 'R':
        for _ in range(0, step):
            head.prev_pos = copy(head.current_pos)
            head.current_pos[0] += 1
            for s in segments[1:]:
                s.update_pos()
            visualize()
            visited_pos = update_visited_list(visited_pos, tail.current_pos)

    elif direction == 'L':
        for _ in range(0, step):
            head.prev_pos = copy(head.current_pos)
            head.current_pos[0] -= 1
            for s in segments[1:]:
                s.update_pos()
            visualize()
            visited_pos = update_visited_list(visited_pos, tail.current_pos)

    elif direction == 'U':
        for _ in range(0, step):
            head.prev_pos = copy(head.current_pos)
            head.current_pos[1] += 1
            for s in segments[1:]:
                s.update_pos()
            visualize()
            visited_pos = update_visited_list(visited_pos, tail.current_pos)

    elif direction == 'D':
        for _ in range(0, step):
            head.prev_pos = copy(head.current_pos)
            head.current_pos[1] -= 1
            for s in segments[1:]:
                s.update_pos()
            visualize()
            visited_pos = update_visited_list(visited_pos, tail.current_pos)


print(visited_pos)
print(len(visited_pos))
