f = open('test_input.txt')
rucksacks = f.readlines()
f.close()
priority_sum = 0
elf_groups = []
elf_group = []
for rucksack in rucksacks:
    rucksack = rucksack.replace('\n', '')
    elf_group.append(rucksack)
    if len(elf_group) == 3:
        elf_groups.append(elf_group)
        elf_group = []

for rucksack in elf_groups:

    for letter in rucksack[0]:
        if rucksack[1].find(letter) != -1 and rucksack[2].find(letter) != -1:
            if letter.islower():
                priority_sum += (ord(letter)-96)
            if letter.isupper():
                priority_sum += (ord(letter)-38)
            break

print('The sum of item priorities is: '+str(priority_sum))
