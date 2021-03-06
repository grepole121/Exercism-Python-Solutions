def find_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        if sorted(candidate.lower()) == sorted(word.lower()) and candidate.lower() != word.lower():
            anagrams.append(candidate)
    return anagrams
