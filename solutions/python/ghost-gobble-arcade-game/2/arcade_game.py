"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.
    Parameters:
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Can a ghost be eaten?

    """

    can_eat_ghost = power_pellet_active and touching_ghost
    return can_eat_ghost



def score(touching_power_pellet, touching_dot):
    """
    logic: when pacman touches p_p or dot he scores
    parameters: touching_power_pellet, touching_dot
    """

    scored = touching_dot or touching_power_pellet
    return scored


def lose(power_pellet_active, touching_ghost):
    """
    logic: if pacman touches ghost without power pellet, he loses
    parameters: power_pellet_active, touching_ghost
    
    """

    pacman_lost = not power_pellet_active and touching_ghost
    return pacman_lost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    Parameters:
        has_eaten_all_dots (bool): Has the player "eaten" all the dots?
        power_pellet_active (bool): Does the player have an active power pellet?
        touching_ghost (bool): Is the player touching a ghost?

    Returns:
        bool: Has the player won the game?
    """

    pacman_won = has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
    return pacman_won
