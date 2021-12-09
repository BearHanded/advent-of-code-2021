from util import christmas_input

FILE = './test.txt'

char_lookup = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

# Parse
rows = [row.split("|") for row in christmas_input.file_to_array(FILE)]
num_count = 0
for codes in rows:
    output = codes[1].split(" ")
    for display in output[1]:
        if char_lookup[len(display)] in [1, 4, 7, 8]:
            num_count += 1

print(num_count)