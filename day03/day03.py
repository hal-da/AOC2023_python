from day03input import inp as inp

# puzzle a: wrong, too high: 620348 , too low: 532162, 515396 - correct: 535235

arr = inp.strip().split('\n')
total_sum = 0


def get_adjacent_nums(i, j, visited, puzzle_typ):
    nums = []
    for k in range(-1, 2):
        m = i + k
        for x in range(-1, 2):
            n = j + x
            if (m, n) in visited:
                continue
            if 0 <= m < len(arr) and 0 <= n < len(arr[0]):
                num = str(arr[m][n])
                if num.isnumeric():
                    z = n - 1
                    # walk left
                    if 0 <= z < len(arr):
                        left_possible_num = arr[m][z]
                        while 0 <= z < len(arr) and left_possible_num.isnumeric():
                            num = left_possible_num + num
                            visited.append((m, z))
                            z = z - 1
                            left_possible_num = arr[m][z]
                    # walk right
                    z = n + 1
                    if 0 <= z < len(arr):
                        right_possible_num = arr[m][z]
                        while 0 <= z < len(arr) and right_possible_num.isnumeric():
                            num = num + right_possible_num
                            visited.append((m, z))
                            z = z + 1
                            if z >= len(arr):
                                continue
                            right_possible_num = arr[m][z]
                    nums.append(int(num))
    if puzzle_typ == 'a':
        return nums
    if len(nums) != 2:
        return 0
    return nums[0] * nums[1]


def puzzle_a():
    total_nums = []
    visited = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            cell = arr[i][j]
            if cell != "." and (not cell.isnumeric()):
                total_nums += get_adjacent_nums(i, j, visited, 'a')
    print(sum(total_nums))


def puzzle_b():
    total_nums = 0
    visited = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "*":
                total_nums += get_adjacent_nums(i, j, visited, 'b')
    print(total_nums)


puzzle_a()

puzzle_b()
