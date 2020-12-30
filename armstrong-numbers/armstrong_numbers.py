def is_armstrong_number(number):
    digits = [int(d) ** len(str(number)) for d in str(number)]
    if sum(digits) == number:
        return True
    return False
