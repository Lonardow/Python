def fatorial(num, show=False):
    """_summary_

    Args:
        num (int): O numero a ser calculado
        show (bool, optional): Mostrar ou não a conta. Defaults to False.

    Returns:
        int: O valor do fatorial de um numero n
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
    return f


print(fatorial(6, True))
