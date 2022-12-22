from string import ascii_lowercase, ascii_uppercase

with open('input.txt', 'r') as f:
    data = [d.replace('\n', '') for d in f.readlines()]


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return list(set(lst3))


def intersection_of_3(lst1, lst2, lst3):
    lst4 = [value for value in lst1 if value in lst2]
    lst4 = [value for value in lst4 if value in lst3]
    return list(set(lst4))


def inter_of_halfs(single_input):
    middle_idx = int(len(single_input) / 2)
    return intersection(single_input[0:middle_idx], single_input[middle_idx:])[0]


def get_data_slice(old_data):
    slice_of_data = old_data[0:3]
    return slice_of_data, old_data[3:]


score = 0
while data:
    sl, data = get_data_slice(data)
    inter = intersection_of_3(sl[0], sl[1], sl[2])[0]
    if inter.islower():
        score += ascii_lowercase.index(inter) + 1
    else:
        score += ascii_uppercase.index(inter) + 27

# score = 0
# for line in data:
#     inter = inter_of_halfs(line)
#     if inter.islower():
#         score += ascii_lowercase.index(inter) + 1
#     else:
#         score += ascii_uppercase.index(inter) + 27

print(score)
