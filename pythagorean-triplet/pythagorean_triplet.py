def triplets_with_sum(number):
    triplets = []
    for a in range(0, int(number/2)):
        for b in range(0, int(number/2)):
            c = number - a - b
            if (a*a + b*b == c*c) and (b > a):
                triplets.append([a, b, c])
    return triplets
