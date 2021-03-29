import re


def abbreviate(words):
    out = ""
    words = re.findall(r'[A-Z\']+', words.upper())
    for word in words:
        out += word[0]
    return out
