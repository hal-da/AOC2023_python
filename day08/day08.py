from day08data import data as inp
from math import lcm
from re import sub

inp = sub('[ ()]', '', inp)
instructions, directions = [line for line in inp.split('\n\n')]
directions = [[x.strip() for x in l.split('=')] for l in directions.split('\n')]
directions = {x[0]: x[1].split(',') for x in directions}


def puzzle_a():
    current_element = 'AAA'
    target = 'ZZZ'
    moves = 0

    while current_element != target:
        i = moves % len(instructions)
        current_instruction = 0 if instructions[i] == "L" else 1
        current_element = directions[current_element][current_instruction]
        moves += 1

    print(moves)


def puzzle_b():
    current_elements = [x for x in directions.keys() if x[2] == "A"]
    moves = 0
    steps = []
    elements_to_pop = None
    while len(current_elements)>0:
        i = moves % len(instructions)
        moves += 1
        current_instruction = 0 if instructions[i] == "L" else 1
        if elements_to_pop is not None:
            current_elements.pop(elements_to_pop)
            elements_to_pop = None
        for i in range(len(current_elements)):
            current_elements[i] = directions[current_elements[i]][current_instruction]
            if current_elements[i][2] == "Z":
                steps.append(moves)
                elements_to_pop = i
    print(lcm(*steps))


puzzle_a()
# not 16555262546256037897470293 too high ;) - correct: 10151663816849
puzzle_b()
