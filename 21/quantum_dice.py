from functools import lru_cache

DISTRIBUTIONS = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


@lru_cache(maxsize=None)
def get_wins(position_a, position_b, score_a, score_b):
    if score_a >= 21:
        return [1, 0]
    if score_b >= 21:
        return [0, 1]

    wins = [0, 0]

    for increment, amount in DISTRIBUTIONS.items():
        new_position = (position_a + increment - 1) % 10 + 1
        points = score_a + new_position
        other_wins = get_wins(position_b, new_position, score_b, points)  # same func, flipped targeting other
        wins = [wins[0] + other_wins[1] * amount, wins[1] + other_wins[0] * amount]
    return wins


test = get_wins(4, 8, 0, 0)
print(test)
assert max(test) == 444356092776315

results = get_wins(4, 5, 0, 0)
print(f'{results} : max - {max(results)}')