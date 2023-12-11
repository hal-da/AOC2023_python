from day11data import data as inp

# A too high: 9615316 CORRECT: 9605127
# B 458191688761

inp = [[field for field in line] for line in inp.split('\n')]


def compute_steps(star_1: (int, int), star_2: (int, int)) -> int:
    x = star_1[0] - star_2[0] if star_1[0] > star_2[0] else star_2[0] - star_1[0]
    y = star_1[1] - star_2[1] if star_1[1] > star_2[1] else star_2[1] - star_1[1]
    return x + y


def get_empty_cols(universe: list) -> list:
    empty_cols = []
    for i, row in enumerate(universe):
        col_is_empty = True
        for j, col in enumerate(row):
            if universe[j][i] == '#':
                col_is_empty = False
                break
        if col_is_empty:
            empty_cols.append(i)
    return empty_cols


def get_stars_coordinates(universe, expansion_rate):
    stars = []
    empty_cols = get_empty_cols(universe)
    above = 0
    for i, line in enumerate(universe):
        line_is_empty = True
        for j, star in enumerate(line):
            if star == '#':
                line_is_empty = False
                before_multiplier = len([c for c in empty_cols if c < j])
                if expansion_rate == 1:
                    stars.append((i+above*expansion_rate, j+expansion_rate*before_multiplier))
                else:
                    stars.append((i+above*expansion_rate-above, j+expansion_rate*before_multiplier-before_multiplier))
        if line_is_empty:
            above += 1
    return stars


def p(expansion_rate):
    my_stars = get_stars_coordinates(inp, expansion_rate)
    my_sum = 0
    while len(my_stars) > 0:
        star = my_stars.pop(0)
        for star2 in my_stars:
            my_sum += compute_steps(star, star2)
    print(my_sum)


p(1)
p(1000000)
