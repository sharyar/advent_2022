import pytest
import day_4


def test_pair_parser_positive():
    initial_pair = "2-4,6-8"
    reformed_pair = ((2, 4), (6, 8))

    assert day_4.pair_parser(initial_pair) == reformed_pair


list_inputs = [
    ((5, 7), (7, 9)),
    ((2, 8), (3, 7)),
    ((6, 6), (4, 7)),
    ((2, 6), (4, 8)),
    ((10, 12), (2, 8)),
    ((1, 4), (5, 6))
]

list_expected = [
    True,
    True,
    True,
    True,
    False,
    False
]


@pytest.mark.parametrize("test_input, expected", [*zip(list_inputs, list_expected)])
def test_overlap_counter(test_input, expected):
    assert day_4.overlap_calculator_extra(test_input) == expected
