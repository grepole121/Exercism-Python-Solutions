def largest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError(".+")

    possible_factors = get_possible(min_factor, max_factor)
    possible_factors.sort()
    possible_factors.reverse()

    for num in possible_factors:
        # Check if palindrome
        if num == int(str(num)[::-1]):
            factors = get_factors(min_factor, max_factor, num)
            return (num, factors)
    return (None, [])


def smallest(min_factor, max_factor):
    if max_factor < min_factor:
        raise ValueError(".+")

    possible_factors = get_possible(min_factor, max_factor)
    possible_factors.sort()

    for num in possible_factors:
        # Check if palindrome
        if num == int(str(num)[::-1]):
            factors = get_factors(min_factor, max_factor, num)
            return (num, factors)
    return (None, [])


def get_possible(min_factor, max_factor):
    possible = set()
    for fact1 in range(min_factor, max_factor+1):
        for fact2 in range(min_factor, max_factor+1):
            possible.add(fact1*fact2)
    return list(possible)


def get_factors(min, max, n):
    factors = []
    for i in range(min, max):
        j = n // i
        if (i*j == n) and (min <= j <= max):
            factors.append([i, j])
    return factors
