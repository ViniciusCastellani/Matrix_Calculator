import numpy as np


def initializeMatrix():
    matrix = []

    while True:
        num = input("insert the elements of the row separated by spaces: ").strip()

        try:
            num = num.split(" ")
            row = [float(n) for n in num]

        except ValueError:
            print("You inserted a invalid element in the row")
            continue

        else:
            if len(matrix) > 0 and len(row) != len(matrix[0]):
                print("You didnt input the same ammount of columns")
                continue

            matrix.append(row)

            while True:
                answer = input("Do you want to insert another row? [Y/N] ").upper()
                if answer == "Y":
                    break
                elif answer == "N":
                    return np.array(matrix)
                else:
                    print("Invalid input, please insert a valid letter ")
