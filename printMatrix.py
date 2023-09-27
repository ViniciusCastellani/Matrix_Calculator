def printMatrix(matrix1):
    for row in matrix1:
        print("[", end=" ")
        for element in row:
                print("", end = " ")
                print(element, end=" ")
        print("]")