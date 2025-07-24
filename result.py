


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



