from collections import defaultdict
import pprint

input_file = "input.txt"

with open(input_file) as in_file:
    lines = in_file.read()

lines = lines.split('\n')

food_dict = defaultdict(list)
elf_counter = 0
heavy_elf = None
highest_food = 0
for line in lines:
    if len(line) > 0:
        food_dict[elf_counter].append(int(line))
    else:
        if sum(food_dict[elf_counter]) > highest_food:
            heavy_elf = elf_counter
            highest_food = sum(food_dict[elf_counter])
        elf_counter += 1

list_food = []
for k, v in food_dict.items():
    list_food.append(sum(v))

print(sum(sorted(list_food)[-3:]))

# pprint.pprint(food_dict)
# print(heavy_elf, '-', highest_food)
#
# top_three = [0, 0, 0]
# running_total = 0
# for line in lines:
#     if len(line) > 0:
#         running_total += int(line)
#     else:
#         running_total = 0
#
#     if running_total > top_three[0]:
#         top_three[0] = running_total
#     elif running_total > top_three[1]:
#         top_three[1] = running_total
#     elif running_total > top_three[2]:
#         top_three[2] = running_total
#
# print(top_three)
# print(sum(top_three))
