from input_parser import get_puzzle_input
from copy import deepcopy


def move_head(head, direction):
    temp = head.get('position')
    prev_head_pos = deepcopy(temp)
    head.update({'previous_position': prev_head_pos})

    if direction == 'R':
        temp[0] += 1
    elif direction == 'U':
        temp[1] += 1
    elif direction == 'L':
        temp[0] -= 1
    elif direction == 'D':
        temp[1] -= 1
    head.update({'position': temp})
    return head


def move_tail(tail, previous_head_pos):
    previous_positions = tail.get('previous_positions')
    previous_positions.add(str(previous_head_pos[0])+'_'+str(previous_head_pos[1]))
    tail.update({'position': previous_head_pos})
    return tail


def is_touching(head_position, tail_position):
    if ((tail_position[0]+1 == head_position[0] or tail_position[0]-1 == head_position[0] or tail_position[0] == head_position[0])
            and (tail_position[1]+1 == head_position[1] or tail_position[1]-1 == head_position[1] or tail_position[1] == head_position[1])):
        return True
    else:
        return False


def print_position(head_pos, tail_pos):
    grid = []
    for i in range(5):
        grid.append(['.', '.', '.', '.', '.', '.'])

    grid[0][0] = 's'
    grid[tail_pos[1]][tail_pos[0]] = 'T'
    grid[head_pos[1]][head_pos[0]] = 'H'
    inverse_grid = []
    for row in grid:
        inverse_grid.insert(0, row)

    for row in inverse_grid:
        print(row)


def print_visits(positions):
    grid = []
    for i in range(5):
        grid.append(['.', '.', '.', '.', '.', '.'])

    grid[0][0] = 's'

    for pos in positions:
        grid[pos[1]][pos[0]] = '#'

    inverse_grid = []
    for row in grid:
        inverse_grid.insert(0, row)

    for row in inverse_grid:
        print(row)


input_file = 'input.txt'
head_moves = get_puzzle_input(input_file)


head = {'position': [0, 0], 'previous_position': [0, 0]}
tail = {'position': [0, 0],
        'previous_position': [0, 0],
        'previous_positions': set()}
tail = move_tail(tail, [0, 0])


if input_file == 'test_input.txt':
    print('== Initial State ==')
    print('\n\n')
    print_position(head.get('position'), tail.get('position'))
    print('\n')


for move in head_moves:
    direction = move.split(' ')[0]
    distance = int(move.split(' ')[1])

    print('== '+move+' ==')

    for i in range(distance):
        head = move_head(head, direction)
        if not is_touching(head.get('position'), tail.get('position')):
            tail = move_tail(tail, head.get('previous_position'))
        if input_file == 'test_input.txt':
            print('\n')
            print_position(head.get('position'), tail.get('position'))
            print('\n')

tail_visits = len(tail.get('previous_positions'))

if input_file == 'test_input.txt':
    positions = []
    for pos in tail.get('previous_positions'):
        positions.append([int(pos.split('_')[0]), int(pos.split('_')[1])])

    print_visits(positions)

print('The tail visited '+str(tail_visits)+' positions at least once')
