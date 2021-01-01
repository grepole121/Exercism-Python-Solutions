color_dict = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
    }


def value(colors):
    resistance = ""
    for col in colors[0:2]:
        resistance += str(color_dict[col])
    return int(resistance)