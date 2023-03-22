from input_parser import get_puzzle_input
from copy import deepcopy


class Face:

    def __init__(self, face_nr, face_map, horizontal_offset, vertical_offset, face_dict):
        self.face_nr = face_nr
        self.face_map = face_map
        self.horizontal_offset = horizontal_offset
        self.vertical_offset = vertical_offset
        self.adjacent_faces = face_dict[self.face_nr]

    def get_adjacent_face(self, direction):
        return self.adjacent_faces[direction]

    def get_face_nr(self):
        return self.face_nr

    def get_map(self):
        return self.face_map

    def get_horizontal_offset(self):
        return self.horizontal_offset

    def get_vertical_offset(self):
        return self.vertical_offset


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


def take_step(character, cube):
    cube_face = character['face']
    face_map = cube[cube_face].get_map()

    row = character['row']
    column = character['column']
    facing = character['facing']
    new_row = row
    new_column = column
    new_facing = facing
    new_face = cube_face
    new_map = face_map

    if facing == 'R':
        new_column += 1
        if new_column == len(face_map[row]):
            # switch to another face
            new_face_data = switch_face(character, cube)
            new_row = new_face_data['row']
            new_column = new_face_data['column']
            new_facing = new_face_data['facing']
            new_face = new_face_data['face']
            new_map = new_face_data['map']

        if new_map[new_row][new_column] == '#':
            new_row = row
            new_column = column
            new_facing = facing
            new_face = cube_face

    elif facing == 'L':
        new_column -= 1
        if new_column == -1:
            # switch to another face
            new_face_data = switch_face(character, cube)
            new_row = new_face_data['row']
            new_column = new_face_data['column']
            new_facing = new_face_data['facing']
            new_face = new_face_data['face']
            new_map = new_face_data['map']

        if new_map[new_row][new_column] == '#':
            new_row = row
            new_column = column
            new_facing = facing
            new_face = cube_face

    elif facing == 'U':
        new_row -= 1

        if new_row == -1:
            # switch to another face
            new_face_data = switch_face(character, cube)
            new_row = new_face_data['row']
            new_column = new_face_data['column']
            new_facing = new_face_data['facing']
            new_face = new_face_data['face']
            new_map = new_face_data['map']

        if new_map[new_row][new_column] == '#':
            new_row = row
            new_column = column
            new_facing = facing
            new_face = cube_face

    elif facing == 'D':
        new_row += 1

        if new_row == len(face_map):
            # switch to another face
            new_face_data = switch_face(character, cube)
            new_row = new_face_data['row']
            new_column = new_face_data['column']
            new_facing = new_face_data['facing']
            new_face = new_face_data['face']
            new_map = new_face_data['map']

        if new_map[new_row][new_column] == '#':
            new_row = row
            new_column = column
            new_facing = facing
            new_face = cube_face

    character.update({'row': new_row, 'column': new_column, 'facing': new_facing, 'face': new_face})
    return character


def switch_face(character, cube):
    current_face_nr = character['face']
    current_face = cube[current_face_nr]
    new_face = cube[current_face.get_adjacent_face(character['facing'])]

    new_face_nr = new_face.get_face_nr()
    new_map = new_face.get_map()
    max_map_position = len(new_map)-1

    old_facing = character['facing']
    new_facing = ''

    old_row = character['row']
    old_column = character['column']

    new_row = 0
    new_column = 0

    if current_face_nr == new_face.get_adjacent_face('U'):
        new_facing = 'D'
        new_row = 0

        if old_facing == 'U':
            new_column = max_map_position-old_column
        elif old_facing == 'D':
            new_column = old_column
        elif old_facing == 'L':
            new_column = old_row
        elif old_facing == 'R':
            new_column = max_map_position-old_row

    elif current_face_nr == new_face.get_adjacent_face('D'):
        new_facing = 'U'
        new_row = max_map_position
        if old_facing == 'U':
            new_column = old_column
        elif old_facing == 'D':
            new_column = max_map_position-old_column
        elif old_facing == 'L':
            new_column = max_map_position-old_row
        elif old_facing == 'R':
            new_column = old_row

    elif current_face_nr == new_face.get_adjacent_face('L'):
        new_facing = 'R'
        new_column = 0
        if old_facing == 'U':
            new_row = old_column
        elif old_facing == 'D':
            new_row = max_map_position-old_column
        elif old_facing == 'L':
            new_row = max_map_position-old_row
        elif old_facing == 'R':
            new_row = old_row

    elif current_face_nr == new_face.get_adjacent_face('R'):
        new_facing = 'L'
        new_column = max_map_position
        if old_facing == 'U':
            new_row = max_map_position-old_column
        elif old_facing == 'D':
            new_row = old_column
        elif old_facing == 'L':
            new_row = old_row
        elif old_facing == 'R':
            new_row = max_map_position-old_row

    return {'row': new_row, 'column': new_column, 'facing': new_facing, 'face': new_face_nr, 'map': new_map}


