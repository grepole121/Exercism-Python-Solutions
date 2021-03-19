import secrets
from string import ascii_lowercase
from itertools import cycle


class Cipher:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = "".join(secrets.choice(ascii_lowercase)
                               for _ in range(100))

    def encode(self, text):
        encoded = []
        for char, key_char in zip(text, cycle(self.key)):
            encoded.append(
                ascii_lowercase[(ord(char) % 97 + ord(key_char) % 97) % 26])
        return "".join(encoded)

    def decode(self, text):
        decoded = []
        for char, key_char in zip(text, cycle(self.key)):
            decoded.append(
                ascii_lowercase[(ord(char) % 97 - ord(key_char) % 97) % 26])
        return "".join(decoded)
