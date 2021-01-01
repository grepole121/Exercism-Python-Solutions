def square(number):
    if number not in range(1,65):
        raise ValueError(".+")
    return 2 ** (number-1)


def total():
    return (2 ** 64) - 1
