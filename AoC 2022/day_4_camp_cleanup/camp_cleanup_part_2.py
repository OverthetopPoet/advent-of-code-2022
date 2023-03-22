f = open('input.txt')
cleanup_pairs = f.readlines()
f.close()

total_overlap_pairs = 0
for pair in cleanup_pairs:
    pair = pair.replace('\n', '')
    areas = pair.split(',')
    elf_1_areas = areas[0].split('-')
    elf_2_areas = areas[1].split('-')

    elf_1_areas[0] = int(elf_1_areas[0])
    elf_1_areas[1] = int(elf_1_areas[1])
    elf_2_areas[0] = int(elf_2_areas[0])
    elf_2_areas[1] = int(elf_2_areas[1])

    if ((min(elf_1_areas)) >= (min(elf_2_areas)) and (min(elf_1_areas)) <= (max(elf_2_areas))):
        total_overlap_pairs += 1
    elif ((max(elf_1_areas)) >= (min(elf_2_areas)) and (max(elf_1_areas)) <= (max(elf_2_areas))):
        total_overlap_pairs += 1
    elif ((min(elf_2_areas)) >= (min(elf_1_areas)) and (min(elf_2_areas)) <= (max(elf_1_areas))):
        total_overlap_pairs += 1
    elif ((max(elf_2_areas)) >= (min(elf_1_areas)) and (max(elf_2_areas)) <= (max(elf_1_areas))):
        total_overlap_pairs += 1
print(str(total_overlap_pairs)+" Elf pairs have overlapping areas.")
