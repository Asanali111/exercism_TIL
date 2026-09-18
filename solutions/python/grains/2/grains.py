"""fucntions that calculate the number of grains on the chess board"""
def square(number):
    """this function calculates the number of grains on the given square"""
    if 1<= number <=64:
        grains_on_this_square = 2**(number - 1)
        return grains_on_this_square
    raise ValueError("square must be between 1 and 64")


def total():
    """fucntion that calculates the total of the grains on the whole table """
    total_grains = 0
    for elements in range (64):
        total_grains += 2**elements
    return total_grains
