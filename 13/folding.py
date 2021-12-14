from util import christmas_input
FILE = './input.txt'


def pretty_print(points, size):
    pretty = [["."] * size[0] for _ in range(size[1])]

    for point in points:
        pretty[point[1]][point[0]] = '#'

    for row in pretty:
        for point in row:
            print(point, end=" ")
        print()


def fold_paper(points, instruction, size):
    # if greater than fold, new point = 2*(fold + 1)) - point
    command = instruction.replace('fold along ', '').split('=')
    fold_line = int(command[1])
    if command[0] == 'x':
        size[0] = size[0] - fold_line
    else:
        size[1] = size[1] - fold_line

    for point in points:
        if command[0] == 'x':
            if command[1] == point[0]:
                # remove
                removed = points.pop(points.index(point))
            elif point[0] > fold_line:
                point[0] = 2 * fold_line - point[0]
        else:
            if fold_line == point[1]:
                # remove
                removed = points.pop(points.index(point))
            elif point[1] > fold_line:
                point[1] = 2 * fold_line - point[1]
    return points, size


# Parse
rows = christmas_input.file_to_array(FILE)
print(rows)
instruction_break = rows.index('')
paper = [[int(pair[0]), int(pair[1])] for pair in [row.split(",") for row in rows[:instruction_break]]]
instructions = rows[instruction_break+1:]
size = [max([i[0] for i in paper]), max([i[1] for i in paper])]

for instruction in instructions:
    paper, size = fold_paper(paper, instruction, size)
    print(instruction)


print("size:", size)
without_duplicates = []
for elem in paper:
    if elem not in without_duplicates:
        without_duplicates.append(elem)

pretty_print(paper, size)
print("dots:", len(without_duplicates))


