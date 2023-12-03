from day03input import test as inp

# puzzle a: wrong, too high: 620348 , too low: 532162, 515396 - correct: 535235

arr = inp.strip().split('\n')


def has_adjacent_symbol(i, j):
    has_symbol = False
    for k in range(-1, 2):
        for x in range(-1, 2):
            if 0 <= (i+k) < len(arr[0]) and 0 <= (j+x) < len(arr[0]):
                possible_symbol = arr[i+k][j+x]
                if possible_symbol != "." and (not possible_symbol.isnumeric()):
                    has_symbol = True
    return has_symbol

# variant does work with test input, not with actual input, maybe visit later again..
def puzzle_a():
    total_sum = 0
    visited = []
    for i in range(len(arr)):
        cell_has_adjacent_symbol = False
        running_num = ""
        for j in range(len(arr[i])):
            cell = arr[i][j]
            if cell.isnumeric():
                running_num += str(cell)
                if not cell_has_adjacent_symbol:
                    cell_has_adjacent_symbol = has_adjacent_symbol(i, j)
                print(running_num, cell_has_adjacent_symbol)
            if not cell.isnumeric():
                print(running_num, cell_has_adjacent_symbol)
                if running_num.isnumeric() and cell_has_adjacent_symbol:
                    total_sum += int(running_num)
                running_num = ""
                cell_has_adjacent_symbol = False
    print(total_sum)


puzzle_a()