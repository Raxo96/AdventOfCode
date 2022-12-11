class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.kids = []

    def __str__(self):
        if len(self.name) < 3:
            return f"{self.name} \t\t\t:{self.size}"
        elif len(self.name) > 6:
            return f"{self.name} \t:{self.size}"
        else:
            return f"{self.name} \t\t:{self.size}"

    def update_size(self, amount):
        self.size += amount
        if self.parent:
            self.parent.update_size(amount)


with open('input.txt', 'r') as f:
    commands = [line.replace('\n', '').split(',')[0] for line in f.readlines()]

initial_dir = Directory('/', None)
current_dir = initial_dir
every_single_dir = [initial_dir]
all_files = 0
for command in commands[1:]:
    if command.startswith('$'):
        if 'ls' in command:
            continue
        elif 'cd ..' in command:
            current_dir = current_dir.parent
        elif 'cd' in command:
            current_dir = Directory(command.split()[-1], current_dir)
            every_single_dir.append(current_dir)
    elif 'dir' in command:
        current_dir.kids.append(command.split()[1])
    elif command[0].isalnum():
        all_files += int(command.split()[0])
        current_dir.update_size(int(command.split()[0]))

big = []

for _ in every_single_dir:
    if _.size >= 389918:
        big.append(_.size)

print(min(big))