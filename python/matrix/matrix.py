class Matrix:
    def __init__(self, matrix_string):
        # create list, each element representing a row of values
        self.rows = matrix_string.split('\n')
        print(self.rows)
        # split each row into list of integers
        # below works
        # self.matrix = [[int(element) for element in row.split(' ')] for row in self.rows]
        # below works
        # self.matrix = list(map(lambda row: [int(element) for element in row.split()], self.rows))
        # works
        self.matrix = list(map(lambda row: self.makeints(row), self.rows))
        print(self.matrix)

    def makeints(self, row:str):
        """Transforms string of '9 12 800' in list of integers [9, 12, 800]"""
        return [int(element) for element in row.split()]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
