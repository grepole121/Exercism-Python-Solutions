import string


def is_isogram(in_string):
    lstring = in_string.lower()
    chars = list(string.ascii_lowercase)
    for i in lstring:
        if (i in chars):
            chars.remove(i)
        elif (i in string.punctuation) or (i in " "):
            pass
        else:
            return False
    return True
