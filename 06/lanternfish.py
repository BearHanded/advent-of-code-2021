from functools import reduce

from util import christmas_input
import datetime
from collections import Counter

FILE = './input.txt'
TOTAL_DAYS = 256  # 18 in example, 80 part one, 256 part two
DETAILED_PRINT = False


# Original Part 1 Solution
def go_fish(fish_state, days):
    print("Initial state:", fish_state)
    for day in range(0, days):
        queued_fish = 0
        for i in range(len(fish_state)):
            # Tick Everything
            fish_state[i] = fish_state[i] - 1
            # Move -1 up to new number and add one
            if fish_state[i] < 0:
                fish_state[i] = 6
                queued_fish += 1
        fish_state.extend([8] * queued_fish)

        if DETAILED_PRINT:
            print("After", day + 1, "days:", fish_state)
        elif day % 5 == 0:
            print("Day", day, "-", datetime.datetime.now())
    print("Total Fish:", len(fish_state))
    return fish_state


class FishFamily:
    def __init__(self, timer, count):
        self.timer = timer
        self.count = count

    def countdown(self):
        self.timer -= 1
        return self.timer


    def add(self, count):
        self.count += count
        return self


def smart_fish(initial_state, days):
    counts = Counter(initial_state)
    fish_state = []
    for key in counts.keys():
        fish_state.append(FishFamily(key, counts[key]))

    for day in range(0, days):
        queued_fish = 0
        removed_fish = None
        for family in fish_state:
            new_timer = family.countdown()
            if new_timer < 0:
                queued_fish += family.count
                removed_fish = family

        if queued_fish:
            # A family popped. Add them to any existing 6, add children at 8, remove -1
            joined_idx = [idx for idx, element in enumerate(fish_state) if element.timer == 6]
            if len(joined_idx) > 0:
                fish_state[joined_idx[0]].add(queued_fish)
            else:
                fish_state.append(FishFamily(6, queued_fish))
            fish_state.append(FishFamily(8, queued_fish))
            if removed_fish is not None:
                fish_state.remove(removed_fish)

        if day % 5 == 0:
            print("Day", day, "-", datetime.datetime.now())
    print("Total Fish:", reduce(lambda x, y: x.add(y.count), fish_state).count)
    return fish_state


# Parse
initial_fish = [int(x) for x in christmas_input.file_as_string(FILE).split(",")]
smart_fish(initial_fish, TOTAL_DAYS)
