from day02input import inp as inp

# day1 a
# only 12 red cubes, 13 green cubes, and 14 blue cubes

max_colors = {
    "blue": 14,
    "red": 12,
    "green": 13
}

def count_colors(cube_arr):
    game_no = cube_arr[0].split(' ')[1]
    games = cube_arr[1].strip().split("; ")
    moves = [game.split(', ') for game in games]
    for m in moves:
        for x in m:
            amount_color = x.split(' ')
            amount = amount_color[0]
            color = amount_color[1]
            if int(amount) > max_colors[color]:
                return 0
    return int(game_no)


def get_smallest_color(cube_arr):
    games = cube_arr[1].strip().split("; ")
    moves = [game.split(', ') for game in games]
    min_colors = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for m in moves:
        for x in m:
            amount_color = x.split(' ')
            amount = int(amount_color[0])
            color = amount_color[1]
            if amount > min_colors[color]:
                min_colors[color] = amount

    multi = 1
    for v in min_colors.values():
        multi *= v
    return multi


print(sum([count_colors(line.split(':')) for line in inp.split('\n')]))
print(sum([get_smallest_color(line.split(':')) for line in inp.split('\n')]))
