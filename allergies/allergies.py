allergy = ["eggs", "peanuts", "shellfish", "strawberries",
           "tomatoes", "chocolate", "pollen", "cats"]


class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        if item in self.lst:
            return True
        return False

    @property
    def lst(self):
        list = []
        binary_score = format(self.score, "#010b")[2:]
        for i in range(1, 9):
            if int(binary_score[-i]):
                list.append(allergy[i-1])

        return list
