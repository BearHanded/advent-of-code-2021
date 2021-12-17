from util import christmas_input

FILE_1 = './input.txt'
TEST_FILE_EXPANDED = './test_input.txt'

def adjacent(x, y, max_length):
    adj = []
    for pair in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        next_x = pair[0] + x
        next_y = pair[1] + y
        if 0 <= next_x < max_length and 0 <= next_y < max_length:
            adj.append((next_x, next_y))
    return adj


def explore(cavern):
    max_length = len(cavern)
    costs = {(0, 0): 0}
    explore_queue = [(0, 0)]

    for (x, y) in explore_queue:
        for (x1, y1) in adjacent(x, y, max_length):
            # Save to known values
            if (x1, y1) in costs and costs[x1, y1] <= costs[x, y] + cavern[y1][x1]:
                continue
            costs[x1, y1] = costs[x, y] + cavern[y1][x1]  # running total, min to get to a given point
            explore_queue.append((x1, y1))
    print("Min journey:", costs[max_length - 1, max_length - 1])


def expand(cavern):
    embiggened = [[] for i in range(0, len(cavern) * 5)]
    for x in range(0, 5):
        for y in range(0, 5):
            modifier = x + y
            for idx, row in enumerate(cavern):
                embiggened[y*len(cavern) + idx].extend([wrapped(val, modifier) for val in row])
    return embiggened


def wrapped(value, modifier):
    new_val = value + modifier
    return new_val if new_val <= 9 else new_val % 9


# Parse
print("Part 1: ")
rows = [[int(x) for x in row] for row in christmas_input.file_to_array(FILE_1)]
explore(rows)

print("Part 2 test:")
rows = [[int(x) for x in row] for row in christmas_input.file_to_array(TEST_FILE_EXPANDED)]
expanded = expand(rows)
explore(expanded)

print("Part 2: ")
rows = [[int(x) for x in row] for row in christmas_input.file_to_array(FILE_1)]
expanded = expand(rows)
explore(expanded)

