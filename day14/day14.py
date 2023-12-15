from day14data import test as inp

inp = [list(s) for s in inp.split('\n')]


def move_stone_north(stone_i, stone_j, inp):
    # print(inp[stone_i - 1][stone_j] )
    while stone_i - 1 >= 0 and inp[stone_i - 1][stone_j] != '#' and inp[stone_i - 1][stone_j] != 'O':
        inp[stone_i - 1][stone_j] = 'O'
        inp[stone_i][stone_j] = '.'
        stone_i -= 1


def move_stone_west(stone_i, stone_j, inp):
    while stone_j - 1 >= 0 and inp[stone_i][stone_j - 1] != '#' and inp[stone_i][stone_j - 1] != 'O':
        inp[stone_i][stone_j - 1] = 'O'
        inp[stone_i][stone_j] = '.'
        stone_j -= 1


def move_stone_south(stone_i, stone_j, inp):
    while stone_j + 1 < len(inp) and inp[stone_i][stone_j + 1] != '#' and inp[stone_i][stone_j + 1] != 'O':
        inp[stone_i][stone_j + 1] = 'O'
        inp[stone_i][stone_j] = '.'
        stone_j += 1


def move_stone_east(stone_i, stone_j, inp):
    while stone_i + 1 < len(inp) and inp[stone_i + 1][stone_j] != '#' and inp[stone_i + 1][stone_j] != 'O':
        inp[stone_i + 1][stone_j] = 'O'
        inp[stone_i][stone_j] = '.'
        stone_i += 1


for times in range(1000000000):
    for i, line in enumerate(inp):
        for j, stone in enumerate(line):
            # print(i, j, stone)
            if stone == 'O':
                # print('stone')
                # print(i,j)
                move_stone_north(i, j, inp)
                move_stone_west(i,j,inp)
                move_stone_south(i,j,inp)
                move_stone_east(i,j,inp)

sum = 0
i = len(inp)
for line in inp:
    print(line.count('O') * i)
    sum += line.count('O') * i
    # print(''.join(line))
    i -= 1

print(sum)
