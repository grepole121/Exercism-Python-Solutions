import string


def is_valid(isbn):
    countdown = 10
    total = 0
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    for char in isbn:
        if char not in (string.digits + "X"):
            return False
        else:
            char = 10 if char == "X" and countdown == 1 else char
            if char == "X" and countdown == 1:
                char = 10
            elif char == "X" and countdown != 1:
                return False
            total += int(char) * countdown
            countdown -= 1
    return not total % 11