from util import christmas_input

FILE = './input.txt'

rows = christmas_input.file_to_array(FILE)


def map_sums(active_rows):
    rotated = list(zip(*active_rows[::-1]))
    most_common = []
    least_common = []
    sums = []
    row_idx = 0
    for row in rotated:
        bits = [int(bit) for bit in row]
        sums.append({0: 0, 1: 0})
        for bit in bits:
            sums[row_idx][bit] += 1

            # get max value from dict
        v = list(sums[row_idx].values())
        k = list(sums[row_idx].keys())
        most_common.append(k[v.index(max(v))])
        least_common.append(k[v.index(min(v))])
        row_idx += 1
    return sums, most_common, least_common


def to_value(arr):
    return int("".join([str(x) for x in arr]), 2)


def oxygen_filter(o_row, idx, curr_sums, curr_gamma):
    most_common_bit = curr_gamma[idx]
    if curr_sums[idx][0] == curr_sums[idx][1]:
        most_common_bit = 1
    return o_row[idx] == str(most_common_bit)


def carbon_filter(c_row, idx, curr_sums, curr_epsilon):
    least_common_bit = curr_epsilon[idx]
    if curr_sums[idx][0] == curr_sums[idx][1]:
        least_common_bit = 0
    return c_row[idx] == str(least_common_bit)


myArr, gamma, epsilon = map_sums(rows)

###
# POWER!!!
##
g = to_value(gamma)
e = to_value(epsilon)
print("Power: ")
print(g, "*", e, ":", g * e)

# oxygen gen rating
gamma_idx = 0
oxygen = rows.copy()

# for most_common_bit in gamma:
while len(oxygen) > 1:
    current_sums, current_gamma, current_epsilon = map_sums(oxygen)
    oxygen = [x for x in oxygen if oxygen_filter(x, gamma_idx, current_sums, current_gamma)]
    gamma_idx += 1
print(oxygen)

# Carbon
epsilon_idx = 0
carbon = rows.copy()

while len(carbon) > 1:
    current_sums, current_gamma, current_epsilon = map_sums(carbon)
    carbon = [x for x in carbon if carbon_filter(x, epsilon_idx, current_sums, current_epsilon)]
    epsilon_idx += 1
print(carbon)

c = to_value(carbon)
o = to_value(oxygen)
print("Part 2: ")
print(o, "*", c, ":", o * c)
