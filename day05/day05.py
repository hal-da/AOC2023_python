from day05data import inp as inp

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


# build_map()
puzzle_b_naive()

# print(408612163 - 364807853)
