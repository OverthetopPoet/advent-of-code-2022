f = open('input.txt')
cleanup_pairs = f.readlines()
f.close()

total_overlap_pairs = 0
for pair in cleanup_pairs:
    pair = pair.replace('\n', '')
    areas = pair.split(',')
    elf_1_areas = areas[0].split('-')
    elf_2_areas = areas[1].split('-')
    if (min(elf_1_areas) >= min(elf_2_areas) and max(elf_1_areas) <= max(elf_2_areas)) or (min(elf_2_areas) >= min(elf_1_areas) and max(elf_2_areas) <= max(elf_1_areas)):
        total_overlap_pairs += 1
print(str(total_overlap_pairs)+" Elf pairs have completely overlapping areas.")
