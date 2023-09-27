def initializeMatrix():
    matrix = []
    answer = ""
    
    while True:
        row = []
        
        while True:
            num = input("insert the elements of the row separated by spaces ")
            num = num.split(" ")
            row = [float(n) for n in num]
            
            if len(matrix) > 0 and len(row) != len(matrix[0]) and answer == "Y":
                print("You didnt input the same ammount of columns")
                continue
            
            matrix.append(row)
            
            while True:    
                answer = input("Do you want to insert another row? [Y/N] ").upper()
                if answer == "Y":
                    break
                elif answer == "N":
                    return matrix
                else:
                    print("Invalid input, please insert a valid letter ")

def printMatrix(matrix1):
    for row in matrix1:
        print("[", end=" ")
        for element in row:
                print("", end = " ")
                print(element, end=" ")
        print("]")
        
def main():
    matrix1 = initializeMatrix()
    printMatrix(matrix1)


main()