from input_parser import get_puzzle_input
from copy import deepcopy


def make_turn(character, direction):
    facing = character['facing']

    if direction == 'R':
        if facing == 'R':
            facing = 'D'
        elif facing == 'D':
            facing = 'L'
        elif facing == 'L':
            facing = 'U'
        elif facing == 'U':
            facing = 'R'

    elif direction == 'L':
        if facing == 'R':
            facing = 'U'
        elif facing == 'D':
            facing = 'R'
        elif facing == 'L':
            facing = 'D'
        elif facing == 'U':
            facing = 'L'
    character.update({'facing': facing})
    return character


def take_step(character, monkey_map):
    row = character['row']
    column = character['column']
    facing = character['facing']
    new_row = row
    new_column = column
    # print(facing)

    if facing == 'R':
        new_column += 1
        if new_column == len(monkey_map[row]):
            new_column = 0
        while monkey_map[new_row][new_column] == ' ':
            new_column += 1
            if new_column == len(monkey_map[row]):
                new_column = 0
        if monkey_map[row][new_column] == '#':
            new_column = column

    # continue implementing
    elif facing == 'L':
        new_column -= 1
        if new_column == -1:
            new_column = len(monkey_map[row])-1
        while monkey_map[new_row][new_column] == ' ':
            new_column -= 1
            if new_column == -1:
                new_column = len(monkey_map[row])-1
        if monkey_map[row][new_column] == '#':
            new_column = column

    elif facing == 'U':
        new_row -= 1

        if new_row == -1:
            new_row = len(monkey_map)-1
        #print(len(monkey_map[row]), len(monkey_map[new_row]))
        while monkey_map[new_row][new_column] == ' ':
            new_row -= 1
            if new_row == -1:
                new_row = len(monkey_map)-1
        if monkey_map[new_row][new_column] == '#':
            new_row = row

    elif facing == 'D':
        new_row += 1

        if new_row == len(monkey_map):
            new_row = 0
        while monkey_map[new_row][new_column] == ' ':
            new_row += 1
            if new_row == len(monkey_map):
                new_row = 0
        if monkey_map[new_row][new_column] == '#':
            new_row = row
    character.update({'row': new_row, 'column': new_column})
    return character


def draw_map_state(character, monkey_map):
    map_copy = deepcopy(monkey_map)

    facing = character['facing']
    facing_sign = ''

    if character['facing'] == 'R':
        facing_sign = '>'
    elif character['facing'] == 'L':
        facing_sign = '<'
    elif character['facing'] == 'U':
        facing_sign = '^'
    elif character['facing'] == 'D':
        facing_sign = 'v'

    map_copy[character['row']] = map_copy[character['row']][:character['column']] + \
        facing_sign+map_copy[character['row']][character['column']+1:]

    for row in map_copy:
        print(row)
    print('\n\n')


monkey_directions = get_puzzle_input('input.txt')

monkey_map = []
directions = ''
max_map_len = 0
for direction in monkey_directions:
    if '.' in direction:
        monkey_map.append(direction)
        if len(direction) > max_map_len:
            max_map_len = len(direction)
    if 'R' in direction:
        directions = direction

for i in range(len(monkey_map)):
    row = monkey_map[i]
    while len(row) < max_map_len:
        row += ' '

    monkey_map[i] = row
    print(row)
    print(len(row))
# print(directions)

starting_column = monkey_map[0].find('.')

character = {'facing': 'R', 'row': 0, 'column': starting_column}

direct = []
split_directions = directions.split('R')
for direction in split_directions:
    if direction == '':
        direct.append('R')
    else:
        while direction.startswith('L'):
            direct.append('L')
            direction = direction[1:]

        l_buffer = []

        while direction.endswith('L'):
            l_buffer.append('L')
            direction = direction[:-1]

        if 'L' in direction:

            split_dir = direction.split('L')

            for d in split_dir:
                direct.append(d)
                direct.append('L')
            if not direction.endswith('L') and direct[len(direct)-1] == 'L':
                direct = direct[:-1]

        else:
            direct.append(direction)

        direct.extend(l_buffer)
        direct.append('R')

if not directions.endswith('R') and direct[len(direct)-1] == 'R':
    direct = direct[:-1]
# print(direct)

for direction in direct:
    if direction.isnumeric():
        for i in range(int(direction)):
            character = take_step(character, monkey_map)
    else:
        character = make_turn(character, direction)
    # print(direction)
    #draw_map_state(character, monkey_map)

draw_map_state(character, monkey_map)

facing_code = 0

if character['facing'] == 'R':
    facing_code = 0
elif character['facing'] == 'L':
    facing_code = 2
elif character['facing'] == 'U':
    facing_code = 3
elif character['facing'] == 'D':
    facing_code = 1

print(character)
password = 1000 * (1+character['row']) + 4 * (1+character['column']) + facing_code

print('The password is: '+str(password))
