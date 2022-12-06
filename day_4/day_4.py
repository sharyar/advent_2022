input_file = "input.txt"

with open(input_file) as infile:
    lines = infile.read().split('\n')
    lines = lines[:-1]


def overlap_counter(pair: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    pair_1, pair_2 = pair

    if pair_1[0] <= pair_2[0] and pair_1[1] >= pair_2[1]:
        return True
    elif pair_2[0] <= pair_1[0] and pair_2[1] >= pair_1[1]:
        return True
    return False


def pair_parser(pair: str) -> tuple[tuple[int, int], tuple[int, int]]:
    pair_1, pair_2 = pair.split(',', maxsplit=2)

    pair_1 = pair_1.split('-')
    pair_1 = int(pair_1[0]), int(pair_1[1])

    pair_2 = pair_2.split('-')
    pair_2 = int(pair_2[0]), int(pair_2[1])

    return pair_1, pair_2


def range_overlapping(x, y):
    if x.start == x.stop or y.start == y.stop:
        return False
    return x.start <= y.stop and y.start <= x.stop


def overlap_calculator_extra(pair: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    p1, p2 = pair[0]
    m1, m2 = pair[1]

    if p1 <= m1 <= p2:
        return True
    elif p1 <= m2 <= p2:
        return True
    elif m1 <= p1 <= m2 or m1 <= p2 <= m2:
        return True

    return False


pairs = map(pair_parser, lines)
# print(sum(map(overlap_counter, pairs)))

print(sum(map(overlap_calculator_extra, pairs)))

print(lines)
print(pair_parser(lines[0]))
