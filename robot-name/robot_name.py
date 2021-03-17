import gc
import random
import string


class Robot:
    def __init__(self):
        self.reset()

    def reset(self):
        random.seed()
        self.name = ""
        letters = "".join(random.choice(string.ascii_uppercase)
                          for _ in range(2))
        digits = "".join(random.choice(string.digits) for _ in range(3))
        name = letters + digits

        for obj in gc.get_objects():
            if isinstance(obj, Robot):
                if (obj.name == name):
                    self.reset()
        self.name = name
