file_name = "input.txt"

with open(file_name) as in_file:
    lines = [(tuple(line.split(' '))) for line in in_file.read().split('\n')]
    lines = lines[:-1]


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


scores = sum(map(score_calculator, lines))
print(scores)
