MOD_CONST = 1


class Monkey:
    def __init__(self, name, items, operation, test, if_true, if_false):
        global MOD_CONST
        self.name: int = name
        self.items: list = items
        self.operation: str = operation
        self.divisible_by: int = test
        self.if_true: int = if_true
        self.if_false: int = if_false
        self.worry_level = 0
        self.items_investigated = 0
        MOD_CONST *= self.divisible_by

    def inspect_item(self, item_worry):
        global MOD_CONST
        self.items_investigated += 1
        self.worry_level = item_worry
        self.worry_level = eval(self.operation.replace('old', str(self.worry_level))) % MOD_CONST
        if self.worry_level % self.divisible_by == 0:
            return self.worry_level, self.if_true
        else:
            return self.worry_level, self.if_false


def instances_generator():
    with open('input.txt', 'r') as f:
        data = f.readlines()

    monkeys = []
    single_monkey = ''
    for i, _ in enumerate(data):
        if 'false' not in _ and _ != '\n':
            single_monkey += _
        else:
            if _ != '\n':
                single_monkey += _
                monkeys.append(single_monkey)
                single_monkey = ''

    monkeys = [m.split('\n') for m in monkeys]
    monkeys_objects = []
    for m in monkeys:
        name = m[0][-2]
        items = m[1].replace('Starting items: ', '').split(',')
        items = [int(i) for i in items]
        operation = m[2].replace('Operation: new = ', '')
        test = int(m[3].split()[-1])
        if_true = int(m[4][-1])
        if_false = int(m[5][-1])

        monkeys_objects.append(Monkey(name, items, operation, test, if_true, if_false))
    return monkeys_objects


monkeys = instances_generator()
for r in range(0, 10000):
    for m in monkeys:
        for i in m.items:
            item, target = m.inspect_item(i)
            monkeys[target].items.append(item)
        m.items = []

r = sorted([m.items_investigated for m in monkeys])
print(r[-1] * r[-2])
