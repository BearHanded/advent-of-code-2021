ENERGY = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}
TARGETS = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8,
}
ROOMS = [2, 4, 6, 8]
TEST =      ['.', '.', 'BA', '.', 'CD', '.', 'BC', '.', 'DA', '.', '.']
INPUT =     ['.', '.', 'AD', '.', 'CA', '.', 'BD', '.', 'CB', '.', '.']
VICTORY =   ['.', '.', 'AA', '.', 'BB', '.', 'CC', '.', 'DD', '.', '.']
BIG_TEST =  ['.', '.', 'BDDA', '.', 'CCBD', '.', 'BBAC', '.', 'DACA', '.', '.']
BIG_INPUT = ['.', '.', 'ADDD', '.', 'CCBA', '.', 'BBAD', '.', 'CACB', '.', '.']
BIG_VICTORY =   ['.', '.', 'AAAA', '.', 'BBBB', '.', 'CCCC', '.', 'DDDD', '.', '.']


def room_valid(rooms, piece, endpoint):
    return len(rooms[endpoint]) == rooms[endpoint].count('.') + rooms[endpoint].count(piece)


def possible(rooms, idx, endpoint):
    path = [idx, endpoint]
    path.sort()
    for i in range(path[0], path[1] + 1):
        if i == idx or i in ROOMS:
            continue
        if rooms[i] != '.':
            return False
    return True


def explore(rooms, idx):
    piece = rooms[idx]
    # Corridors
    if idx not in ROOMS:
        if possible(rooms, idx, TARGETS[piece]) and room_valid(rooms, piece, TARGETS[piece]):
            return [TARGETS[piece]]
        return []
    # Rooms
    piece = get_piece(piece)
    if idx == TARGETS[piece] and room_valid(rooms, piece, idx):
        return []
    all_paths = []
    for endpoint in range(len(rooms)):
        if endpoint == idx or (endpoint in ROOMS and TARGETS[piece] != endpoint):  # current or not a goal
            continue
        if TARGETS[piece] == endpoint and not room_valid(rooms, piece, endpoint):  # room occupied
            continue
        if possible(rooms, idx, endpoint):
            all_paths.append(endpoint)
    return all_paths


def move(rooms, idx, path):
    new_state = rooms[:]
    d = 0
    piece = get_piece(rooms[idx])
    # Leave Room
    if len(rooms[idx]) == 1:
        new_state[idx] = '.'
    else:
        new_room = ''
        found = False
        for c in rooms[idx]:
            if c == '.':
                d += 1
                new_room += c
            elif not found:
                new_room += '.'
                d += 1
                found = True
            else:
                new_room += c
        new_state[idx] = new_room

    d += abs(idx - path)
    # Enter space
    if len(rooms[path]) == 1:  # Hallway
        new_state[path] = piece
        return new_state, d * ENERGY[piece]
    else:  # Room
        new_state[path], offset = add(piece, rooms[path])
        d += offset
        return new_state, d * ENERGY[piece]


def add(piece, room):
    room = list(room)
    offset = room.count('.')
    room[offset - 1] = piece
    return ''.join(room), offset


def get_piece(room):
    for char in room:
        if char != '.':
            return char
    return None


def solve(rooms, victory_condition=VICTORY):
    print("\nSOLVING: ", rooms, "\n----------")
    states = {tuple(rooms): 0}
    journey = {tuple(rooms): []}

    queued = [rooms]
    while queued:
        state = queued.pop()
        for idx, room in enumerate(state):
            if get_piece(room) is None:
                continue
            paths = explore(state, idx)
            for path in paths:
                new_state, cost = move(state, idx, path)
                key = tuple(new_state)
                cost += states[tuple(state)]
                if key not in states or (key in states and cost < states[key]):
                    states[key] = cost
                    queued.append(new_state)
                    if key not in journey:
                        journey[key] = []
                    new_journey = journey[tuple(state)].copy()
                    new_journey.append(state)
                    journey[key] = new_journey

    victory_cost = states[tuple(victory_condition)]
    solution = journey[tuple(victory_condition)]
    for i in solution:
        print(i, states[tuple(i)])
    print(victory_condition, victory_cost)
    return victory_cost


assert get_piece('.') is None
assert get_piece('..') is None
assert get_piece('AB') == 'A'
assert get_piece('.B') == 'B'
assert room_valid(['.', '.', 'A.', '.', 'BB', '.', 'CC', '.', 'DD', '.', '.'], 'A', 2) is True
assert room_valid(['.', '.', 'A.', '.', 'BB', '.', 'CC', '.', 'DD', '.', '.'], 'B', 2) is False

# Move tests
move_test_rooms, move_test_cost = move(['.', '.', '.A', '.', 'BB', '.', 'CC', '.', 'DD', '.', '.'], 2, 3)
assert move_test_rooms == ['.', '.', '..', 'A', 'BB', '.', 'CC', '.', 'DD', '.', '.']
assert move_test_cost == 3

move_test_rooms, move_test_cost = move(['.', '.', 'AB', '.', 'BB', '.', 'CC', '.', 'DD', '.', '.'], 2, 0)
assert move_test_rooms == ['A', '.', '.B', '.', 'BB', '.', 'CC', '.', 'DD', '.', '.']
assert move_test_cost == 3

move_test_rooms, move_test_cost = move(['B', '.', 'AA', '.', '..', 'B', 'CC', '.', 'DD', '.', '.'], 0, 4)
assert move_test_rooms == ['.', '.', 'AA', '.', '.B', 'B', 'CC', '.', 'DD', '.', '.']
assert move_test_cost == 6 * 10

test_idx = 2
assert TARGETS['A'] == test_idx and test_idx in ROOMS
assert solve(TEST, VICTORY) == 12521
solve(INPUT)
assert solve(BIG_TEST, BIG_VICTORY) == 44169
solve(BIG_INPUT, BIG_VICTORY)
