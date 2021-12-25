# solve framework from solutions section, got stuck after breaking down the abstracted function
def abstracted_function(params, z, w):
    if (z % 26 + params[1]) != w:
        return z // params[0] * 26 + w + params[2]
    else:
        return z // params[0]


def solve():
    data = [line.split() for line in open("input.txt")]
    params = []
    for i in range(0, 18 * 14, 18):
        p1 = int(data[i + 4][-1])
        p2 = int(data[i + 5][-1])
        p3 = int(data[i + 15][-1])
        params.append((p1, p2, p3))

    possibilities = {0: [0, 0]}
    for i, p in enumerate(params):
        new_options = {}
        for z, inp in possibilities.items():
            for w in range(1, 10):
                new_z = abstracted_function(p, w, z)
                if p[0] == 1 or (p[0] == 26 and new_z < z):
                    if new_z not in new_options:
                        new_options[new_z] = [inp[0] * 10 + w, inp[1] * 10 + w]
                    else:
                        new_options[new_z][0] = min(new_options[new_z][0], inp[0] * 10 + w)
                        new_options[new_z][1] = max(new_options[new_z][1], inp[1] * 10 + w)

        print("Digit:", i + 1, "Tracked values of z:", len(new_options))
        possibilities = new_options

    print("Best valid values:", possibilities[0])

solve()
