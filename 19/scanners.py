from util import christmas_input

###
# A chunk of this was written from a comment in the solutions section. Got stuck today pretty bad
# Threw away an initial implementation where matches were id'd by the manhattan distances b/w points
# as a thumbprint


class Frame:
    def __init__(self, readout):
        self.points = set(readout)
        self.scanners = {(0, 0, 0)}
        self.manhattans = set()

    def join(self, other_scanner):
        for axis1 in range(3):
            for sign1 in [1, -1]:
                for axis2 in {0, 1, 2} - {axis1}:
                    for sign2 in [1, -1]:
                        orientation = (axis1, sign1, axis2, sign2)
                        candidates = [reorient(point, *orientation) for point in other_scanner.points]
                        corrected, scanner = try_align(self.points, candidates)
                        if corrected:
                            self.scanners.add(scanner)
                            self.points.update(corrected)
                            return True
        return False

    def build_manhattans(self):
        for i in self.scanners:
            for j in self.scanners:
                self.manhattans.add(manhattan(i, j))


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


def try_align(known_beacons, unaligned_beacons):
    for axis in range(3):
        known_sorted = sorted(known_beacons, key=lambda pos: pos[axis])
        unaligned_beacons.sort(key=lambda pos: pos[axis])
        known_diffs = diffs(known_sorted)
        unaligned_diffs = diffs(unaligned_beacons)
        inter = set(known_diffs) & set(unaligned_diffs)
        if inter:
            diff = inter.pop()
            kx, ky, kz = known_sorted[known_diffs.index(diff)]
            ux, uy, uz = unaligned_beacons[unaligned_diffs.index(diff)]
            ox, oy, oz = (ux - kx, uy - ky, uz - kz)
            moved = {(x - ox, y - oy, z - oz) for (x, y, z) in unaligned_beacons}
            matches = known_beacons & moved
            if len(matches) >= 12:
                return moved, (ox, oy, oz)
    return None, None


def reorient(pos, axis1, sign1, axis2, sign2):
    axis3 = 3 - (axis1 + axis2)
    sign3 = 1 if (((axis2 - axis1) % 3 == 1) ^ (sign1 != sign2)) else -1
    return pos[axis1] * sign1, pos[axis2] * sign2, pos[axis3] * sign3


def diffs(poses):
    return [
        (x1 - x0, y1 - y0, z1 - z0)
        for (x0, y0, z0), (x1, y1, z1)
        in zip(poses, poses[1:])
    ]


def file_to_readouts(file_name):
    rows = christmas_input.file_to_array(file_name)
    readouts = []
    scanner_idx = -1
    for i in rows:
        if i == '':
            continue
        if '--- scanner' in i:
            readouts.append([])
            scanner_idx += 1
        else:
            readouts[scanner_idx].append(tuple(map(int, i.split(','))))
    return readouts


def build_map(file_name):
    readouts = file_to_readouts(file_name)
    mapped = Frame(readouts[0])
    unmapped = [Frame(readout) for readout in readouts[1:]]

    while unmapped:
        for scanner in unmapped:
            if mapped.join(scanner):
                progress = True
                unmapped.remove(scanner)
                break  # start over at the top

    mapped.build_manhattans()
    print(f'{file_name}:\n  Points: {len(mapped.points)}\n  Max Distance:{max(mapped.manhattans)}')

    return mapped


assert manhattan((1105, -1205, 1229), (-92, -2380, -20)) == 3621
test = build_map("test_input.txt")
assert len(test.points) == 79
assert max(test.manhattans) == 3621

test = build_map("input.txt")
