def add_all(a: int, b: int, c: int) -> int:
    """
    Adds three integer parameters and returns the sum.
    Args:
        a (int): First integer
        b (int): Second integer
        c (int): Third integer
    Returns:
        int: The sum of a, b, and c
    """
    if not all(isinstance(x, int) for x in (a, b, c)):
        raise TypeError("All parameters must be integers.")
    return a + b + c
