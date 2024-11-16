import numpy as np
import sys

def generate_dijkstra_input(size=100, min_val=0, max_val=100):
    """
    Generate a square matrix of random integers for Dijkstra's algorithm

    Parameters:
    size (int): Dimension of the square matrix
    min_val (int): Minimum value for random integers
    max_val (int): Maximum value for random integers

    Returns:
    numpy.ndarray: Generated matrix
    """
    return np.random.randint(min_val, max_val + 1, size=(size, size))

def save_matrix_to_file(matrix, filename="dijkstra_input.txt"):
    """
    Save the generated matrix to a file

    Parameters:
    matrix (numpy.ndarray): Matrix to save
    filename (str): Output filename
    """
    with open(filename, 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <size>")
        print("Example: python script.py 200")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
        if size <= 0:
            raise ValueError("Size must be positive")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    min_val = 5
    max_val = 100

    matrix = generate_dijkstra_input(size, min_val, max_val)
    save_matrix_to_file(matrix)

    print(f"Generated {size}x{size} matrix and saved to dijkstra_input.txt")

if __name__ == "__main__":
    main()

