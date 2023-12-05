from day05data import test as inp

input_map = inp.split('\n\n')

# CORRECT A: 1181555926

input_map = [m.split(':') for m in input_map]
seeds = input_map.pop(0)[1].strip().split(' ')


def get_mapping(arr: [], src: int) -> int:
    for nums in arr:
        if nums[1] <= src <= nums[1] + nums[2]:
            return src + nums[0] - nums[1]
    return src


def build_map():
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


def puzzle_b_naive():
    lowest_no = 99999999999999999
    my_arr = []
    for z in input_map:
        arr = [[int(s) for s in s.split(' ')] for s in z[1].strip().split('\n')]
        my_arr.append(arr)

    for i in range(408612163):
        x = i + 364807853
        for to_map in my_arr:
            x = get_mapping(to_map, x)
        if x < lowest_no:
            lowest_no = x
    print(lowest_no)


def get_mapped(map_arr, seed_map, mapped_seeds):
    # print(map_arr, " die verschiebungen")
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
        if lower_bound <= lower_seed_bound and upper_bound >= upper_seed_bound:
            print("NEUE BOUNDS um ", shift)
            mapped_seeds.append([lower_seed_bound + shift, upper_seed_bound + shift])
            return

        if lower_seed_bound <= lower_bound <= upper_seed_bound <= upper_bound:
            no_shift_seeds = [lower_seed_bound, lower_bound - 1]
            mapped_seeds.append(no_shift_seeds)
            shifted_seeds = [lower_bound + shift, upper_seed_bound + shift]
            mapped_seeds.append(shifted_seeds)
            print(lower_bound, lower_seed_bound, " L")
            print(upper_bound, upper_seed_bound, " U")
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print("lower seed bound: ", lower_seed_bound," upper seed bound", upper_seed_bound, "lower bound ", lower_bound, " upper bound: ", upper_bound)
            print("no shift seeds: ", no_shift_seeds)
            print("shifted seeds: ", shifted_seeds, " waren ", lower_bound, " plus shift", shift)
            return

        if lower_bound <= lower_seed_bound <= upper_bound <= upper_seed_bound:
            no_shift_seeds = [upper_bound + 1, upper_seed_bound]
            mapped_seeds.append(no_shift_seeds)
            shifted_seeds = [lower_seed_bound + shift, upper_bound]
            mapped_seeds.append(shifted_seeds)

            print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
            print("lower seed bound: ", lower_seed_bound, " upper seed bound", upper_seed_bound, "lower bound ",
                  lower_bound, " upper bound: ", upper_bound)
            print("no shift seeds: ", no_shift_seeds)
            print("shifted seeds: ", shifted_seeds, " waren ", lower_bound, " plus shift", shift)
            return

        if lower_seed_bound <= lower_bound and upper_seed_bound >= upper_bound:
            lower_no_shift_seeds = [lower_seed_bound, lower_bound - 1]
            mapped_seeds.append(lower_no_shift_seeds)
            shift_seeds = [lower_bound + shift, upper_bound + shift]
            mapped_seeds.append(shift_seeds)
            upper_no_shift_seeds = [upper_bound+1,upper_seed_bound]
            mapped_seeds.append(upper_no_shift_seeds)
            print("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
            print("lower seed bound: ", lower_seed_bound, " upper seed bound", upper_seed_bound, "lower bound ",
                  lower_bound, " upper bound: ", upper_bound)
            print("no shift seeds: ", lower_no_shift_seeds, " und ", upper_no_shift_seeds)
            print("shifted seeds: ", shift_seeds, " waren ", lower_bound, " plus shift", shift)
            return
        # print(lower_bound, " lower bound", upper_bound, " upper_bound")
    mapped_seeds.append(seed_map)
    # print(" KEINE VERSCHIEBUNG ")


def puzzle_b():
    seed_range = []
    # print(seeds)
    for i in range(len(seeds)):
        if i % 2 == 0:
            seed_range.append([int(seeds[i]), int(seeds[i]) + int(seeds[i + 1]) - 1])

    # print(seed_range)

    shift_maps = [[z for z in z[1].split('\n') if z] for z in input_map]
    shift_maps = [[[int(i) for i in a.split(" ")] for a in arr] for arr in shift_maps]
    # print(my_arr)
    new_seed_pairs = []

    for maps in shift_maps:
        print(maps)
        new_seed_pairs = []
        for seed_pairs in seed_range:
            print(seed_pairs)
            get_mapped(maps, seed_pairs, new_seed_pairs)
            print(new_seed_pairs, " NEW SEED PAIRS IN MAIN FUN")
        print("alle seedpairs abgearbeitet oida")
        # return
        seed_range = new_seed_pairs
    # print(new_seed_pairs)
    lowest = 9999999999999999999999999999

    for p in seed_range:
        for x in p:
            if x < lowest:
                lowest = x
    print(lowest)


puzzle_b()
