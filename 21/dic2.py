from collections import Counter

from util import christmas_input
DIRAC_ROLLS = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


def dirac_play(p1_start, p2_start):
    game_states = Counter()
    game_states[((p1_start - 1, 0), (p2_start - 1, 0))] = 1
    wins = [0, 0]
    rnd_cnt = 0

    while game_states:
        new_states = Counter()
        p = rnd_cnt % 2

        for state, n_universe in game_states.items():
            for roll, n_rolls in DIRAC_ROLLS.items():
                new_s = list(state)
                new_pos = (state[p][0] + roll) % 10
                new_score = state[p][1] + new_pos + 1

                if new_score >= 21:
                    wins[p] += n_universe * n_rolls
                else:
                    new_s[p] = (new_pos, new_score)
                    new_states[tuple(new_s)] += n_universe * n_rolls

        rnd_cnt += 1
        game_states = new_states
    return wins

print("Part 2")
assert dirac_play(4, 8) == 444356092776315
