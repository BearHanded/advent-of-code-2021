from util import christmas_input
import math

FILE = './input.txt'
CORRUPTED_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
AUTOCOMPLETE_SCORE = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}
MATCHED = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
rows = christmas_input.file_to_array(FILE)

# Part 1
score = 0
incomplete_rows = []
auto_scores = []
for row in rows:
    stack = []
    auto_score = 0
    corrupted = False
    for bracket in row:
        if bracket in ['(', '[', '{', '<']:
            stack.append(bracket)
        else:
            opening = stack.pop()
            if opening != MATCHED[bracket]:
                score += CORRUPTED_SCORES[bracket]
                incomplete_rows.append(row)
                corrupted = True
                break
        # if closing, validate
    # if remaining in stack, incomplete
    if not corrupted:
        for remaining in reversed(stack):
            next_bracket = stack.pop()
            auto_score *= 5
            auto_score += AUTOCOMPLETE_SCORE[next_bracket]
        auto_scores.append(auto_score)
auto_scores = sorted(auto_scores)

print("Part 1:", score)
print("Part 2:", auto_scores[math.floor(len(auto_scores)/2)])
