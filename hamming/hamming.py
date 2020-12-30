def distance(strand_a, strand_b):
    hamd = 0
    if len(strand_a) != len(strand_b):
        raise ValueError(".+")

    for a,b in zip(strand_a, strand_b):
        if a!=b:
            hamd+=1

    return hamd