from util import christmas_input

FILE = './input.txt'


def align_crabs(crabs):
    costs = []
    for position in range(0, max(crabs) + 1):
        costs.append(sum(abs(position - x) for x in crabs))
    print("Part 1:", min(costs))


def scaling_crabs(crabs):
    costs = []
    for position in range(0, max(crabs) + 1):
        costs.append(sum(fuel_burn(position, x) for x in crabs))
    print("Part 2:", min(costs))


def fuel_burn(position, x):
    return sum([i for i in range(1, abs(position - x) + 1)])


# Parse
values = [int(x) for x in christmas_input.file_as_string(FILE).split(",")]
align_crabs(values)
scaling_crabs(values)
