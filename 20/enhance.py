from util import christmas_input

LIGHT_PIXEL, DARK_PIXEL = '#', '.'
PIXEL_TABLE = {
    DARK_PIXEL: 0,
    LIGHT_PIXEL: 1,
}


def read_file(file_name):
    rows = christmas_input.file_to_array(file_name)
    img_algorithm = rows[0]
    img = rows[2:]
    return img_algorithm, img


def get_pixel_value(coordinates, img, generation=0, universe_flicker=False):
    val = ''
    for y in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            surrounding_pixel = (coordinates[0] + x, coordinates[1] + y)
            if surrounding_pixel in img:
                val += '1' if img[surrounding_pixel] == LIGHT_PIXEL else '0'
            else:
                val += '1' if universe_flicker and generation % 2 == 1 else '0'
    return int(val, 2)


def map_pixels(image):
    mapped_pixels = {}
    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            mapped_pixels[x, y] = pixel
    return mapped_pixels


def get_output_pixel(position, algorithm):
    return algorithm[position]


def get_output_dimensions(image):
    points = [*image]
    # Consider 1 wider than max for changes
    max_x = max(points, key=lambda item: item[0])[0] + 1
    min_x = min(points, key=lambda item: item[0])[0] - 1
    max_y = max(points, key=lambda item: item[1])[1] + 1
    min_y = min(points, key=lambda item: item[1])[1] - 1
    return (min_x, max_x), (min_y, max_y)


def enhance(mapped_image, algorithm_string, generation=0):
    universe_flicker = algorithm_string[0] == '#' and algorithm_string[-1] == '.'
    (min_x, max_x), (min_y, max_y) = get_output_dimensions(mapped_image)
    output = {}
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            val = get_pixel_value((x, y), mapped_image, generation=generation, universe_flicker=universe_flicker)
            output[(x, y)] = get_output_pixel(val, algorithm_string)
    return output


def pretty_print(mapped_image):
    (min_x, max_x), (min_y, max_y) = get_output_dimensions(mapped_image)
    print("")
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            val = mapped_image.get((x, y), '.')
            print(val, end="")
        print("")


def run_enhancements(algorithm_string, image, amount):
    mapped = map_pixels(image)
    growth = mapped
    for generation in range(0, amount):
        growth = enhance(growth, algorithm_string, generation=generation)
    pixels = list(growth.values())
    total = pixels.count('#')
    print(f"Enhanced x{generation+1} - Total #:", total)
    return total


test_alg, test_img = read_file("test_input.txt")
test_map = map_pixels(test_img)
assert get_pixel_value((2, 2), test_map) == 34
assert get_pixel_value((-10, -10), test_map) == 0
assert get_output_pixel(34, test_alg) == LIGHT_PIXEL
assert get_output_pixel(33, test_alg) == DARK_PIXEL
assert get_output_pixel(35, test_alg) == LIGHT_PIXEL
assert run_enhancements(test_alg, test_img, 2) == 35

print("PART ONE: ")
alg, img_rows = read_file("input.txt")
run_enhancements(alg, img_rows, 2)
run_enhancements(alg, img_rows, 50)
