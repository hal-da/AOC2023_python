from day05data import inp as inp

input_map = inp.split('\n\n')

# CORRECT A: 1181555926
# WRONG _B: 0, 37466397, 6683080


input_map = [m.split(':') for m in input_map]
seeds = input_map.pop(0)[1].strip().split(' ')


def get_mapping(arr: [], src: int) -> int:
    for nums in arr:
        if nums[1] <= src <= nums[1] + nums[2]:
            return src + nums[0] - nums[1]
    return src


def puzzle_a():
    mapped_seeds = []
    my_arr = []
    for z in input_map:
        string = [[int(s) for s in s.split(' ')] for s in z[1].strip().split('\n')]
        my_arr.append(string)

    for seed in seeds:
        for to_map in my_arr:
            print(to_map)
            seed = get_mapping(to_map, int(seed))
        mapped_seeds.append(seed)
    print(min(mapped_seeds))


def get_maps(map_arr, seed_map, mapped_seeds):
    # print(map_arr, " die verschiebungen")
    # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", seed_map, mapped_seeds)
    lower_seed_bound = seed_map[0]
    upper_seed_bound = seed_map[1]
    # print(seed_map, " die seeds")
    # print(lower_seed_bound, " lower seed bound ", upper_seed_bound, " upper seed bound")
    for shift_arr in map_arr:
        # print("shift_arr: ", shift_arr)
        lower_bound = shift_arr[1]
        upper_bound = shift_arr[1] + shift_arr[2] - 1
        # print(lower_bound, lower_seed_bound, " L")
        # print(upper_bound, upper_seed_bound, " U")
        shift = shift_arr[0] - shift_arr[1]
        if lower_bound < lower_seed_bound and upper_bound > upper_seed_bound:
            # print("NEUE BOUNDS um ", shift)
            mapped_seeds.append([lower_seed_bound + shift, upper_seed_bound + shift])
            return

        if lower_seed_bound < lower_bound < upper_seed_bound < upper_bound:
            no_shift_seeds = [lower_seed_bound, lower_bound]
            get_maps(map_arr, no_shift_seeds, mapped_seeds)
            shifted_seeds = [lower_bound + shift, upper_seed_bound + shift]
            mapped_seeds.append(shifted_seeds)
            # print(lower_bound, lower_seed_bound, " L")
            # print(upper_bound, upper_seed_bound, " U")
            # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            # print("lower seed bound: ", lower_seed_bound, " upper seed bound", upper_seed_bound, "lower bound ",
            #       lower_bound, " upper bound: ", upper_bound)
            # print("no shift seeds: ", no_shift_seeds)
            # print("shifted seeds: ", shifted_seeds, " waren ", lower_bound, " plus shift", shift)

        if lower_bound < lower_seed_bound < upper_bound < upper_seed_bound:
            no_shift_seeds = [upper_bound, upper_seed_bound]

            get_maps(map_arr, no_shift_seeds, mapped_seeds)
            shifted_seeds = [lower_seed_bound + shift, upper_bound + shift]
            mapped_seeds.append(shifted_seeds)

            # print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
            # print("lower seed bound: ", lower_seed_bound, " upper seed bound", upper_seed_bound, "lower bound ",
            #       lower_bound, " upper bound: ", upper_bound)
            # print("no shift seeds: ", no_shift_seeds)
            # print("shifted seeds: ", shifted_seeds, " waren ", lower_bound, " plus shift", shift)
            continue

        if lower_seed_bound < lower_bound and upper_seed_bound > upper_bound:
            lower_no_shift_seeds = [lower_seed_bound, lower_bound]
            upper_no_shift_seeds = [upper_bound, upper_seed_bound]
            shift_seeds = [lower_bound + shift, upper_bound + shift]
            get_maps(map_arr, lower_no_shift_seeds, mapped_seeds)
            get_maps(map_arr, upper_no_shift_seeds, mapped_seeds)
            mapped_seeds.append(shift_seeds)
            # print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
            # print("lower seed bound: ", lower_seed_bound, " upper seed bound", upper_seed_bound, "lower bound ",
            #       lower_bound, " upper bound: ", upper_bound)
            # print("no shift seeds: ", lower_no_shift_seeds, " und ", upper_no_shift_seeds)
            # print("shifted seeds: ", shift_seeds, " waren ", lower_bound, " plus shift", shift)
            return
    mapped_seeds.append(seed_map)


def puzzle_b_naive():
    seed_range = [[] for _ in range(8)]
    for i in range(len(seeds)):
        if i % 2 == 0:
            seed_range[0].append([int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]) - 1])

    shift_maps = [[z for z in z[1].split('\n') if z] for z in input_map]
    shift_maps = [[[int(i) for i in a.split(" ")] for a in arr] for arr in shift_maps]

    for i, shift_map in enumerate(shift_maps):
        new_pairs = []
        for pair in seed_range[i]:
            get_maps(shift_map, pair, new_pairs)
        if i < len(seed_range):
            seed_range[i + 1] += new_pairs
    print(seed_range)

    lowest = 99999999999999999999999999999999999999

    for x in seed_range:
        for y in x:
            for z in y:
                if z < lowest:
                    lowest = z

    print(lowest)
    # print(seed_range)


# puzzle_b()
# puzzle_a()


puzzle_b_naive()
