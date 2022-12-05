file_name = "input.txt"

with open(file_name) as in_file:
    lines = in_file.read().splitlines()


def find_common(line):
    half_num = len(line) // 2
    part_a, part_b = line[:half_num], line[half_num:]

    common = set(part_a) & set(part_b)

    return str(list(common)[0])


def score_calculator(input_str: str) -> int:
    if input_str.islower():
        return ord(input_str) - 96
    else:
        return ord(input_str) - 65 + 27


def find_common_badge(input_list: list[str]) -> str:
    common = set(input_list[0]) & set(input_list[1]) & set(input_list[2])
    return str(list(common)[0])


print(sum(map(score_calculator, map(find_common, lines))))

score = 0
for i in range(3, len(lines)+1, 3):
    common = find_common_badge(lines[i-3:i])
    score += score_calculator(common)

print(score)