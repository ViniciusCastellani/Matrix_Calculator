import numpy as np
from initializeMatrix import initializeMatrix
from printMatrix import printMatrix
from menu import menu
from calc import *

def main():
    answer = " "
    
    while True:
        
        if answer == "N":
            break
        
        choice = menu()
        
        if choice == '0':
            return
        
        elif choice not in ['6','4','5','7'] and answer != "Y":
            print("\nMATRIX 1")
            matrix1 = initializeMatrix()
            
            print("\nMATRIX 2")
            matrix2 = initializeMatrix()
        
        else:
            matrix1 = initializeMatrix()
            
        match choice:
                case '1':
                    if answer == "Y":
                        result = add(result,matrix1)
                    else:    
                        result = add(matrix1, matrix2)
                    
                    if result is not None:
                        printMatrix(result)
                    else:
                        print("Matrix addition is not possible.")
                        
                case '2':
                    if answer == "Y":
                        result = sub(result,matrix1)
                    else:    
                        result = sub(matrix1, matrix2)
                    
                    if result is not None:
                        printMatrix(result)
                    else:
                        print("Matrix subtraction is not possible.")
                        
                case '3':
                    if answer == "Y":
                        result = mult(result,matrix1)
                    else:    
                        result = mult(matrix1, matrix2)
                    
                    if result is not None:
                        printMatrix(result)
                    else:
                        print("Matrix multiplication is not possible.")
                
                case '4':
                    if answer == "Y":
                        constant = int(input("Insert the constant to multiply the matrix: "))
                        result = multconst(result, constant)
                    else:    
                        constant = int(input("Insert the constant to multiply the matrix: "))
                        result = multconst(matrix1, constant)
                    
                    if result is not None:
                        printMatrix(result)
                    else:
                        print("Invalid constant is not possible.")
                    
                case '5':
                    if answer == "Y":
                        result = inverse(result)
                    else:    
                        result = inverse(matrix1)
                    
                    if result is not None:
                        printMatrix(result)
                    else:
                        print("Operation not possible.")
                
                case '6':
                    if answer == "Y":
                        result = transpose(result)
                    else:    
                        result = transpose(matrix1)
                    
                    if result is not None:
                        printMatrix(result)
                    else:
                        print("Operation not possible.")
                
                case '7':
                    if answer == "Y":
                        result = determinant(result)
                    else:    
                        result = determinant(matrix1)
                    
                    if result is not None:
                        print(f"\nThe determinant of the matrix is = {result:.2f}")
                    else:
                        print("Operation not possible.")
        
        while True:
            answer = input("Do you want to calculate another operation using the result? [Y/N] ").upper()
            if answer in ["Y","N"]:
                break
            else:
                print("Invalid input")
    
          
            
if __name__ == "__main__":
    main()