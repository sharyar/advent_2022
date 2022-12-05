file_name = "input.txt"

with open(file_name) as in_file:
    lines = [(tuple(line.split(' '))) for line in in_file.read().split('\n')]
    lines = lines[:-1]  # removes last line from the list, its empty


def score_calculator(input_tuple: tuple) -> int:
    score_map = {
        'X': 1,  # rock
        'Y': 2,  # paper
        'Z': 3,  # scissors
    }

    return who_won(input_tuple) + score_map[input_tuple[1]]


def who_won(input_tuple: tuple) -> int:
    win_map = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }

    draw_map = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    if input_tuple in win_map.items():
        return 6
    elif input_tuple in draw_map.items():
        return 3
    else:
        return 0


def what_you_choose(input_tuple: tuple) -> tuple:
    win_map = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }

    lose_map = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }

    move_score = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    match input_tuple[1]:
        case 'X':
            return lose_map[input_tuple[0]], 0 + move_score[lose_map[input_tuple[0]]]

        case 'Y':
            return input_tuple[0], 3 + move_score[input_tuple[0]]

        case _:
            return win_map[input_tuple[0]], 6 + move_score[win_map[input_tuple[0]]]


scores = sum(map(score_calculator, lines))
print(scores)

second_scores = map(what_you_choose, lines)

total_score = 0
for score in second_scores:
    total_score += score[1]

print(total_score)
