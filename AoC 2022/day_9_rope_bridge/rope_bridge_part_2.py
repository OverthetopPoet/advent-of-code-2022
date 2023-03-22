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


def move_tail(tail, head):
    prev_head_pos = head.get('previous_position')
    head_pos = head.get('position')
    tail_pos = tail.get('position')
    prev_tail_pos = deepcopy(tail_pos)
    tail.update({'previous_position': prev_tail_pos})

    if tail_pos[0] == head_pos[0] and tail_pos[1] == head_pos[1]-2:
        tail_pos[1] += 1
    elif tail_pos[0] == head_pos[0] and tail_pos[1] == head_pos[1]+2:
        tail_pos[1] -= 1
    elif tail_pos[1] == head_pos[1] and tail_pos[0] == head_pos[0]-2:
        tail_pos[0] += 1
    elif tail_pos[1] == head_pos[1] and tail_pos[0] == head_pos[0]+2:
        tail_pos[0] -= 1

    else:
        if tail_pos[0] == head_pos[0]-2 or tail_pos[0] == head_pos[0]-1:
            tail_pos[0] += 1
        if tail_pos[0] == head_pos[0]+2 or tail_pos[0] == head_pos[0]+1:
            tail_pos[0] -= 1
        if tail_pos[1] == head_pos[1]-2 or tail_pos[1] == head_pos[1]-1:
            tail_pos[1] += 1
        if tail_pos[1] == head_pos[1]+2 or tail_pos[1] == head_pos[1]+1:
            tail_pos[1] -= 1

    previous_positions = tail.get('previous_positions')
    previous_positions.add(str(tail_pos[0])+'_'+str(tail_pos[1]))
    tail.update({'previous_positions': previous_positions})

    tail.update({'position': tail_pos})
    return tail


def is_touching(head_position, tail_position):
    if ((tail_position[0]+1 == head_position[0] or tail_position[0]-1 == head_position[0] or tail_position[0] == head_position[0])
            and (tail_position[1]+1 == head_position[1] or tail_position[1]-1 == head_position[1] or tail_position[1] == head_position[1])):
        return True
    else:
        return False


def print_position(head_pos, tail):
    x_offset = 11
    y_offset = 5
    grid = []
    for i in range(21):
        row = []
        for j in range(26):
            row.append('.')

        grid.append(row)
    grid[0+y_offset][0+x_offset] = 's'
    for i in range(len(tail)):
        tail_pos = tail[i].get('position')
        grid[tail_pos[1]+y_offset][tail_pos[0]+x_offset] = str(i+1)
    grid[head_pos[1]+y_offset][head_pos[0]+x_offset] = 'H'
    inverse_grid = []
    for row in grid:
        inverse_grid.insert(0, row)

    for row in inverse_grid:
        print(row)


def print_visits(positions):
    x_offset = 11
    y_offset = 5
    grid = []
    for i in range(21):
        row = []
        for j in range(26):
            row.append('.')
        grid.append(row)

    grid[0+y_offset][0+x_offset] = 's'

    for pos in positions:
        grid[pos[1]+y_offset][pos[0]+x_offset] = '#'

    inverse_grid = []
    for row in grid:
        inverse_grid.insert(0, row)

    for row in inverse_grid:
        print(row)


input_file = 'input.txt'
head_moves = get_puzzle_input(input_file)


head = {'position': [0, 0], 'previous_position': [0, 0]}

knots = []
nr_knots = 9
for i in range(nr_knots):
    temp = set()
    temp.add('0_0')
    knot = {'position': [0, 0],
            'previous_position': [0, 0],
            'previous_positions': temp}
    knots.append(knot)

for move in head_moves:
    print(move)
    direction = move.split(' ')[0]
    distance = int(move.split(' ')[1])

    for i in range(distance):
        head = move_head(head, direction)

        for i in range(nr_knots):
            if i == 0:
                if not is_touching(head.get('position'), knots[i].get('position')):
                    knots[i] = move_tail(knots[i], head)

            else:
                if not is_touching(knots[i-1].get('position'), knots[i].get('position')):
                    knots[i] = move_tail(knots[i], knots[i-1])
    #print_position(head.get('position'), knots)

tail_visits = len(knots[len(knots)-1].get('previous_positions'))
positions = []
for pos in knots[len(knots)-1].get('previous_positions'):
    positions.append([int(pos.split('_')[0]), int(pos.split('_')[1])])
# print_visits(positions)

print('The tail visited '+str(tail_visits)+' positions at least once')
