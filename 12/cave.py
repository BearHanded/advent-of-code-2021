from util import christmas_input

FILE = './test_input.txt'
START = 'start'
END = 'end'


def build_paths(paths, journey='', key=START, bonus_time=False):
    available = paths[key]
    current = key if journey == '' else journey + "," + key
    results = []

    for route in available:
        if route == START:
            continue
        elif route == END:
            results.append(current)
        elif route.isupper() or route not in current:
            results.extend(build_paths(paths, current, route, bonus_time))
        elif bonus_time:
            results.extend(build_paths(paths, current, route, False))
    return results


# Parse
rows = christmas_input.file_to_array(FILE)
data = [(path[0], path[1]) for path in [row.split("-") for row in rows]]
segments = {}
for path in data:
    # Bidirectional travel
    if path[0] not in segments:
        segments[path[0]] = []
    segments[path[0]].append(path[1])
    if path[1] not in segments:
        segments[path[1]] = []
    segments[path[1]].append(path[0])

# PART 1:
all_paths = build_paths(segments)
print("Part 1:", len(all_paths))

# PART 2:
all_paths = build_paths(segments, bonus_time=True)
print("Part 2:", len(all_paths))
