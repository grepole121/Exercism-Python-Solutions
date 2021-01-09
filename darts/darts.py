import math


def score(x, y):
    distance_from_centre = math.sqrt( (x**2) + (y**2) )
    if distance_from_centre > 10:
        return 0
    elif distance_from_centre > 5:
        return 1
    elif distance_from_centre > 1:
        return 5
    else:
        return 10
