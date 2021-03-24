scores = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}


def score(word):
    result = 0
    for char in word.lower():
        for letters, value in scores.items():
            if char in letters:
                result += value
    return result
