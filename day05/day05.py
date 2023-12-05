from day05data import inp as inp

input_map = inp.split('\n\n')

# CORRECT A: 1181555926

input_map = [m.split(':') for m in input_map]
seeds = input_map.pop(0)[1].strip().split(' ')


def get_mapping(string: str, src: int) -> int:
    string = string.strip().split('\n')
    arr = [[int(x) for x in x.split(' ')] for x in string]
    for nums in arr:
        if nums[1] <= src <= nums[1] + nums[2]:
            return src + nums[0] - nums[1]
    return src


def build_map():
    mapped_seeds = []
    for seed in seeds:
        for to_map in input_map:
            seed = get_mapping(to_map[1], int(seed))
        mapped_seeds.append(seed)
    print(min(mapped_seeds))


def puzzle_b_naive():
    lowest_no = 99999999999999999999999999999999999999999
    for i in range(408612163):
        x = i
        for to_map in input_map:
            x = get_mapping(to_map[1], 364807853 + x)
            # print(x)
        if x < lowest_no:
            lowest_no = x

    print(lowest_no)


#build_map()
puzzle_b_naive()

# print(408612163 - 364807853)
