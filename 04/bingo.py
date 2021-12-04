from util import christmas_input

FILE = './input.txt'


class BingoTile:
    def __init__(self, value):
        self.value = value  # forward
        self.marked = False


def pretty_board(board):
    for row in board:
        print([tile.value if not tile.marked else "X" for tile in row])
    print("\n")


def apply_bingo_number(board, number):
    for row in board:
        for tile in row:
            if tile.value == number:
                tile.marked = True
                return True
    return False


def check_horizontal_line(board):
    return any([all([tile.marked for tile in row]) for row in board])


def check_win(board):
    if check_horizontal_line(board):
        return True
    rotated = list(zip(*board))
    if check_horizontal_line(rotated):
        return True
    return False


def get_unmarked_total(board):
    total = 0
    for row in board:
        for tile in row:
            if not tile.marked:
                total += tile.value
    return total


# Parse
rows = christmas_input.file_to_array(FILE)
bingo_numbers = [int(x) for x in rows[0].split(",")]
string_boards = [rows[n + 1:n + 6] for n in range(1, len(rows), 6)]
boards = [[[BingoTile(int(x)) for x in row.split()] for row in board] for board in string_boards]

# All boards for fun
boards = [[[BingoTile(int(x)) for x in row.split()] for row in board] for board in string_boards]  # new boards
for number in bingo_numbers:
    board_idx = 0
    wins = []
    for board in boards:
        match = apply_bingo_number(board, number)
        if match and check_win(board):
            wins.append(board_idx)
        board_idx += 1

    for win_idx in wins:  # display in order before removing
        print("Removing board", win_idx, "on number", number)
        print("SCORE: ", number * get_unmarked_total(boards[win_idx]))
        pretty_board(boards[win_idx])
    for win_idx in sorted(wins, reverse=True):  # remove the winning indexes in reverse order, avoid collisions
        del boards[win_idx]
    if len(boards) == 0:
        break
