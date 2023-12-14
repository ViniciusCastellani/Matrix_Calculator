# Two-Dimensional Array Calculator in Python

This Python program serves as a two-dimensional array calculator, capable of performing various operations between two-dimensional arrays. It uses NumPy for handling matrix operations and a command-line interface to interact with the user.

## Technologies Used

- **Python**: Programming language used to develop the application.
- **NumPy**: Library for numerical computing in Python.

## Description

The program allows users to perform the following operations between two two-dimensional arrays:

- Addition
- Subtraction
- Multiplication
- Multiplication by a constant
- Matrix Inversion
- Transposition
- Determinant Calculation

### Functionality

- **main**: The main function orchestrates the program flow. It presents a menu for selecting the desired operation and takes user inputs to perform calculations based on the chosen operation.

### Modules

- **initializeMatrix.py**: Module to initialize and input two-dimensional arrays.
- **menu.py**: Module to display the menu of operations and accept user choices.
- **printMatrix.py**: Module to print the resulting matrices or output of operations.
- **calc.py**: Module containing functions to perform array calculations using NumPy operations.

### Matrix Operations

- **add**: Performs addition between two matrices.
- **sub**: Performs subtraction between two matrices.
- **mult**: Performs matrix multiplication between two matrices.
- **multconst**: Multiplies a matrix by a constant value.
- **inverse**: Finds the inverse of a matrix.
- **transpose**: Transposes a matrix.
- **determinant**: Calculates the determinant of a matrix.

## How to Use

Run the Python script, and a command-line interface will prompt you to choose operations and input matrices. Enter your choices based on the menu prompts to perform the desired calculations.

## Usage

To run the program, execute the Python script:

```bash
python main.py
```

**Note:** This assumes the file containing the code is named `main.py`. Adjust the command according to your actual file name if necessary.

Feel free to explore the code and utilize the functionalities to perform various operations on two-dimensional arrays!
