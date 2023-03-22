from input_parser import get_puzzle_input


def get_min_distance(current_position, previous_position, start_location=False):
    # print(current_position)
    print_puzzle(current_position)
    mountain_range[current_position[0]][current_position[1]].update({'visited': True})
    distance = 0
    current_letter = mountain_range[current_position[0]][current_position[1]]['letter']
    if current_letter == 'E':
        return 1

    direction_distances = []

    for i in [-1, 1]:
        if can_move_there(current_position, (current_position[0]+i, current_position[1]), previous_position) and i != 0:
            min_dist = get_min_distance((current_position[0]+i, current_position[1]), current_position)
            if min_dist != None:
                direction_distances.append(min_dist)

    for j in [-1, 1]:
        if can_move_there(current_position, (current_position[0], current_position[1]+j), previous_position) and j != 0:
            min_dist = get_min_distance((current_position[0], current_position[1]+j), current_position)
            if min_dist != None:
                direction_distances.append(min_dist)

    #mountain_range[current_position[0]][current_position[1]].update({'visited': False})

    if direction_distances == []:
        mountain_range[current_position[0]][current_position[1]].update({'letter': '.'})
        return None
    else:

        distance = min(direction_distances)

    if start_location:
        return distance
    else:
        return distance+1


def can_move_there(current_position, next_position, previous_position):

    if next_position[0] < 0 or next_position[1] < 0 or next_position[0] >= len(mountain_range) or next_position[1] >= len(mountain_range[0]):
        return False
    if next_position == previous_position:
        return False
    if mountain_range[next_position[0]][next_position[1]]['visited']:
        return False
    next_letter = mountain_range[next_position[0]][next_position[1]]['letter']
    current_letter = mountain_range[current_position[0]][current_position[1]]['letter']

    if next_letter == 'E':
        next_letter = 'z'
    if current_letter == 'S':
        current_letter = 'a'

    if ord(current_letter) == ord(next_letter)-1 or ord(current_letter) == ord(next_letter)+1 or ord(current_letter) == ord(next_letter):
        return True
    else:
        return False


def distance_to_end(position):
    current_mountain = mountain_range[position[0]][position[1]]

    current_distance = current_mountain['distance']

    if current_mountain['letter'] == 'E':
        current_distance = 0
        current_mountain.update({'distance': current_distance})

    if current_distance == None:
        possible_positions = [(position[0]+1, position[1]), (position[0]-1, position[1]),
                              (position[0], position[1]+1), (position[0], position[1]-1)]
        possible_distances = []
        for new_position in possible_positions:

            if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(mountain_range) or new_position[1] >= len(mountain_range[0]):
                break

            new_mountain = mountain_range[new_position[0]][new_position[1]]
            new_letter = new_mountain['letter']
            current_letter = current_mountain['letter']

            if new_letter == 'E':
                new_letter = 'z'
            if current_letter == 'S':
                current_letter = 'a'

            if ord(current_letter) == ord(new_letter)-1 or ord(current_letter) == ord(new_letter)+1 or ord(current_letter) == ord(new_letter):
                possible_distances.append(distance_to_end(new_position))
            else:
                break

        if possible_distances == []:
            current_distance = None
        else:
            current_distance = min(possible_distances)
            current_distance += 1
        current_mountain.update({'distance': current_distance})

    return current_distance


def print_puzzle(position):
    puzzle_board = []

    for i in range(len(mountain_range)):
        mt_row = ''
        for j in range(len(mountain_range[i])):
            if (i, j) != position:
                mt_row += mountain_range[i][j]['letter']
            else:
                mt_row += '#'
        puzzle_board.append(mt_row)

    for row in puzzle_board:
        print(row)
    print('\n\n')


mountain_input = get_puzzle_input('test_input.txt')
mountain_range = []
start_position = 0
for i in range(len(mountain_input)):
    mountain_row = []
    for j in range(len(mountain_input[i])):
        mountain_row.append({'letter': mountain_input[i][j], 'visited': False, 'distance': None})
        if mountain_input[i][j] == 'S':
            start_position = (i, j)
    mountain_range.append(mountain_row)

min_distance = get_min_distance(start_position, start_position, True)

print('The minimum distance from start to end is: '+str(min_distance))
# print_puzzle(start_position)
