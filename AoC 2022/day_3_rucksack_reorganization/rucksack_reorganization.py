f = open('input.txt')
rucksacks = f.readlines()
f.close()
priority_sum = 0
for rucksack in rucksacks:
    rucksack = rucksack.replace('\n', '')
    first_compartment = rucksack[:int(len(rucksack)/2)]
    second_compartment = rucksack[int(len(rucksack)/2):]

    for letter in first_compartment:
        if second_compartment.find(letter) != -1:
            if letter.islower():
                priority_sum += (ord(letter)-96)
            if letter.isupper():
                priority_sum += (ord(letter)-38)
            break

print('The sum of item priorities is: '+str(priority_sum))
