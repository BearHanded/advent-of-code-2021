from util import christmas_input
DEBUG = False


def read_file(file_name):
    east_slugs = set()
    south_slugs = set()
    rows = christmas_input.file_to_array(file_name)
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char == '>':
                east_slugs.add((x, y))
            elif char == 'v':
                south_slugs.add((x, y))
    size = (len(row), len(rows))
    return east_slugs, south_slugs, size


def wrap(x, y, size):
    return x % size[0], y % size[1]


def test_location(coordinates, east_slugs, south_slugs):
    return coordinates not in east_slugs and coordinates not in south_slugs


def pretty_print(east, south, size, step):
    if not DEBUG:
        if step % 100 == 0:
            print("   STEP ", step)
        return
    print("   STEP ", step)
    for y in range(0, size[1]):
        for x in range(0, size[0]):
            char = '.'
            if (x, y) in east and (x, y) in south:
                char = 'X'
            elif (x,y) in east:
                char = '>'
            elif (x,y) in south:
                char = 'v'
            # assert not ((x, y) in east and (x, y) in south)
            print(char, end='')
    print('')
    return


def tick(east_slugs, south_slugs, size):
    progress = False
    new_east = east_slugs.copy()
    new_south = south_slugs.copy()

    for slug_x, slug_y in east_slugs:
        new_location = wrap(slug_x + 1, slug_y, size)
        if test_location(new_location, east_slugs, south_slugs):
            new_east.remove((slug_x, slug_y))
            new_east.add(new_location)
            progress = True
    for slug_x, slug_y in south_slugs:
        new_location = wrap(slug_x, slug_y + 1, size)
        if test_location(new_location, new_east, south_slugs):  # TEST AGAINST NEW EAST HERE
            new_south.remove((slug_x, slug_y))
            new_south.add(new_location)
            progress = True
    return progress, new_east, new_south


def snail_lock(east_slugs, south_slugs, size):
    step = 0
    progress = True
    pretty_print(east_slugs, south_slugs, size, 0)
    while progress:
        progress, new_east, new_south = tick(east_slugs, south_slugs, size)
        east_slugs, south_slugs = new_east, new_south
        step += 1
        pretty_print(east_slugs, south_slugs, size, step)
    print("Locked in", step)
    return step


test_e, test_s, test_size = read_file('test_input.txt')
assert test_location((2,2), set([(2,2)]), set([])) is False
assert test_location((2,2), set([]), set([(2,2)])) is False
assert test_location((2,2), set([(1,1)]), set([(5,5)])) is True
assert snail_lock(test_e, test_s, test_size) == 58

e, s, input_size = read_file('input.txt')
snail_lock(e, s, input_size)
