from input_parser import get_puzzle_input
import networkx as nx
import matplotlib.pyplot as plt

mountain_input = get_puzzle_input('input.txt')
mountain_range = []
start_positions = []
end_position = ''
G = nx.DiGraph()
for i in range(len(mountain_input)):
    mountain_row = []
    for j in range(len(mountain_input[i])):
        if mountain_input[i][j] == 'S':
            start_positions.append(str(i)+'_'+str(j))
            mountain_row += 'a'
        elif mountain_input[i][j] == 'E':
            end_position = str(i)+'_'+str(j)
            mountain_row += 'z'
        else:
            mountain_row += mountain_input[i][j]
            if mountain_input[i][j] == 'a':
                start_positions.append(str(i)+'_'+str(j))

    mountain_range.append(mountain_row)

for i in range(len(mountain_range)):
    for j in range(len(mountain_range[i])):
        current_letter = mountain_range[i][j]
        current_letter_pos=str(i)+'_'+str(j)
        if i+1 < len(mountain_range):
            next_letter = mountain_range[i+1][j]
            next_letter_pos = str(i+1)+'_'+str(j)
            #print(current_letter, next_letter)
            if ord(current_letter) >= ord(next_letter):
                G.add_edge(current_letter_pos, next_letter_pos, weight=1)
            if ord(current_letter) == ord(next_letter)-1:
                #print(current_letter,'+1 ==' ,next_letter)
                G.add_edge(current_letter_pos, next_letter_pos, weight=1)

        if j+1 < len(mountain_range[i]):
            next_letter = mountain_range[i][j+1]
            next_letter_pos = str(i)+'_'+str(j+1)

            #print(current_letter, next_letter)
            if ord(current_letter) >= ord(next_letter):
                G.add_edge(current_letter_pos, next_letter_pos, weight=1)
            if ord(current_letter) == ord(next_letter)-1:
                #print(current_letter,'+1 ==' ,next_letter)
                G.add_edge(current_letter_pos, next_letter_pos, weight=1)

        if i!=0:
            next_letter = mountain_range[i-1][j]
            next_letter_pos = str(i-1)+'_'+str(j)
            #print(current_letter, next_letter)
            if ord(current_letter) >= ord(next_letter):
                G.add_edge(current_letter_pos, next_letter_pos, weight=1)
            if ord(current_letter) == ord(next_letter)-1:
                #print(current_letter,'+1 ==' ,next_letter)
                G.add_edge(current_letter_pos, next_letter_pos, weight=1)

        if j!=0:
            next_letter = mountain_range[i][j-1]
            next_letter_pos = str(i)+'_'+str(j-1)
            #print(current_letter, next_letter)
            if ord(current_letter) >= ord(next_letter):
                G.add_edge(current_letter_pos, next_letter_pos, weight=1)
            if ord(current_letter) == ord(next_letter)-1:
                #print(current_letter,'+1 ==' ,next_letter)
                G.add_edge(current_letter_pos, next_letter_pos, weight=1)


#nx.draw(G, with_labels = True)
#plt.savefig("graph_visualization.png")
min_distance=0
for start_position in start_positions:
    try:
        distance = len(nx.shortest_path(G, start_position, end_position, weight="weight"))-1
    except:
        distance = min_distance*1000
    if min_distance ==0:
        min_distance=distance
    elif distance < min_distance:
        min_distance=distance

print('The minimum distance from start to end is: '+str(min_distance))

