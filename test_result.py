import pytest

from result import sort


@pytest.mark.parametrize('width, height, length, mass, expected', [
    (10, 10, 10, 10, "STANDARD"),
    (10, 1, 1, 1, "STANDARD"),
    (10, 10, 10, 20, "SPECIAL"),
    (1, 1, 1000000, 20, "REJECTED"),
    (1, 1, 1000000, 21, "REJECTED"),
    (1, 1, 1000000, 10, "SPECIAL"),
    (0, 1, 1000000, 10, "REJECTED"),
    (1, 0, 1000000, 10, "REJECTED"),
    (1, 1, 0, 10, "REJECTED"),
    (1, 1, 1000000, 0, "REJECTED"),
    ('a', 1, 1000000, 0, "REJECTED"),
    (1, 'a', 1000000, 0, "REJECTED"),
    (1, 1, 'a', 0, "REJECTED"),
    (1, 1, 1000000, 'a', "REJECTED"),
])
def test_sort(width, height, length, mass, expected):
    """
    Test the sort function.
    """
    assert sort(width, height, length, mass) == expected
