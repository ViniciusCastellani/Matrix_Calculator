def printMatrix(matrix1):
    print("\nRESULT")
    for row in matrix1:
        print("[", end=" ")
        for element in row:
                print(element, end=" ")
        print("]")