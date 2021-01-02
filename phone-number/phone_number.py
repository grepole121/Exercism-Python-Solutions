import string


class PhoneNumber:
    def __init__(self, number):
        output = list(number)
        invalid_chars = []

        for i in output:
            if (i not in string.digits) or (i == ""):
                invalid_chars.append(i)

        for char in invalid_chars:
            output.remove(char)

        if output[0] == "1":
            output.pop(0)

        if (len(output) != 10) or (output[0] == "1") or (output[0] == "0") or (output[3] == "1") or (output[3] == "0"):
            raise ValueError(".+")
        self.number= ''.join(output)
        self.area_code = self.number[0:3]

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:10]}"
