def equilateral(sides):
    if not check_if_triangle(sides):
        return False
    elif len(set(sides)) == 1:
        return True
    else:
        return False


def isosceles(sides):
    if not check_if_triangle(sides):
        return False
    elif len(set(sides)) <= 2:
        return True
    else:
        return False


def scalene(sides):
    if not check_if_triangle(sides):
        return False
    elif len(set(sides)) == 3:
        return True
    else:
        return False


def check_if_triangle(sides):
    for side in sides:
        if side <= 0 or side > 0.5*sum(sides):
            return False
    return True
