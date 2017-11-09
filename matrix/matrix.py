import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################

    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")

        # TODO - your code here
        if self.h == 1:
            determinant = self.g[0][0]
        elif self.h == 2:
            determinant = self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]
        return determinant

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    trace += self.g[i][j]
        return trace
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        if self.h == 1:
            m_inverse = (1/self.determinant())*identity(self.h)
        elif self.h == 2:
            m_inverse = (1/self.determinant())*(self.trace()*identity(self.h)-self)
        return m_inverse
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        g = []
        for i in range(self.w):
            row = []
            for j in range(self.h):
                row.append(self.g[j][i])
            g.append(row)
        return Matrix(g)
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if isinstance(other, list):
            other = Matrix(other)
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        #
        # TODO - your code here
        #
        g = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] + other.g[i][j])
            g.append(row)
        return Matrix(g)
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #
        # TODO - your code here
        #
        g = []
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-self.g[i][j])
            g.append(row)
        return Matrix(g)
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #
        # TODO - your code here
        #
        return self + (-other)
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #
        # TODO - your code here
        #
        if isinstance(other, list):
            other = Matrix(other)
        if self.w != other.h:
            raise(ValueError, "Multiplication of Matrix A with matrix B is only possible if the width of A is equal to the height of B")
        result = []
        other = other.T()
        for i in range(self.h):
            row_result = []
            for j in range(other.h):
                dotprodr = 0
                for k in range(self.w):
                    dotprodr += self[i][k]*other[j][k]
                row_result.append(dotprodr)
            result.append(row_result)
        return Matrix(result)
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #
            # TODO - your code here
            #
            mg = zeroes(self.h,self.w)
            for i in range(self.h):
                for j in range(self.w):
                    mg.g[i][j] = other*self.g[i][j]
            return mg
        else:
            return None