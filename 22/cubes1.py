from util import christmas_input


def read_file(file_name):
    rows = [row.split(" ") for row in christmas_input.file_to_array(file_name)]
    instructions = []
    for row in rows:
        command = [0 if row[0] == 'off' else 1]
        cube = row[1].split(',')
        by_coord = [[i for i in pair.split("=")] for pair in cube]
        coordinates = [[int(i) for i in pair[1].split('..')] for pair in by_coord]
        for values in coordinates:
            values.sort()
        command.append(coordinates)
        instructions.append(command)
    return instructions


def cap_range(a, b):
    if (a < -50 and b < -50) or (a > 50 and b > 50):
        return []
    out = range(max(min(a, 50), -50), max(min(b, 50), -50))
    return out


def reboot(instructions):
    cube_map = {}
    for instruction in instructions:
        toggle, cube = instruction
        for x in cap_range(cube[0][0], cube[0][1] + 1):
            for y in cap_range(cube[1][0], cube[1][1] + 1):
                for z in cap_range(cube[2][0], cube[2][1] + 1):
                    if toggle == 1:
                        cube_map[x, y, z] = 1
                    else:
                        cube_map.pop((x, y, z), 0)
    on_cubes = len(cube_map)
    print(f'Cubes on: {on_cubes}')
    return on_cubes


test = read_file('test_input.txt')
assert reboot(test) == 39

test = read_file('test_2_input.txt')
assert reboot(test) == 590784

part_one = read_file('input.txt')
