from util import christmas_input
import copy

FILE = './test_input.txt'


class Compound:
    def __init__(self, name, result):
        self.results = [name[0] + result, result + name[1]]
        self.count = 0


def populate(elements, rule_dict):
    for idx, elem in enumerate(elements):
        if idx + 1 >= len(elements):
            break
        pair = elem + elements[idx+1]
        rule_dict[pair].count += 1


def print_rules(rule_dict):
    print("-------")
    for k in rule_dict:
        print(k, rule_dict[k].count, rule_dict[k].results)


def polymerize(rules_dict, steps=10):
    for i in range(steps):
        print("Step", i+1)
        updated_rules = copy.deepcopy(rules_dict)  # make sure none of the updates cascade into each other
        for k in rules_dict:
            # add to results for each entry
            count = rules_dict[k].count
            if count > 0:
                for result in rules_dict[k].results:
                    updated_rules[result].count += count
                updated_rules[k].count -= count # removes itself
        rules_dict = updated_rules

    return rules_dict


def analyze(rules_dict, start, end):
    char_counts = {}
    for k in rules_dict:
        count = rules_dict[k].count / 2
        if k[0] in char_counts:
            char_counts[k[0]] += count
        else:
            char_counts[k[0]] = count
        if k[1] in char_counts:
            char_counts[k[1]] += count
        else:
            char_counts[k[1]] = count
    # fix ends of the string
    char_counts[start] += 0.5
    char_counts[end] += 0.5
    print(char_counts)
    # res = {i: elements.count(i) for i in set(elements)}
    v = list(char_counts.values())
    print(max(v) - min(v))


# Parse
rows = christmas_input.file_to_array(FILE)
instruction_break = rows.index('')
template = rows[:instruction_break][0]
print(template)
rules = {pair[0]: Compound(pair[0], pair[1]) for pair in [row.split(" -> ") for row in rows[instruction_break+1:]]}
populate(template, rules)

final_results = polymerize(rules)
analyze(final_results, template[0], template[-1])

print("Part 2 begin:")
final_results = polymerize(rules, steps=40)
analyze(final_results, template[0], template[-1])