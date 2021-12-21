from util import christmas_input


class Dice:
    def __init__(self):
        self.index = 1
        self.total_rolls = 0

    def roll_x(self, amount):
        out = 0
        for _ in range(0, amount):
            rolled = self.roll()
            # print(rolled, end=" ")
            out += rolled
        # print(" - ", end="")
        return out

    def roll(self):
        result = self.index
        self.total_rolls += 1
        self.index += 1
        if self.index > 100:
            self.index %= 100
        return result


class Player:
    def __init__(self, position=1):
        self.position = position
        self.score = 0

    def move(self, distance):
        self.position += distance
        self.position %= 10
        if self.position == 0:
            self.position = 10
        self.score += self.position


def play_game(positions=[]):
    players = []
    if positions:
        for position in positions:
            players.append(Player(position))
    else:
        players = [Player(), Player()]

    turn = 0
    dice = Dice()
    while max(players, key=lambda p: p.score).score < 1000:
        players[turn % 2].move(dice.roll_x(3))
        p = players[turn % 2]
        # print(f"Turn {turn}, rolls: {dice.total_rolls}\n   p{turn % 2}, @{p.position} - {p.score}")
        turn += 1
    part_one = dice.total_rolls * min(players, key=lambda p: p.score).score
    print(f'GAME OVER: SCORE {part_one}')
    return part_one


def split_universe(player, roll):
    out = {}
    for state in player:
        new_position = state[0] + roll
        new_position %= 10
        if new_position == 0:
            new_position = 10
        if (new_position, state[1]) in out:
            out[(new_position, state[1])] += player[state]
        else:
            out[(new_position, state[1])] = player[state]
    return out


def update_scores(player):
    out = {}
    for state in player:
        new_score = state[0] + state[1]
        out[(state[0], new_score)] = player[state]
    return out


def merge(u1, u2):
    out = u1.copy()
    for state in u2:
        if state in out:
            out[state] += u2[state]
        else:
            out[state] = u2[state]
    return out


def check_victory(player, name):
    win = max(player.keys(), key=lambda state: state[1])[1] >= 21
    total = 0
    if win:
        winning_states = {state: v for state, v in player.items() if state[1] >= 21}
        total = sum(winning_states.values())
        print(name, 'Universal victory achieved: ', total)
    return total


def play_quantum_game(positions):
    players = [
        {
            (positions[0], 0): 1
        },
        {
            (positions[1], 0): 1
        }
    ]

    turn = 0
    player_one_victory = 0
    player_two_victory = 0

    while not player_one_victory or not player_two_victory:
        for _ in range(0, 3):
            player = players[turn % 2]
            u1 = split_universe(player, 1)
            u2 = split_universe(player, 2)
            u3 = split_universe(player, 3)
            players[turn % 2] = merge(merge(u1, u2), u3)

        players[turn % 2] = update_scores(players[turn % 2])
        players[(turn + 1) % 2] = {k: v * 27 for (k, v) in players[(turn + 1) % 2].items()}

        # Win Condition
        if not player_one_victory:
            player_one_victory = check_victory(players[0], "Player 1")
        if not player_two_victory:
            player_two_victory = check_victory(players[1], "Player 2")
        turn += 1


test_dice = Dice()
assert test_dice.roll_x(3) == 1 + 2 + 3
assert test_dice.roll_x(3) == 4 + 5 + 6
assert test_dice.roll_x(3) == 7 + 8 + 9
test_player = Player(position=7)
test_player.move(5)
assert test_player.position == 2
assert test_player.score == 2

assert play_game(positions=[4, 8]) == 739785
print("PART 1")
play_game(positions=[4, 5])

print("Part 2")
assert play_quantum_game(positions=[4, 8]) == 444356092776315
play_quantum_game(positions=[4, 5])
