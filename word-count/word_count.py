import string


def count_words(sentence):
    word_counts = {}
    sentence = sentence.lower()
    punctuation_without_apostrophe = string.punctuation.replace("'", "")
    # Remove all punctuation other than apostrophes and replace with whitespace
    for punc in punctuation_without_apostrophe:
        sentence = sentence.replace(punc, " ")
    # Split string into list
    sentence = sentence.split()

    for word in sentence:
        stripped_word = word
        # Remove all leading apostrophes
        while stripped_word[0] == "'":
            stripped_word = stripped_word[1:]
        # Remove all tailing apostrophes
        while stripped_word[-1] == "'":
            stripped_word = stripped_word[:-1]
        # Create key in word_counts dictionary if it doesn't exist
        if stripped_word not in word_counts:
            word_counts[stripped_word] = 0
        # Increment word key by one
        word_counts[stripped_word] += 1
    return word_counts
