from day06data import inp as inp

inp_b = inp.replace(r"Time: ", "").replace(r"Distance:  ", "").replace(" ", "").split('\n')
inp_a = inp.replace(r"Time: ", "").replace(r"Distance:  ", "").strip().split('\n')


def puzzle_a():
    time = [x for x in inp_a[0].split(" ") if x]
    distance = [x for x in inp_a[1].split(" ") if x]
    ways_to_win = 1

    for i in range(len(time)):
        has_won = 0
        for seconds in range(int(time[i])):
            remaining_time = int(time[i]) - int(seconds)
            max_distance = remaining_time * int(seconds)
            if max_distance > int(distance[i]):
                has_won += 1
        ways_to_win *= has_won
    print(ways_to_win)


def puzzle_b_naive():
    has_won = 0
    time = int(inp_b[0])
    distance = int(inp_b[1])
    for seconds in range(time):
        remaining_time = time - seconds
        max_distance = remaining_time * seconds
        if max_distance > distance:
            has_won += 1
    print(has_won)


puzzle_a()
puzzle_b_naive()
