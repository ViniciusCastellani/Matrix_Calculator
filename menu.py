def menu():
    options = {
        '1': 'Sum two matrices',
        '2': 'Subtract two matrices',
        '3': 'Multiply two matrices',
        '4': 'Multiply a matrix by a constant',
        '5': 'Find the inverse of a matrix',
        '6': 'Transpose a matrix',
        '7': 'Calculate the determinant of a matrix',
        '0': 'Exit'
    }
    
    print("Menu:")
    for key, value in options.items():
        print(f"{key}) {value}")

    while True:

        choice = input("Enter your choice: ")

        if choice in options:
            return choice
        else:
            print("Invalid option. Please try again.")