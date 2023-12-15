from day15data import data as inp

inp = inp.split(',')


def compute_hash(s):
    c_sum = 0
    for c in s:
        c_sum += (ord(c))
        c_sum *= 17
        c_sum %= 256
    return c_sum


def p_a():
    sum = 0
    for s in inp:
        sum += compute_hash(s)
    print(sum)


# p_a()


def p_b():
    my_map = {}
    c = 0
    for s in inp:
        try:
            value = int(s[-1])
            k = s[:-2]
            my_hash = compute_hash(k)
            if my_hash not in my_map:
                my_map[my_hash] = {}
            my_map[my_hash][k] = value
        except ValueError:
            k = s[:-1]
            my_hash = compute_hash(k)
            if my_hash not in my_map:
                continue
            if k not in my_map[my_hash]:
                continue
            del my_map[my_hash][k]

    for my_hash in my_map:
        for i, item in enumerate(my_map[my_hash].items()):
            c += (i + 1) * item[1] * (my_hash + 1)

    print(c)


p_b()
