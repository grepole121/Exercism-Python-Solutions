scores = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}
scores_dict = {}
for letters, value in scores.items():
    for letter in letters:
        scores_dict[letter] = value


def score(word):
    return sum(scores_dict[char] for char in word.lower())
