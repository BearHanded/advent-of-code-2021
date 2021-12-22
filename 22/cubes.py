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


def overlap(cube_a, cube_b):
    xa, ya, za = cube_a
    xb, yb, zb = cube_b
    return xb[0] <= xa[1] and xb[1] >= xa[0] \
        and yb[0] <= ya[1] and yb[1] >= ya[0] \
        and zb[0] <= za[1] and zb[1] >= za[0]


def volume(cube):
    x, y, z = cube
    return (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)


def cube_subtraction(cube_a, cube_b):
    if cube_a != cube_b:
        if not overlap(cube_a, cube_b):
            yield cube_a
        else:
            xa, ya, za = cube_a
            xb, yb, zb = cube_b
            for xi, (x0, x1) in enumerate(
                    zip((xa[0], max(xa[0], xb[0]), xb[1] + 1), (xb[0] - 1, min(xa[1], xb[1]), xa[1]))):
                if x0 > x1:
                    continue
                for yi, (y0, y1) in enumerate(
                        zip((ya[0], max(ya[0], yb[0]), yb[1] + 1), (yb[0] - 1, min(ya[1], yb[1]), ya[1]))):
                    if y0 > y1:
                        continue
                    for zi, (z0, z1) in enumerate(
                            zip((za[0], max(za[0], zb[0]), zb[1] + 1), (zb[0] - 1, min(za[1], zb[1]), za[1]))):
                        if z0 > z1:
                            continue
                        if xi == 1 and yi == 1 and zi == 1:
                            continue
                        yield (x0, x1), (y0, y1), (z0, z1)


def reboot(instructions):
    cubes = []
    for toggle, cube in instructions:
        new_cubes = []
        for existing in cubes:
            new_cubes.extend(cube_subtraction(existing, cube))  # remove collisions, and queue
        if toggle:
            new_cubes.append(cube)                              # If "ON" add them back as smaller cubers
        cubes = new_cubes
    on_volume = sum(volume(cube) for cube in cubes)
    print("On volume:", on_volume)
    return on_volume


assert volume(([0, 4], [1, 6], [2, 8])) == 5 * 6 * 7
assert overlap(([0, 4], [1, 6], [2, 8]), ([0, 1], [1, 2], [2, 4])) is True
assert overlap(([0, 4], [1, 6], [2, 8]), ([100, 105], [100, 105], [100, 105])) is False
removed = cube_subtraction(([0, 4], [1, 6], [2, 8]), ([100, 105], [100, 105], [100, 105]))
out = [i for i in removed]
test = [([0, 4], [1, 6], [2, 8])]
assert out == test

test = read_file('test_3_input.txt')
assert reboot(test) == 2758514936282235
part_one = read_file('input.txt')
reboot(part_one)
