with open('input.txt', 'r') as f:
    data = f.read()

start_index = 14
i = 0

while True:
    four_last = data[i:start_index]
    if len(set(four_last)) == 14:
        print(i + 14)
        break
    i += 1
    start_index += 1

