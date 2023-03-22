from input_parser import get_puzzle_input

def drop_sand(cave,start_position):
    #cave[start_position[0]][start_position[1]]='+'
    previous_position=start_position
    down_pos=[previous_position[0]+1,previous_position[1]]
    left_pos=[previous_position[0]+1,previous_position[1]-1]
    right_pos=[previous_position[0]+1,previous_position[1]+1]
    while True:

        if previous_position[0]==len(cave)-1:
            break

        if cave[down_pos[0]][down_pos[1]]==' ':
            previous_position=down_pos
            down_pos=[previous_position[0]+1,previous_position[1]]
            left_pos=[previous_position[0]+1,previous_position[1]-1]
            right_pos=[previous_position[0]+1,previous_position[1]+1]

        elif cave[left_pos[0]][left_pos[1]]==' ':
            previous_position=left_pos
            down_pos=[previous_position[0]+1,previous_position[1]]
            left_pos=[previous_position[0]+1,previous_position[1]-1]
            right_pos=[previous_position[0]+1,previous_position[1]+1]
        elif cave[right_pos[0]][right_pos[1]]==' ':
            previous_position=right_pos
            down_pos=[previous_position[0]+1,previous_position[1]]
            left_pos=[previous_position[0]+1,previous_position[1]-1]
            right_pos=[previous_position[0]+1,previous_position[1]+1]
        else:
            cave[previous_position[0]][previous_position[1]]='o'
            return True

    return False


rock_formations=get_puzzle_input('input.txt')
sand_spawn=[0,500]
rock_positions=[]
max_fall_depth=0
max_formation_width=500

for line in rock_formations:
    line=line.replace(' ','')
    node_points=line.split('->')
    while len(node_points)>=2:
        start_point=[int(node_points[0].split(',')[1]),int(node_points[0].split(',')[0])]
        end_point=[int(node_points[1].split(',')[1]),int(node_points[1].split(',')[0])]

        if start_point[0]>max_fall_depth:
            max_fall_depth=start_point[0]
        if start_point[1]>max_formation_width:
            max_formation_width=start_point[1]
        if end_point[0]>max_fall_depth:
            max_fall_depth=end_point[0]
        if end_point[1]>max_formation_width:
            max_formation_width=end_point[1]

        if start_point[0] != end_point[0]:
            for i in range(min([start_point[0], end_point[0]]), max([start_point[0], end_point[0]])+1):
                rock_positions.append([i,start_point[1]])
        elif start_point[1] != end_point[1]:
            for i in range(min([start_point[1], end_point[1]]), max([start_point[1], end_point[1]])+1):
                rock_positions.append([start_point[0],i])

        node_points.pop(0)

max_fall_depth+=1

cave=[]
for i in range(max_fall_depth+1):
    row=[]
    for j in range(max_formation_width+2):
        row.append(' ')
    cave.append(row)

#print(len(cave),len(cave[0]))

for rock in rock_positions:
    cave[rock[0]][rock[1]]='#'

#for row in cave:
#    print(row[490:])

while drop_sand(cave,sand_spawn):
    pass


#for row in cave:
#    print(row[490:])

sand_pieces=0
for row in cave:
    sand_pieces+=row.count('o')

print(str(sand_pieces)+' pieces of sand come to rest.')