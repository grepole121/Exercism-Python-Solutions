def classify(number):
    aliquot = 0
    if number < 1:
        raise ValueError(".+")
    for i in range(1, number):
        if number % i == 0:
            aliquot += i

    if aliquot == number:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    elif aliquot < number:
        return "deficient"
