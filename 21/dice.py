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