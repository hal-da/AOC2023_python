from day09data import data as inp

# correct naive puzzle a: 2043677056, part2: 1062

inp = [[int(y) for y in x.split(' ')] for x in inp.split('\n')]


def part_1():
    all_new_last_digits = []
    for line in inp:
        line = line[::-1]  # PART 2 !!
        digits_before_new_last = line[-1]
        additional = 0
        all_zeros = False
        while not all_zeros:
            diffs = []
            all_zeros = True
            for i in range(len(line) - 1):
                diff = line[i + 1] - line[i]
                diffs.append(diff)
                if diff != 0:
                    all_zeros = False
            additional += diffs[-1]
            line = diffs

        all_new_last_digits.append(digits_before_new_last + additional)
    print(sum(all_new_last_digits))


part_1()
