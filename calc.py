import numpy as np

def add(matrix1, matrix2):
    num_elements_matrix1 = len(matrix1[0]) * matrix1
    num_elements_matrix2 = len(matrix2[0]) * matrix2
    
    if num_elements_matrix1 != num_elements_matrix2:
        return None
    else:
        return matrix1 + matrix2

def sub(matrix1,matrix2):
    num_elements_matrix1 = len(matrix1[0]) * matrix1
    num_elements_matrix2 = len(matrix2[0]) * matrix2
    
    if num_elements_matrix1 != num_elements_matrix2:
        return None
    else:
        return matrix1 - matrix2

def mult(matrix1,matrix2):
    num_cols_matrix1 = len(matrix1[0])
    num_rows_matrix2 = len(matrix2)
    
    if num_cols_matrix1 == num_rows_matrix2:
        return np.array(np.matmul(matrix1,matrix2)) 
    else:
        return None

def multconst(matrix1,constant):
    return constant * matrix1

def inverse(matrix1):
    num_cols_matrix1 = len(matrix1[0])
    num_rows_matrix1 = len(matrix1)
    
    if num_cols_matrix1 != num_rows_matrix1:
        pass
