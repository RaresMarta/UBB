# Linear Combination Subspace Generator

This project calculates K-dimensional subspaces and generates linear combinations of vectors, leveraging mathematical principles for efficient subspace generation. It includes algorithms to generate Z vectors and calculate all linear combinations.

## Project Structure

The project is divided into the following files:
- `main.py`: Contains the main program logic to calculate K-dimensional subspaces and generate vector combinations.
- `formula.py`: Provides helper functions used for generating permutations and calculating linear combinations.

## Description

The program calculates K-dimensional subspaces based on the mathematical formula:

$$
\frac{(2^n - 1)(2^n - 2)(2^n - 4) \ldots (2^n - 2^{k-1})}{(2^k - 1)(2^k - 2)(2^k - 4) \ldots (2^k - 2^{k-1})}
$$


It checks if a basis generates a new subspace using linear combinations and vector properties.

### Key Components

- **K Dimensional Subspaces Calculation**: The algorithm calculates K-dimensional subspaces using combinatorial mathematics.
- **Z Vectors Generation**: Generates vectors with binary combinations to serve as a base set for calculations.
- **Linear Combination Checks**: Uses generated vectors to create all possible linear combinations and checks for new subspace generation conditions.

## How to Run

### Prerequisites

- Python 3.x is required to run the project.

### Running the Project

1. Clone this repository to your local system.
2. Run the main program by executing the `main.py` script:

   ```bash
   python main.py

3. Enter values for N and K when prompted. These represent parameters for the subspace calculation.

### Example Usage

N: 3
K: 2
K dimensional subspaces: 3
1
[1, 0, 0]
[0, 1, 0]

2
[1, 0, 0]
[0, 0, 1]

3
[0, 1, 0]
[0, 0, 1]


## Files Description

### `main.py`

- **Calculates K-Dimensional Subspaces**: Using combinatorial formulas, it determines the total number of subspaces.
- **Z Vector and Basis Generation**: Generates Z vectors and iteratively checks for new subspace formations through linear combinations.

### `formula.py`

- **Permutation Function**: Generates permutations of binary vectors.
- **Z Vector Generation**: Creates vectors of a specified length and number of combinations.
- **Linear Combination Functions**: Calculates all linear combinations of input vectors, used to identify new subspaces.
