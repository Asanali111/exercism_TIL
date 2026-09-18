"""fucntions that calculate the number of grains on the chess board"""
def square(number):
    """this function calculates the number of grains on the given square"""
    if number not in range(1,65):
        raise ValueError("square must be between 1 and 64")
    return  2**(number-1)


def total():
    """a function that calculates the total amount of grains on the board"""
    return 2**64 - 1
