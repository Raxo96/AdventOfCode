def sum_of_calories():
    with open('input.txt', 'r') as file:
        data = file.readlines()

    data = [e.replace('\n', '') for e in data]

    single_elf = []
    calories = []
    for _ in data:
        if _:
            single_elf.append(int(_))
        else:
            calories.append(sum(single_elf))
            single_elf = []

    return calories


def max_calories_list():
    calories = sum_of_calories()
    print(f"Max calories : {max(calories)}, carried by elf #: {calories.index(max(calories))}")


def top_three_elfs():
    calories = sum_of_calories()

    calories = sorted(calories, reverse=True)
    print(f"Top three Elfes are carring {sum(calories[0:3])} calories in total")


top_three_elfs()
