from util import christmas_input

FILE = './input.txt'
DIAGONAL_ALLOWED = True
PRINT = False


def map_size(coordinates):
    x_max = max(map(lambda pair: max(pair[0][0], pair[1][0]), coordinates))
    y_max = max(map(lambda pair: max(pair[0][1], pair[1][1]), coordinates))
    return x_max, y_max


class VentMap:
    def __init__(self, coordinates):
        self.collision_count = 0
        self.collisions = []
        M, N = map_size(coordinates)
        self.vent_map = [[0]*(N + 1) for _ in range((M + 1))]
        self.build_vent_map(coordinates)

    def print_pretty(self):
        rotated = zip(*self.vent_map[::-1])
        for row in rotated:
            for item in row[::-1]:
                print(item if item > 0 else ".", end=" ")
            print("")

    def build_vent_map(self, coordinates):
        for pair in coordinates:
            y_diff = pair[1][1] - pair[0][1]
            x_diff = pair[1][0] - pair[0][0]
            x_mod = 1 if x_diff >= 0 else -1
            y_mod = 1 if y_diff >= 0 else -1

            if x_diff == 0 or y_diff == 0:  # part 1 limit
                for x in range(pair[0][0], pair[1][0] + x_mod, x_mod):
                    for y in range(pair[0][1], pair[1][1] + y_mod, y_mod):
                        self.add_vent(x,y)
            elif DIAGONAL_ALLOWED:
                temp_x = pair[0][0]
                temp_y = pair[0][1]
                for point in range(0, x_diff + x_mod, x_mod):
                    self.add_vent(temp_x, temp_y)
                    temp_x += x_mod
                    temp_y += y_mod

    def add_vent(self, x, y):
        if self.vent_map[x][y] == 1:
            self.collision_count += 1
            self.collisions.append([x, y])
        self.vent_map[x][y] += 1

def rows_to_coordinates(rows):
    points = [row.split(" -> ") for row in rows]
    points_as_nums = [(list(map(int, row[0].split(","))), list(map(int, row[1].split(",")))) for row in points]
    return points_as_nums


# Parse
rows = christmas_input.file_to_array(FILE)
parsed = rows_to_coordinates(rows)
vent_map = VentMap(parsed)
if PRINT:
    vent_map.print_pretty()
print("Collisions", vent_map.collision_count)
