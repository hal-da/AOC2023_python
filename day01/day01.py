import re
from day01Input import puzzle_input as inp


def day01():
    arr = inp.split('\n')
    my_sum = 0
    for s in arr:
        for i, n in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            s = s.replace(n, n + str(i + 1) + n)
        n = re.findall('\d', s)
        if len(n) > 0:
            d = "".join([str(n[0])] + [str(n[-1])])
        else:
            d = 0
        my_sum += int(d)

    print(my_sum)


day01()
