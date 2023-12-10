import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

from day10data import data as inp

maze = [[tile for tile in line] for line in inp.split('\n')]
starting_point = (0, 0)
shadow_maze = [['.' for tile in line] for line in maze]
# #| is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

my_dict = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
    ".": [(0, 0), (0, 0)],
    "O": [(0, 0), (0, 0)],
    "I": [(0, 0), (0, 0)],
    "S": [(0, 0), (0, 0)]
}


class Tile:
    def __init__(self, coordinates: (int, int), tile_type: str):
        self.type = tile_type
        self.coordinates = coordinates
        self.offsets = my_dict[tile_type]
        self.is_start = True if tile_type == "S" else False

        self.directions = {
            (coordinates[0] + self.offsets[0][0], coordinates[1] + self.offsets[0][1]): (
                coordinates[0] + self.offsets[1][0], coordinates[1] + self.offsets[1][1]),
            (coordinates[0] + self.offsets[1][0], coordinates[1] + self.offsets[1][1]): (
                coordinates[0] + self.offsets[0][0], coordinates[1] + self.offsets[0][1])
        }

    def get_direction(self, coming_from: (int, int)) -> (int, int):
        return self.directions[coming_from]


def map_objects():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            tile_symbol = maze[i][j]
            if tile_symbol == "S":
                global starting_point
                starting_point = (i, j)
            maze[i][j] = Tile((i, j), tile_symbol)


def walk_maze_puzzle_a():
    map_objects()
    steps = 1

    actual_tile = maze[starting_point[0] + 1][starting_point[1]]
    coming_from_coordinates = starting_point
    going_to_coordinates = actual_tile.get_direction(coming_from_coordinates)
    shadow_maze[actual_tile.coordinates[0]][actual_tile.coordinates[1]] = actual_tile.type

    while True:
        steps += 1
        coming_from_coordinates = actual_tile.coordinates
        actual_tile: Tile = maze[going_to_coordinates[0]][going_to_coordinates[1]]
        shadow_maze[actual_tile.coordinates[0]][actual_tile.coordinates[1]] = actual_tile.type
        if actual_tile.is_start:
            break
        going_to_coordinates = actual_tile.get_direction(coming_from_coordinates)

    farthest_away = steps // 2

    print("farthest away: ", farthest_away)


walk_maze_puzzle_a()


def my_flood_fill(tile_coordinates, maze_to_flood):
    empty_tiles = [tile_coordinates]
    while empty_tiles:
        tile = empty_tiles.pop()
        if maze_to_flood[tile[0]][tile[1]] == '.' or maze_to_flood[tile[0]][tile[1]] == ' ':
            maze_to_flood[tile[0]][tile[1]] = 'X'
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if 0 <= tile[0] + i < len(maze_to_flood) and 0 <= tile[1] + j < len(maze_to_flood[0]):
                    tile_symbol = maze_to_flood[tile[0] + i][tile[1] + j]
                    if tile_symbol == '.' or tile_symbol == " ":
                        empty_tiles.append((tile[0] + i, tile[1] + j))


def stretch_maze():
    x = []

    # wider:
    for i, line in enumerate(shadow_maze):

        wider_line = []
        taller_line = []
        for j, tile in enumerate(line):
            if tile == ' ':
                wider_line.append(' ')
                wider_line.append(' ')
                taller_line.append(' ')
                taller_line.append(' ')
            if tile == 'S':
                wider_line.append('S')
                wider_line.append(' ')
                taller_line.append('|')
                taller_line.append('|')

            if tile == '-':
                wider_line.append('-')
                wider_line.append('-')
                taller_line.append(' ')
                taller_line.append(' ')

            if tile == '|':
                if (shadow_maze[i][j + 1] == '|'
                        or shadow_maze[i][j + 1] == 'L'
                        or shadow_maze[i][j + 1] == 'F'
                        or shadow_maze[i][j + 1] == '.'):
                    wider_line.append('|')
                    wider_line.append(' ')
                    taller_line.append('|')
                    taller_line.append(' ')
                else:
                    wider_line.append('|')
                    wider_line.append(shadow_maze[i][j + 1])
                    taller_line.append('|')
                    taller_line.append(shadow_maze[i][j + 1])

            if tile == 'L':
                wider_line.append('L')
                wider_line.append('-')
                taller_line.append(' ')
                taller_line.append(' ')

            if tile == 'F':
                wider_line.append('F')
                wider_line.append('-')
                taller_line.append('|')
                taller_line.append(' ')

            if tile == 'J':
                wider_line.append('J')
                wider_line.append(' ')
                taller_line.append(' ')
                taller_line.append(' ')

            if tile == '7':
                wider_line.append('7')
                wider_line.append(' ')
                taller_line.append('|')
                taller_line.append(' ')

            if tile == '.':
                wider_line.append('.')
                wider_line.append(' ')
                taller_line.append(' ')
                taller_line.append(' ')
        x.append(wider_line)
        x.append(taller_line)
    return x


def puzzle_b():
    x = stretch_maze()
    for i, line in enumerate(x):
        for j, tile in enumerate(line):
            if i == 0 or j == 0 or i == len(x) - 1 or j == len(x[0]) - 1:
                my_flood_fill((i, j), x)
    for y in x:
        print(''.join(y))
    dots = 0
    for line in x:
        for y in line:
            if y == '.':
                dots += 1
    print(dots)

    data = np.array(x)
    unique_chars, matrix = np.unique(data, return_inverse=True)
    color_dict = {
        '.': 'yellow',
        'X': 'black',
        ' ': 'white',
        '|': 'brown',
        '-': 'brown',
        'F': 'brown',
        'L': 'brown',
        'J': 'brown',
        '7': 'brown',
        'S': 'red'
    }
    plt.matshow(matrix.reshape(data.shape), cmap=ListedColormap([color_dict[char] for char in unique_chars]))
    plt.xticks(np.arange(data.shape[1]), np.arange(data.shape[1]) + 1)
    plt.yticks(np.arange(data.shape[0]), np.arange(data.shape[0]) + 1)
    plt.savefig('plot.png', dpi=300)
    plt.show()


puzzle_b()
