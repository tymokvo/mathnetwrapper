"""
A wrapper for MathNet.Numerics
https://numerics.mathdotnet.com/api/


Full MathNet.Numerics namespace available as MN

Example:

import mathnetwrapper as mnw

x = mnw.matrix((2, 2), distribution=mnw.MN.Distributions.Normal())

print x
DenseMatrix 2x2-Double
 0.308277 -0.47732
-0.0486687 1.38952

More to come...

"""


"""
from clr import AddReferenceToFileAndPath as addref
mathnet_path = "PATH TO MATHNET FOLDER"
path = "{}\\MathNet.Numerics\\lib\\net40\\MathNet.Numerics.dll".format(mathnet_path)
addref(path)
import MathNet.Numerics as MN
"""
### This is primarily for use with pyRevit. If using as a standard Python lib, uncomment above, edit mathnet_path, comment out below
from pyrevit.coreutils.mathnet import MathNet
MN = MathNet.Numerics
from System import Array


### .NET to Python aliases
mnDoubleVector = MN.LinearAlgebra.Double.Vector.Build.DenseOfArray
mnDoubleMatrix = MN.LinearAlgebra.Double.DenseMatrix


### Wrapper functions TODO: just inherit from the .NET class
def vector(input_list):
    """
    Turn a Python List into a vector of Doubles

    x = [1, 2, 3, 4] # a python list

    x = vector(x)

    print x
    DenseVector 4 Double
    1
    2
    3
    4
    """
    arr = Array[float](input_list)
    return mnDoubleVector(arr)


def matrix((rows, columns), input_list=None, fill_value=None, distribution=None):
    """
    Turn a Python List into a matrix of Doubles (Column-major order)

    x = [1, 2, 3, 4] # a python list

    x = matrix(x)

    print x
    DenseMatrix 2x2-Double
    1 3
    2 4
    """

    if input_list != None:
        assert(len(input_list) == rows * columns, "Matrix rank must equal input list length")
        arr = Array[float](input_list)
        matrix = mnDoubleMatrix(rows, columns, arr)
        return matrix

    if fill_value != None:
        matrix = mnDoubleMatrix.Create(rows, columns, fill_value)
        return matrix

    if distribution != None:
        matrix = mnDoubleMatrix.CreateRandom(rows, columns, distribution)
        return matrix


def list_transpose_stack(input_list):
    """
    Transpose row-major python list of lists into column-major for MathNet matrix

    a = [1, 2, 3, 4]
    b = [a, a[::-1]]

    c = mnw.matrix((2, 4), input_list=mnw.list_transpose_stack(b))

    print b, c
    [[1, 2, 3, 4], [4, 3, 2, 1]]
    DenseMatrix 2x4-Double
    1 2 3 4
    4 3 2 1
    """

    out = map(list, zip(*input_list))

    out = itertools.chain(*out)

    return [i for i in out]
