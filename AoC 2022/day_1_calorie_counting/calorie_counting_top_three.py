f = open('input.txt')
calorie_lines = f.readlines()
f.close()
calorie_lines.append('')

current_calories = 0
calory_list = []

for calorie in calorie_lines:
    calorie = calorie.replace('\n', '')

    if calorie == '':
        calory_list.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(calorie)

calory_list.sort(reverse=True)
top_elves = 3
total_calories = 0
for i in range(top_elves):
    total_calories += calory_list[i]


print('The top '+str(top_elves)+' elves carry a total of '+str(total_calories)+' calories.')
