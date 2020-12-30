class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        rows = []
        for i in self.matrix_string.split("\n")[index-1].split(" "):
            rows.append(int(i))
        return rows

    def column(self, index):
        col = []
        for i in range(len(self.matrix_string.split("\n"))):
            col.append(int(self.matrix_string.split("\n")[i].split(" ")[index-1]))
        return col
