f = open('input.txt')
rps_guide = f.readlines()
f.close()

total_score = 0
shape_scores = {'rock': 1, 'paper': 2, 'scizzors': 3}
decoded_shapes = {'A': 'rock', 'B': 'paper', 'C': 'scizzors'}
decoded_outcome = {'X': 0, 'Y': 3, 'Z': 6}

win_shapes = {'rock': 'paper', 'paper': 'scizzors', 'scizzors': 'rock'}
loose_shapes = {'rock': 'scizzors', 'paper': 'rock', 'scizzors': 'paper'}

for game_result in rps_guide:
    game_result = game_result.replace('\n', '')

    elf_shape = decoded_shapes[game_result[0]]
    game_outcome = decoded_outcome[game_result[2]]

    if game_outcome == 0:
        my_shape = loose_shapes[elf_shape]

    elif game_outcome == 3:
        my_shape = elf_shape

    elif game_outcome == 6:
        my_shape = win_shapes[elf_shape]

    total_score = total_score+game_outcome+shape_scores[my_shape]


print('My total score is: '+str(total_score))
