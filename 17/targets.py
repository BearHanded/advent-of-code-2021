from util import christmas_input
import math

FILE_1 = './input.txt'
TEST_FILE = './test_input.txt'


def calculate_max(x_points, y_points):
    grav = -1
    drag = -1
    position = [0, 0]
    max_y = 0

    # to be cool, x just needs to be such that drag zeroes out velocity in range
    angle_x = get_x(x_points)
    angle_y = get_y(y_points)
    print(angle_x, angle_y)
    return


def get_x(x_points):
    # to be cool, x just needs to be such that drag zeroes out velocity in range
    n = x_points[0] / 2
    solved = False
    bound_start = 0
    bound_end = x_points[0]
    while not solved:
        final_position = (n * (n+1)/2)
        solved = x_points[0] <= final_position <= x_points[1]
        if not solved:
            if final_position > x_points[1]:
                bound_end = n
            else:
                bound_start = n
            n = bound_start + (bound_end - bound_start) / 2
    return n


def get_y(y_points):
    # going for max height here
    initial_velocity = 0
    impossible = False
    size = abs(y_points[0] - y_points[1])
    while not impossible:
        in_flight = True
        curr_velocity = initial_velocity
        position = 0
        success = False
        while in_flight:
            position += curr_velocity
            curr_velocity -= 1

            if y_points[0] <= position <= y_points[1]:
                success = True
                in_flight = False
            elif position < y_points[0]:
                in_flight = False

        if not success and curr_velocity > size:
            impossible = True
        else:
            initial_velocity += 1
    return initial_velocity


def in_range(coordinates, x_points, y_points):
    return x_points[0] <= coordinates[0] <= x_points[1] and y_points[0] <= coordinates[1] <= y_points[1]


def has_missed(coordinates, x_points, y_points):
    return coordinates[0] > x_points[1] or coordinates[1] < y_points[0]

# Parse
print("Part 1: ")
test = (20, 30), (-5, -10)          # target area: x=20..30, y=-10..-5
part_1 = (32, 65), (-177, -225)     # target area: x=32..65, y=-225..-177

highest_arc = calculate_max((20, 30), (-5, -10))