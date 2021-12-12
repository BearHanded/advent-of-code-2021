from util import christmas_input

FILE = './input.txt'

flashes = 0


class Octopus:
    def __init__(self, energy):
        self.power = energy


def print_pretty(octopi):
    for row in octopi:
        for item in row:
            print(item.power, end=" ")
        print("")
    print("------")


def tick(octopi):
    # Add one to all
    for y in range(0, len(octopi)):
        for x in range(0, len(octopi[0])):
            octopi = gain_power(octopi, (x, y))

    for y in range(0, len(octopi)):
        for x in range(0, len(octopi[0])):
            if octopi[y][x].power > 9:
                octopi[y][x].power = 0
    return octopi


def gain_power(octopi, coordinate):
    global flashes
    (x, y) = coordinate
    octopi[y][x].power += 1

    if octopi[y][x].power == 10:
        flashes += 1
        if y != len(octopi) - 1: # N
            gain_power(octopi, (x, y+1))
            if x != len(octopi[0]) - 1:
                gain_power(octopi, (x + 1, y + 1))  # NW
            if x > 0:
                gain_power(octopi, (x - 1, y + 1))  # NE
        if x != len(octopi[0]) - 1:
            gain_power(octopi, (x+1, y))  # W
        if y > 0:  # S
            gain_power(octopi, (x, y-1))
            if x != len(octopi[0]) - 1:
                gain_power(octopi, (x + 1, y - 1))  # SW
            if x > 0:
                gain_power(octopi, (x - 1, y - 1))  # SE
        if x > 0:
            gain_power(octopi, (x - 1, y))  # E
    return octopi


# Parse
rows = christmas_input.file_to_array(FILE)
parsed = [[Octopus(int(value)) for value in row] for row in rows]

print_pretty(parsed)
for i in range(0, 100):
    parsed = tick(parsed)
    if i < 10 or (i + 1) % 10 == 0:
        print_pretty(parsed)


print("Flashes:", flashes)