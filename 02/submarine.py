from util import christmas_input


class Coordinates:
    def __init__(self):
        self.x = 0  # forward
        self.y = 0  # horizontal (unused)
        self.z = 0  # vertical


def nav_down(coordinates, amount):
    coordinates.z += amount


def nav_up(coordinates, amount):
    coordinates.z -= amount


def nav_fwd(coordinates, amount):
    coordinates.x += amount


nav_rules = {
    "forward": nav_fwd,
    "down": nav_down,
    "up": nav_up,
}

FILE = './input.txt'
instructions = [str(i) for i in christmas_input.file_to_array(FILE)]

position = Coordinates()

for instruction in instructions:
    segments = instruction.split(" ")
    operation = nav_rules.get(segments[0])
    operation(position, int(segments[1]))

print(position.x, position.y, position.z)
print(position.x * position.z)