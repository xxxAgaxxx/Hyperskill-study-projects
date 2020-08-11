import copy


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
        s = '\n'.join([' '.join(['{: f}'.format(item) for item in row]) for row in self.rows])
        return s + '\n'

    def get_rank(self):
        return self.height, self.width

    def main_transpose(self):
        """ Return a transpose of the matrix without
        modifying the matrix itself """

        height, width = self.height, self.width
        mat = Matrix(height, width)
        mat.rows = [list(item) for item in zip(*self.rows)]
        return mat

    def side_transpose(self):
        """ Return a transpose of the matrix without
        modifying the matrix itself """

        height, width = self.height, self.width
        mat = Matrix(height, width)
        mat.rows = [list(item)[::-1] for item in zip(*self.rows)][::-1]
        return mat

    def vertical_transpose(self):
        """ Return a transpose of the matrix without
        modifying the matrix itself """

        height, width = self.height, self.width
        mat = Matrix(height, width)
        mat.rows = [list(item[::-1]) for item in self.rows]
        return mat

    def horizontal_transpose(self):
        """ Return a transpose of the matrix without
        modifying the matrix itself """

        height, width = self.height, self.width
        mat = Matrix(height, width)
        mat.rows = self.rows[::-1]
        return mat

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
        elif isinstance(other, Matrix):
            """ Multiple a matrix with this matrix and
            return the new matrix. Doesn't modify
            the current matrix """

            mat_height, mat_width = other.get_rank()
            if (self.width != mat_height):
                raise MatrixError("Matrices cannot be multipled!")
            mat_t = other.main_transpose()
            mulmat = Matrix(self.height, mat_width)
            for x in range(self.height):
                for y in range(mat_width):
                    mulmat[x][y] = sum([item[0]*item[1] for item in zip(self.rows[x], mat_t[y])])
            return mulmat

    def read_matrix(self, msg=''):
        """ Read a matrix line from standard input """
        if msg:
            print(msg)
        for x in range(self.height):
            self.rows[x] = list(map(float, input().strip().split()))

    def matrix_determinant(self):
        if self.height != self.width:
            raise MatrixError("Cannot calculate determinant for non-square matrix!")
        if self.get_rank() == (1, 1):
            return self.rows[0][0]
        if self.get_rank() == (2, 2):
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]
        total = 0
        for col_id, number in enumerate(self.rows[0]):
            submatrix = Matrix(self.height-1, self.width-1)
            tmp_rows = copy.deepcopy(self.rows)
            tmp_rows = tmp_rows[1:]
            for row in tmp_rows:
                del row[col_id]
            submatrix.rows = tmp_rows
            total += number * pow(-1, col_id) * submatrix.matrix_determinant()
        return total


def select_action():
    first_menu_lvl = '''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
0. Exit
'''
    print(first_menu_lvl)
    selection = input('Your choice: ')
    if selection == '1':
        return 'add'
    elif selection == '2':
        return 'c_mul'
    elif selection == '3':
        return 'mat_mul'
    elif selection == '4':
        transpose_mode = select_transpose()
        if transpose_mode == '1':
            return 'main_trans'
        elif transpose_mode == '2':
            return 'side_trans'
        elif transpose_mode == '3':
            return 'v_trans'
        elif transpose_mode == '4':
            return 'h_trans'
        else:
            return None
    elif selection == '5':
        return 'determinant'
    else:
        return None


def select_transpose():
    transpose_menu = '''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line'''
    print(transpose_menu)
    return input('Your choice: ')


def get_matrix(msg=''):
    rows, cols = map(int, input('Enter matrix size: ').split())
    tmp_matrix = Matrix(rows, cols)
    tmp_matrix.read_matrix(msg)
    return tmp_matrix


if __name__ == '__main__':
    while True:
        action = select_action()
        if not action:
            break
        elif action == 'add':
            A = get_matrix('Enter matrix:')
            B = get_matrix('Enter matrix:')
            try:
                print('The result is:\n', A + B, sep='')
            except MatrixError:
                print('ERROR')
        elif action == 'c_mul':
            A = get_matrix('Enter matrix:')
            const = float(input())
            try:
                print('The result is:\n', A * const, sep='')
            except MatrixError:
                print('ERROR')
        elif action == 'mat_mul':
            A = get_matrix('Enter matrix:')
            B = get_matrix('Enter matrix:')
            try:
                print('The result is:\n', A * B, sep='')
            except MatrixError:
                print('ERROR')
        elif action == 'main_trans':
            A = get_matrix('Enter matrix:')
            try:
                print('The result is:\n', A.main_transpose(), sep='')
            except MatrixError:
                print('ERROR')
        elif action == 'side_trans':
            A = get_matrix('Enter matrix:')
            try:
                print('The result is:\n', A.side_transpose(), sep='')
            except MatrixError:
                print('ERROR')
        elif action == 'v_trans':
            A = get_matrix('Enter matrix:')
            try:
                print('The result is:\n', A.vertical_transpose(), sep='')
            except MatrixError:
                print('ERROR')
        elif action == 'h_trans':
            A = get_matrix('Enter matrix:')
            try:
                print('The result is:\n', A.horizontal_transpose(), sep='')
            except MatrixError:
                print('ERROR')
        elif action == 'determinant':
            A = get_matrix('Enter matrix:')
            try:
                print(A.matrix_determinant())
            except MatrixError:
                print('ERROR')
        else:
            print('Unknown operation')
