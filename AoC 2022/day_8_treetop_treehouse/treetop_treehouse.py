from input_parser import get_puzzle_input


def calculate_visibility(tree, row, column, forest):
    if tree.get('visible') == None:
        if row == 0 or column == 0 or row == len(forest) or column == len(forest[row]):
            tree.update({'visible': True})
        else:
            tree_height = tree.get('height')
            northern_visibility = True
            southern_visibility = True
            western_visibility = True
            eastern_visibility = True

            for n in range(row):
                if forest[n][column].get('height') >= tree_height:
                    northern_visibility = False
            for s in range(row+1, len(forest)):
                if forest[s][column].get('height') >= tree_height:
                    southern_visibility = False
            for w in range(column):
                if forest[row][w].get('height') >= tree_height:
                    western_visibility = False
            for e in range(column+1, len(forest[row])):
                if forest[row][e].get('height') >= tree_height:
                    eastern_visibility = False

            if northern_visibility or southern_visibility or western_visibility or eastern_visibility:
                tree.update({'visible': True})
            else:
                tree.update({'visible': False})

    return tree


def calculate_scenic_score(tree, row, column, forest):
    north_view = 0
    south_view = 0
    west_view = 0
    east_view = 0

    # if row == 0 or column == 0 or row == len(forest) or column == len(forest[row]):
    #   tree.update({'scenic_score': 0})
    #   return tree

    tree_height = tree.get('height')
    for n in range(row-1, -1, -1):
        north_view += 1
        if forest[n][column].get('height') >= tree_height:
            break
    for s in range(row+1, len(forest)):
        south_view += 1
        if forest[s][column].get('height') >= tree_height:
            break
    for w in range(column-1, -1, -1):
        west_view += 1
        if forest[row][w].get('height') >= tree_height:
            break
    for e in range(column+1, len(forest[row])):
        east_view += 1
        if forest[row][e].get('height') >= tree_height:
            break
    scenic_score = north_view*south_view*west_view*east_view
    tree.update({'scenic_score': scenic_score})
    return tree


forest_input = get_puzzle_input('input.txt')
forest = []

for treeline in forest_input:
    new_treeline = []
    for tree in treeline:
        new_treeline.append({'height': int(tree), 'visible': None})
    forest.append(new_treeline)

for i in range(len(forest)):
    for j in range(len(forest[i])):
        forest[i][j] = calculate_visibility(forest[i][j], i, j, forest)

total_visible = 0
for i in range(len(forest)):
    for j in range(len(forest[i])):
        if forest[i][j].get('visible'):
            total_visible += 1

print('there is a total of '+str(total_visible)+' visible trees.')

for i in range(len(forest)):
    for j in range(len(forest[i])):
        forest[i][j] = calculate_scenic_score(forest[i][j], i, j, forest)

highest_scenic_score = 0
for i in range(len(forest)):
    for j in range(len(forest[i])):
        if forest[i][j].get('scenic_score') > highest_scenic_score:
            highest_scenic_score = forest[i][j].get('scenic_score')
print('The highest scenic score is: '+str(highest_scenic_score))
