class MatrixError(Exception):
    """ An exception class for Matrix """
    pass


class Matrix:
    """ A simple Python matrix class with
    basic operations and operator overloading """

    def __init__(self, height, width):
        self.rows = [[0] * width for _ in range(height)]
        self.height = height
        self.width = width

    def __getitem__(self, line):
        return self.rows[line]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def get_rank(self):
        return self.height, self.width

    def __add__(self, mat):
        """ Add a matrix to this matrix and
        return the new matrix. Doesn't modify
        the current matrix """

        if self.get_rank() != mat.get_rank():
            raise MatrixError

        ret = Matrix(self.height, self.width)

        for x in range(self.height):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    def __iadd__(self, mat):
        """ Add a matrix to this matrix.
        This modifies the current matrix """

        # Calls __add__
        tempmat = self + mat
        self.rows = tempmat.rows[:]
        return self

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            """ Multiply a matrix with number"""
            new_matrix = Matrix(self.height, self.width)
            for x in range(self.height):
                row = [other * item for item in self.rows[x]]
                new_matrix[x] = row
            return new_matrix

    def read_matrix(self):
        """ Read a matrix line from standard input """
        for x in range(self.height):
            self.rows[x] = list(map(int, input().strip().split()))


if __name__ == '__main__':
    rows, cols = map(int, input().split())
    A = Matrix(rows, cols)
    A.read_matrix()
    dims = list(map(int, input().split()))
    if len(dims) == 1:
        B = A * dims[0]
        print(B)
    elif len(dims) == 2:
        print('ERROR')
