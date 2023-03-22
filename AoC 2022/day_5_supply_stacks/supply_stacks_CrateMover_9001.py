def move_boxes(crates, number_of_boxes, source, destination):
    print('move '+str(number_of_boxes)+' from '+str(source)+' to '+str(destination)+'')
    source -= 1
    destination -= 1

    for i in range(number_of_boxes):
        temp = crates[source][0]
        crates[source].pop(0)
        crates[destination].insert(i, temp)
    return crates


def visualize_stack(crates):
    for i in range(len(crates)):
        print(i+1, crates[i])


f = open('input.txt')
cleanup_pairs = f.readlines()
f.close()

instruction_stack = []

crates = []

for row in cleanup_pairs:
    row = row.replace('\n', '')
    if 'move' in row:
        row = row.replace('move ', '')
        row = row.replace(' from ', ';')
        row = row.replace(' to ', ';')
        instruction_stack.append(row.split(';'))

    if '[' in row:
        row = row.replace('   ', '-')
        row = row.replace(' ', '')
        row = row.replace('[', '')
        row = row.replace(']', '')
        print(row)
        if crates == []:
            print('here', len(row))
            for i in range(len(row)):
                crates.append([])
        for i in range(len(row)):
            if row[i] != '-':
                crates[i].append(row[i])

for instruction in instruction_stack:
    crates = move_boxes(crates, int(instruction[0]), int(instruction[1]), int(instruction[2]))


top_letters = ''
for crate in crates:
    top_letters += crate[0]

print('The letters on the topmost crates are: '+top_letters)
