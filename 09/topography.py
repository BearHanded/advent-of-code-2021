from util import christmas_input

FILE = './input.txt'

danger = []
basins = {}


def explore_basin(depths, coordinate):
    # recursive search in basin range
    (x, y) = coordinate
    if depths[y][x].tracked or depths[y][x].height == 9:
        return 0
    depths[y][x].tracked = True

    size = 1
    if y > 0:
        size += explore_basin(depths, (x, y - 1))
    if y != len(depths) - 1:
        size += explore_basin(depths, (x, y + 1))
    if x > 0:
        size += explore_basin(depths, (x - 1, y))
    if x != len(depths[0]) - 1:
        size += explore_basin(depths, (x + 1, y))
    return size


class BasinPoint:
    def __init__(self, height):
        self.height = height
        self.tracked = False


# Parse
rows = christmas_input.file_to_array(FILE)
parsed = [[BasinPoint(int(value)) for value in row] for row in rows]

for y in range(0, len(parsed)):
    for x in range(0, len(parsed[0])):
        depth = parsed[y][x].height
        if (y == 0 or parsed[y - 1][x].height > depth) and \
                (y + 1 >= len(parsed) or parsed[y + 1][x].height > depth) and \
                (x == 0 or parsed[y][x - 1].height > depth) and \
                (x + 1 >= len(parsed[0]) or parsed[y][x + 1].height > depth):
            danger.append((parsed[y][x].height + 1))
            basins[(x, y)] = parsed[y][x].height
print("Part 1:", sum(danger))

sizes = []
for basin in basins.keys():
    sizes.append(explore_basin(parsed, basin))
sizes = sorted(sizes, reverse=True)

print("Part 2:", sizes[0] * sizes[1] * sizes[2])
