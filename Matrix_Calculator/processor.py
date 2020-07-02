class MatrixError(Exception):
    pass

class Matrix:
    def __init__(self, dims):
        self.rows = [[0]*dims[0] for _ in range(dims[1])]
        self.m = dims[0]
        self.n = dims[1]

    def __str__(self):
        string = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return string + '\n'

    def getRank(self):
        return self.m, self.n

    def readLines(self):
        self.rows = [map(int, input().split()) for _ in range(self.n)]

    def __add__(self, other):
        if self.getRank() != other.getRank():
            raise MatrixError
        C = Matrix(m, n)
        for row in range(self.rows):
            C.rows = self.rows[row] + other.rows[row]
        return C


if __name__ == '__main__':
    A = Matrix(list(map(int, input().split())))
    A.readLines()
    B = Matrix(list(map(int, input().split())))
    B.readLines()
    try:
        C = A + B
    except MatrixError:
        print('Error')
