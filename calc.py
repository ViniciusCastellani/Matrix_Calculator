import numpy as np

def add(matrix1, matrix2):
    try:
        return matrix1 + matrix2
    except ValueError:
        return None

def sub(matrix1,matrix2):
    try:
        return matrix1 - matrix2
    except ValueError:
        return None

def mult(matrix1,matrix2):
    try:
        return np.matmul(matrix1,matrix2)
    except ValueError:
        return None

def multconst(matrix1,constant):
    try:
        return constant * matrix1
    except ValueError:
        return None

def inverse(matrix1):
    try:
        return np.linalg.inv(matrix1)
    except ValueError:
        return None

def transpose(matrix1):
    try:
        return matrix1.transpose()
    except ValueError:
        return None

def determinant(matrix1):
    try:
        return np.linalg.det(matrix1)
    except ValueError:
        return None
