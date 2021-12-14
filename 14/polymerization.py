from util import christmas_input

FILE = './test_input.txt'


def add_queued_elements(elements, queue):
    result = [None]*(len(elements)+len(queue))
    result[::2] = elements
    result[1::2] = queue
    return result


def polymerize(elements, rules, steps=10):
    max_key_size = 2
    for i in range(steps):
        new_elements = ''
        operable_string = ''.join(elements)
        while len(operable_string) > 1:
            restart = False
            for idx in range(len(elements)):
                end_range = min(len(elements)+1, idx + max_key_size)
                for end_idx in reversed(range(idx + 1, end_range)):
                    compound = operable_string[idx:end_idx + 1]
                    if compound in rules:
                        result = rules[compound]
                        operable_string = operable_string[idx+1:]
                        new_elements += result
                        restart = True
                        break
                if restart is True:
                    break
        new_elements += operable_string # add last character back

        print("step:", i + 1)
        if steps <= 10:
            print("".join(new_elements))

        # Save new rules
        for x in range(len(elements) - 1):
            for y in range(x+1+i, len(elements)+1):
                rules[''.join(elements[x:y+1])] = ''.join(new_elements[2*x:2*y])
        max_key_size = len(new_elements)
        elements = new_elements

    return elements


def analyze(elements):
    res = {i: elements.count(i) for i in set(elements)}
    v = list(res.values())
    print(max(v) - min(v))

# Parse
rows = christmas_input.file_to_array(FILE)
instruction_break = rows.index('')
template = rows[:instruction_break][0]
print(template)
rules = {pair[0]: pair[0][0] + pair[1] for pair in [row.split(" -> ") for row in rows[instruction_break+1:]]}
print(rules)

final_results = polymerize(template, rules)
analyze(final_results)

print("Part 2 begin:")
# final_results = polymerize(template, rules, steps=40)
# analyze(final_results)