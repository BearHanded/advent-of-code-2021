from util import christmas_input

FILE = './test_input.txt'

# Parse
rows = christmas_input.file_to_array(FILE)
parsed = [[int(value) for value in row] for row in rows]


def explore_basin(depths, coordinate):
    # recursive search in basin range
    return 0


danger = []
basins = {}
for y in range(0, len(parsed)):
    for x in range(0, len(parsed[0])):
        depth = parsed[y][x]
        if (y == 0 or parsed[y - 1][x] > depth) and \
                (y + 1 >= len(parsed) or parsed[y + 1][x] > depth) and \
                (x == 0 or parsed[y][x - 1] > depth) and \
                (x + 1 >= len(parsed[0]) or parsed[y][x + 1] > depth):
            danger.append((parsed[y][x] + 1))
            basins[(x, y)] = parsed[y][x]

sizes = 0
for basin in basins.keys():
    sizes += explore_basin(parsed, basin)

print(basins)
print("Part 1:", sum(danger))
