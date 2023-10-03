import numpy as np

from initializeMatrix import initializeMatrix
from printMatrix import printMatrix
from menu import menu
from calc import add, sub, mult, multconst


def main():
    choice = menu()
    
    if choice not in ['6','4','5','7']:
        print("\nMATRIX 1")
        matrix1 = initializeMatrix()
        
        print("\nMATRIX 2")
        matrix2 = initializeMatrix()
    
    elif choice == '4':
        matrix1 = initializeMatrix()
        constant = int(input("Insert the constant to multiply the matrix: "))
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
                result = multconst(matrix1, constant)
                printMatrix(result)
                
            case '5':
                pass
            case '6':
                pass
            case '7':
                pass
            
if __name__ == "__main__":
    main()