from collections import deque

elf_energy = deque(map(int, input().split()))
materials = deque(map(int, input().split()))

total_elfs_energy = 0
toys_made = 0
elves_counter = 0
no_more_elves = False
while elf_energy and materials:
    curr_elf = elf_energy.popleft()
    if curr_elf < 5:
        if elf_energy:
            continue
        else:
            no_more_elves = True
            break
    if no_more_elves:
        break

    elves_counter += 1
    curr_materials = materials.pop()

    if elves_counter % 3 == 0:
        twice_energy = curr_materials * 2
        if twice_energy <= curr_elf:
            toys_made += 2
            total_elfs_energy += twice_energy
            curr_elf = (curr_elf - twice_energy) + 1
            elf_energy.append(curr_elf)
            if elves_counter % 5 == 0:
                toys_made -= 2
                curr_elf -= 1
        else:
            materials.append(curr_materials)
            curr_elf *= 2
            elf_energy.append(curr_elf)

    else:
        if curr_materials <= curr_elf:
            toys_made += 1
            total_elfs_energy += curr_materials
            curr_elf = (curr_elf - curr_materials) + 1
            elf_energy.append(curr_elf)
            if elves_counter % 5 == 0:
                toys_made -= 1
                curr_elf -= 1
        else:
            materials.append(curr_materials)
            curr_elf *= 2
            elf_energy.append(curr_elf)


print(f"Toys: {toys_made}")
print(f"Energy: {total_elfs_energy}")
if elf_energy:
    print(f'Elves left: {", ".join(str(elf) for elf in elf_energy)}')