def draw_map_state(character, monkey_map, cube):
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

    map_copy[character['row']+cube[character['face']].get_vertical_offset()] = map_copy[character['row']+cube[character['face']].get_vertical_offset()][:character['column']+cube[character['face']].get_horizontal_offset()] + \
        facing_sign+map_copy[character['row']+cube[character['face']].get_vertical_offset()
                             ][character['column']+cube[character['face']].get_horizontal_offset()+1:]

    for row in map_copy:
        print(row)
    print('\n\n')


input_type = 'standard'

input_def = {'standard': {'file': 'input.txt', 'grid_size': 50, 'grid_layout': {
    '0_1': '1',
    '2_0': '2',
    '1_1': '3',
    '3_0': '4',
    '0_2': '5',
    '2_1': '6'},
    'face_dict': {
    '1': {'U': '4', 'D': '3', 'L': '2', 'R': '5'},
    '2': {'U': '3', 'D': '4', 'L': '1', 'R': '6'},
    '3': {'U': '1', 'D': '6', 'L': '2', 'R': '5'},
    '4': {'U': '2', 'D': '5', 'L': '1', 'R': '6'},
    '5': {'U': '4', 'D': '3', 'L': '1', 'R': '6'},
    '6': {'U': '3', 'D': '4', 'L': '2', 'R': '5'}}
},
    'test': {'file': 'test_input.txt', 'grid_size': 4, 'grid_layout': {
        '0_2': '1',
        '1_1': '2',
        '1_2': '3',
        '1_0': '4',
        '2_3': '5',
        '2_2': '6'

    },
    'face_dict': {
        '1': {'U': '4', 'D': '3', 'L': '2', 'R': '5'},
        '2': {'U': '1', 'D': '6', 'L': '4', 'R': '3'},
        '3': {'U': '1', 'D': '6', 'L': '2', 'R': '5'},
        '4': {'U': '1', 'D': '6', 'L': '5', 'R': '2'},
        '5': {'U': '3', 'D': '4', 'L': '6', 'R': '1'},
        '6': {'U': '3', 'D': '4', 'L': '2', 'R': '5'}}}}

grid_size = input_def[input_type]['grid_size']
grid_layout = input_def[input_type]['grid_layout']
face_dict = input_def[input_type]['face_dict']
monkey_directions = get_puzzle_input(input_def[input_type]['file'])

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

# print(directions)
cube = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None}

split_grid = []

for i in range(int(len(monkey_map)/grid_size)):
    split_grid.append(monkey_map[i*grid_size:i*grid_size+grid_size])

for i in range(len(split_grid)):
    for j in range(int(len(split_grid[i][0])/grid_size)):
        new_face = []
        for k in range(len(split_grid[i])):
            new_face.append(split_grid[i][k][j*grid_size:j*grid_size+grid_size])
        vertical_offset = grid_size*i
        horizontal_offset = grid_size*j

        if grid_layout.get(str(i)+'_'+str(j)) != None:
            print(str(i)+'_'+str(j))
            print(new_face)
            created_face = Face(grid_layout.get(str(i)+'_'+str(j)), new_face,
                                horizontal_offset, vertical_offset, face_dict)
            cube.update({grid_layout.get(str(i)+'_'+str(j)): created_face})


character = {'facing': 'R', 'row': 0, 'column': 0, 'face': '1'}

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

for direction in direct:
    if direction.isnumeric():
        for i in range(int(direction)):
            pass
            character = take_step(character, cube)
    else:
        character = make_turn(character, direction)
    # print(direction)
    #draw_map_state(character, monkey_map, cube)

draw_map_state(character, monkey_map, cube)

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

password = 1000 * (1+(character['row']+cube[character['face']].get_vertical_offset())) + \
    4 * (1+(character['column']+cube[character['face']].get_horizontal_offset())) + facing_code

print('The password is: '+str(password))
