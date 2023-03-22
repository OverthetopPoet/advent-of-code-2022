f = open('input.txt')
rps_guide = f.readlines()
f.close()

total_score = 0
shape_scores = {'X': 1, 'Y': 2, 'Z': 3}
decoded_shapes = {'A': 'rock', 'B': 'paper', 'C': 'scizzors', 'X': 'rock', 'Y': 'paper', 'Z': 'scizzors'}

for game_result in rps_guide:
    game_result = game_result.replace('\n', '')
    total_score += shape_scores[game_result[2]]

    elf_shape = decoded_shapes[game_result[0]]
    my_shape = decoded_shapes[game_result[2]]

    if my_shape == elf_shape:
        total_score += 3
    elif (my_shape == 'rock' and elf_shape == 'scizzors') or (my_shape == 'paper' and elf_shape == 'rock') or (my_shape == 'scizzors' and elf_shape == 'paper'):
        total_score += 6
print('My total score is: '+str(total_score))
