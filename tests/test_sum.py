import pytest

from func.demo_sum import inc


@pytest.mark.parametrize("inputs, expected_output", [
    (3, 4),
    (-1, 0),
    (0.5, 1.5)
]
)
def test_sum(inputs, expected_output):
    assert inc(inputs) == expected_output


def test_sum_error():
    assert inc(0) == 2
