import math

from util import christmas_input
from util.christmas_input import BColors


def op_input(a, input_val, memory):
    memory[a] = input_val


def op_add(a, b, memory):
    memory[a] = get_value(a, memory) + get_value(b, memory)


def op_multiply(a, b, memory):
    memory[a] = get_value(a, memory) * get_value(b, memory)


def op_divide(a, b, memory):
    out = get_value(a, memory) / get_value(b, memory)
    memory[a] = math.floor(out) if out > 0 else math.ceil(out)


def op_modulo(a, b, memory):
    memory[a] = get_value(a, memory) % get_value(b, memory)


def op_equal(a, b, memory):
    memory[a] = 1 if get_value(a, memory) == get_value(b, memory) else 0


OPERATIONS = {
    'inp': op_input,
    'add': op_add,
    'mul': op_multiply,
    'div': op_divide,
    'mod': op_modulo,
    'eql': op_equal
}
DEBUG = False


def read_file(file_name):
    return christmas_input.file_to_array(file_name)


def get_value(variable, memory):
    if variable in memory:
        return memory[variable]
    return int(variable)


def run(instructions, number):
    memory = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    queue = [int(i) for i in number]
    for instruction in instructions:
        chunks = instruction.split(' ')
        op_code = chunks[0]
        if op_code == 'inp':
            digit = queue.pop(0)
            op_input(chunks[1], digit, memory)
        else:
            operation = OPERATIONS[op_code]
            a = chunks[1]
            b = get_value(chunks[2], memory)
            operation(a, b, memory)
        if DEBUG:
            print("{0:20} {1}{2}{3}".format(instruction, BColors.OKBLUE, memory, BColors.ENDC))
    return memory


def find_number(instructions):
    number = 99999999999999
    floor = 11111111111111
    # options = reversed(range(0, number + 1)
    options = range(11111111111111, number + 1)
    for i in options:
        num_str = str(i)
        if '0' in num_str:
            continue
        memory = run(instructions, num_str)
        success = memory.get('w', 1)
        if success == '0':
            print('MAX =', num_str)
            break
        elif i % 5555 == 0:
            print(i)


part_one = read_file('input.txt')
find_number(part_one)
