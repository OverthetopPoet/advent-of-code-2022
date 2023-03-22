f = open('input.txt')
calorie_lines = f.readlines()
f.close()
calorie_lines.append('')

max_calories = 0
max_calory_elf = 0
current_elf = 1
current_calories = 0

for calorie in calorie_lines:
    calorie = calorie.replace('\n', '')

    if calorie == '':
        if current_calories > max_calories:
            max_calories = current_calories
            max_calory_elf = current_elf

        current_elf += 1
        current_calories = 0
    else:
        current_calories += int(calorie)

print('Elf nr. '+str(max_calory_elf)+' has the most calories with '+str(max_calories)+' calories.')
