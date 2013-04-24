def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """

    # error if the bus is full (e.g., 50, 100, 150) or empty (0) but all other values should work.
    return (n // 50) + 1

