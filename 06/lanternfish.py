from util import christmas_input
from collections import Counter

FILE = './input.txt'
TOTAL_DAYS = 256  # 18 in example, 80 part one, 256 part two


def go_fish(initial_state, days):
    counts = Counter(initial_state)
    fish_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for key in counts.keys():
        fish_state[key] = counts[key]

    for day in range(0, days):
        popped = fish_state.pop(0)
        fish_state.append(0)
        if popped > 0:
            fish_state[6] += popped
            fish_state[8] += popped
    print("Total Fish:", sum(fish_state))
    return fish_state


# Parse
initial_fish = [int(x) for x in christmas_input.file_as_string(FILE).split(",")]
smart_fish(initial_fish, TOTAL_DAYS)
