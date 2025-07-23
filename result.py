import pytest


def sort(width, height, length, mass):
    """
    Sorts objects based on their dimensions and mass.

    This function takes the dimensions and mass of objects as input and
    sorts them accordingly. The sorting criterion or logic can be
    defined within this function.

    Args:
        width (float): Width of the object.
        height (float): Height of the object.
        length (float): Length of the object.
        mass (float): Mass of the object.
    Returns:
        (str): A string indicating the sorted category.
    """
    for item in (width, height, length, mass):
        if not isinstance(item, (int, float)):
            return "REJECTED"
        if item <= 0:
            return "REJECTED"

    MAX_VOLUME = 1000000
    MAX_SIZE = 150
    MAX_MASS = 20

    heavy = mass >= MAX_MASS
    bulky = False

    big_dimension = any(measure >= MAX_SIZE for measure in (width, height, length))
    volume = width * height * length
    if big_dimension or volume >= MAX_VOLUME:
        bulky = True

    if bulky and heavy:
        return "REJECTED"

    if bulky or heavy:
        return "SPECIAL"

    return "STANDARD"


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
