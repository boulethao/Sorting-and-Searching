# MEDIAN OF THREE


def medianOfThree(a, b, c):
    """
    Find median among a, b and c

    @param a: One of the three numbers
    @param b: One of the three numbers
    @param c: One of the three numbers

    @return: the median of the three numbers
    """

    # Hypothesis: b is median, we need to verify:
    # a <= b <= c
    # => (b-a) >= 0 and (c-b) >= 0 => (b-a) * (c-b) >= 0
    # OR
    # c <= b <= a
    # => (b-a) <= 0 and (c-b) <= 0 => (b-a) * (c-b) >= 0

    if (b - a) * (c - b) >= 0:
        return b

    # Hypothesis: a is median, we need to verify:
    # b <= a <= c
    # => (a-b) >= 0 and (c-a) >= 0 => (a-b) * (c-a) >= 0
    # OR
    # c <= a <= b
    # => (a-b) <= 0 and (c-a) <= 0 => (a-b) * (c-a) >= 0

    if (a - b) * (c - a) >= 0:
        return a

    return c
