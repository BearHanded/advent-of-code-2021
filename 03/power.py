from util import christmas_input

FILE = './input.txt'

gamma = []
epsilon = []

rows = christmas_input.file_to_array(FILE)
rotated = list(zip(*rows[::-1]))

for row in rotated:
    bits = [int(bit) for bit in row]
    sums = {0: 0, 1: 0}
    for bit in bits:
        sums[bit] += 1

    # get max value from dict
    v = list(sums.values())
    k = list(sums.keys())
    gamma.append(k[v.index(max(v))])
    epsilon.append(k[v.index(min(v))])


def to_value(arr):
    return int("".join([str(x) for x in arr]), 2)


g = to_value(gamma)
e = to_value(epsilon)
print(g, "*", e, ":", g * e)
