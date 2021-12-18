import math
import json
import copy
from util import christmas_input

DEBUG = False
EXPLODE = "EXPLODE"
SPLIT = "SPLIT"


def snail_addition(array_a, array_b):
    return [array_a, array_b]


def add_list(assignment):
    number = assignment[0]
    for item in assignment[1:]:
        number = snail_addition(number, item)
        number = reduce(number)
    return number


def reduce(phrase):
    reducing = True

    while reducing:
        reducing = try_reduce(phrase, phase=EXPLODE)
        if not reducing:
            reducing = try_reduce(phrase, phase=SPLIT)
    return phrase


def get_sub_phrase(phrase, indexes):
    target = phrase
    for i in indexes:
        target = target[i]
    return target


def try_reduce(phrase, indexes=[], phase=EXPLODE):
    if phase == EXPLODE and len(indexes) >= 4:  # EXPLODE
        parent = phrase
        for i in indexes[:-1]:
            parent = parent[i]
        target = parent[indexes[-1]]

        reversed_idx = [i for i in reversed(indexes)]
        if 1 in reversed_idx:  # LEFT
            left_branch = indexes[:-1 * (reversed_idx.index(1) + 1)]
            left_parent = get_sub_phrase(phrase, left_branch)
            if isinstance(left_parent[0], list):
                left_parent = left_parent[0]
                while isinstance(left_parent[1], list):
                    left_parent = left_parent[1]
                left_parent[1] += target[0]
            else:
                left_parent[0] += target[0]

        # Add right
        if 0 in reversed_idx:  # RIGHT
            right_branch = indexes[:-1 * (reversed_idx.index(0) + 1)]
            right_parent = get_sub_phrase(phrase, right_branch)
            if isinstance(right_parent[1], list):
                right_parent = right_parent[1]
                while isinstance(right_parent[0], list):
                    right_parent = right_parent[0]
                right_parent[0] += target[1]
            else:
                right_parent[1] += target[1]

        # print("EXPLODE", parent[indexes[-1]])
        parent[indexes[-1]] = 0
        return True

    sub_phrase = get_sub_phrase(phrase, indexes)
    for idx, number in enumerate(sub_phrase):
        if isinstance(number, list):  # Array
            new_indexes = indexes.copy()
            new_indexes.append(idx)
            modified = try_reduce(phrase, new_indexes, phase=phase)  # Modifies list
            if modified:
                return True
        else:  # number -> split?
            if phase == SPLIT and number > 9:
                # if number > 10, split
                # print("SPLIT", sub_phrase[idx])
                sub_phrase[idx] = [math.floor(number / 2), math.ceil(number / 2)]
                return True
    return False


def get_magnitude(phrase):
    left = get_magnitude(phrase[0]) if isinstance(phrase[0], list) else phrase[0]
    right = get_magnitude(phrase[1]) if isinstance(phrase[1], list) else phrase[1]
    return left * 3 + right * 2


def strings_to_arrays(str_array):
    return [json.loads(i) for i in str_array]


if DEBUG:
    assert snail_addition([1, 2], [[3, 4], 5]) == [[1, 2], [[3, 4], 5]]
    # Split tests
    assert reduce([11, 3]) == [[5, 6], 3]
    #
    # # Explode Tests
    assert reduce([[[[[9, 8], 1], 2], 3], 4]) == [[[[0, 9], 2], 3], 4]
    assert reduce([7, [6, [5, [4, [3, 2]]]]]) == [7, [6, [5, [7, 0]]]]
    assert reduce([[6, [5, [4, [3, 2]]]], 1]) == [[6, [5, [7, 0]]], 3]
    added = snail_addition([[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1])
    assert reduce(added) == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]

    # magnitude
    assert get_magnitude([[1, 2], [[3, 4], 5]]) == 143
    assert get_magnitude([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]) == 1384
    assert get_magnitude([[[[1, 1], [2, 2]], [3, 3]], [4, 4]]) == 445

    test_large = strings_to_arrays(christmas_input.file_to_array('./test_input.txt'))
    r = add_list(test_large)
    assert add_list(test_large) == [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]

    test_large_2 = strings_to_arrays(christmas_input.file_to_array('./test_input_magnitude.txt'))
    result = add_list(test_large_2)
    assert result == [[[[6, 6], [7, 6]], [[7, 7], [7, 0]]], [[[7, 7], [7, 7]], [[7, 8], [9, 9]]]]
    assert get_magnitude(result) == 4140

print("PART 1")
part_1 = strings_to_arrays(christmas_input.file_to_array('./input.txt'))
result = add_list(part_1)
print(get_magnitude(result))

print("PART 2")
part_2 = strings_to_arrays(christmas_input.file_to_array('./input.txt'))
max_mag = 0
for i in part_2:
    for j in part_2:
        if i == j:
            continue
        potential_value = add_list([copy.deepcopy(i), copy.deepcopy(j)])
        max_mag = max(get_magnitude(potential_value), max_mag)
print(max_mag)

