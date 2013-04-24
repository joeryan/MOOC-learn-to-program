def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """

    # determine number of full busses
    full_busses = n//50
    # add an additional bus if a partial bus is needed
    if n%50 > 0:
        full_busses += 1

    return full_busses
    


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    # initialize sum of gains and sum of losses to zero
    sum_gains, sum_losses = 0, 0

    # iterate over list to find gains/losses
    for item in price_changes:
    # if positive, add to sum_gains
        if item > 0:
            sum_gains += item
        else:
            # otherwise it is a zero or a loss, add to sum_losses
            sum_losses += item

    # return results rounded to 10 places to eliminate binary float errors
    return (sum_gains, sum_losses)


def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

    # check for and return the original list of len(1) 
    if len(L) <= 1:
        return
    else:
        tmp_beg, tmp_end = [], []
        # store begining and ending k items temporarily
        for i in range(k):
            tmp_end.append(L.pop())
            tmp_beg.append(L.pop(0))
        # move stored temp saved items to front and end positions
        for i in range(k):
            L.append(tmp_beg.pop(0))
            L.insert(0, tmp_end.pop(0))

        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
