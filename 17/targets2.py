FILE_1 = './input.txt'
TEST_FILE = './test_input.txt'


def calculate_max(x_points, y_points):
    total = 0
    max_height = 0
    for angle_x in range(0, 1000):
        final_position = (angle_x * (angle_x + 1) / 2)
        if final_position < x_points[0]:  # Doesn't reach target. Kill
            continue
        if angle_x > x_points[1]:  # too fast to hit target
            break
        success = False

        # Simulate Y
        for angle_y in range(-1000, 1000):
            if angle_y < y_points[0]:  # too fast to hit target
                continue
            xv, yv = angle_x, angle_y
            x, y = 0, 0
            trip_max_height = 0

            for _ in range(1000):
                x += xv
                y += yv
                trip_max_height = max(trip_max_height, y)

                if xv > 0:
                    xv -= 1
                yv -= 1

                if in_range((x, y), x_points, y_points):
                    max_height = max(max_height, trip_max_height)
                    total += 1
                    success = True
                    print("(", angle_x, angle_y, ")", end=" ")
                    break
                elif y < y_points[0]:  # Passed target. Kill
                    break
        if success:
            print("")

    print("Max Y:", max_height)
    print("Total", total)


def in_range(coordinates, x_points, y_points):
    return x_points[0] <= coordinates[0] <= x_points[1] and y_points[0] <= coordinates[1] <= y_points[1]


# Parse
print("TEST: ")
calculate_max((20, 30), (-10, -5))
print("LIVE: ")
calculate_max((32, 65), (-225, -177))
