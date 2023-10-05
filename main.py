import numpy as np
from initializeMatrix import initializeMatrix
from printMatrix import printMatrix
from menu import menu
from calc import *

def main():
    choice = menu()
    
    if choice == '0':
        return
    
    elif choice not in ['6','4','5','7']:
        print("\nMATRIX 1")
        matrix1 = initializeMatrix()
        
        print("\nMATRIX 2")
        matrix2 = initializeMatrix()
        
    else:
        matrix1 = initializeMatrix()
    
    match choice:
            case '1':
                result = add(matrix1, matrix2)
                if result is not None:
                    printMatrix(result)
                else:
                    print("Matrix addition is not possible.")
                    
            case '2':
                result = sub(matrix1, matrix2)
                if result is not None:
                    printMatrix(result)
                else:
                    print("Matrix subtraction is not possible.")
                    
            case '3':
                result = mult(matrix1, matrix2)
                if result is not None:
                    printMatrix(result)
                else:
                    print("Matrix multiplication is not possible.")
            
            case '4':
                constant = int(input("Insert the constant to multiply the matrix: "))
                result = multconst(matrix1, constant)
                if result is not None:
                    printMatrix(result)
                else:
                    print("Invalid constant is not possible.")
                
            case '5':
                result = inverse(matrix1)
                if result is not None:
                    printMatrix(result)
                else:
                    print("Operation not possible.")
            
            case '6':
                result = transpose(matrix1)
                if result is not None:
                    printMatrix(result)
                else:
                    print("Operation not possible.")
            
            case '7':
                result = determinant(matrix1)
                if result is not None:
                    print(f"\nThe determinant of the matrix is = {result:.2f}")
                else:
                    print("Operation not possible.")
          
            
if __name__ == "__main__":
    main()