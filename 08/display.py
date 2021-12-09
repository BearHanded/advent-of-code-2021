from util import christmas_input

# FILE = './test_input.txt'
FILE = 'input.txt'
COUNT_LOOKUP = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


def sort_display(display_string):
    return "".join(sorted(display_string))


# Part 1
def solve_wires(rows):
    all_output = []
    for codes in rows: # The rules change per-row
        wire_map = {}
        row_wires = codes[0]

        for combination in row_wires:  # Easy lookups: 1, 4, 7, 8
            digit = COUNT_LOOKUP.get(len(combination), None)
            if digit is not None:
                wire_map[digit] = combination

        while len(wire_map) < 10:
            for combination in row_wires:
                if len(combination) == 6:  # 0, 6
                    if all(x in combination for x in wire_map[4]):
                        wire_map[9] = combination
                    elif all(x in combination for x in wire_map[1]):
                        wire_map[0] = combination
                    else:
                        wire_map[6] = combination
                elif len(combination) == 5:  # 2, 3, 5, 9
                    if all(x in combination for x in wire_map[1]):
                        wire_map[3] = combination
                    elif all(x in ''.join(set(combination + wire_map[4])) for x in wire_map[8]):
                        # unique wires in 4 + 2 = 8
                        wire_map[2] = combination
                    elif len(wire_map) == 9:
                        wire_map[5] = combination

        # list out keys and values separately
        sorted_displays = {sort_display(v): k for k, v in wire_map.items()}

        display = []
        for combination in [sort_display(x) for x in codes[1]]:
            display.append(sorted_displays[combination])
        all_output.append(int("".join([str(i) for i in display])))  # join up all the numbers as if they were strings
    print("Sum total:   ", sum(all_output))


# Part 2
def count_easy(rows):
    num_count = 0
    for codes in rows:  # The rules change per-row
        wire_map = {}
        output = codes[1]
        for display in output:
            digit = COUNT_LOOKUP.get(len(display), None)
            if digit is not None:
                num_count += 1
    print("Known values:", num_count)


# Parse
rows = [[segment.strip().split(" ") for segment in row.split("|")] for row in christmas_input.file_to_array(FILE)]
count_easy(rows)
solve_wires(rows)
