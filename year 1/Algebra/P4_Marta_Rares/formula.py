def Permutation(vector, i, ls):
    if i == len(vector):
        ls.append(vector.copy())
    else:
        Permutation(vector.copy(), i + 1, ls)
        vector[i] = 1
        Permutation(vector.copy(), i + 1, ls)
        vector[i] = 0


def GenerateZVectors(n, k):
    Vector = [0] * n
    matrix = [Vector.copy() for _ in range(k)]

    ZVectors = []
    Permutation(Vector, 0, ZVectors)

    return ZVectors, matrix


def AllLinearCombinations(Matrix, Index, LinearComb, ZVectors, AllLinearCombs):
    if Index == len(Matrix):
        AllLinearCombs.append(LinearComb.copy())
    else:
        M1 = [(x + y) % 2 for x, y in zip(LinearComb, Matrix[Index])]
        AllLinearCombinations(Matrix, Index + 1, M1, ZVectors, AllLinearCombs)

        M2 = [(x + y) % 2 for x, y in zip(LinearComb, ZVectors[0])]
        AllLinearCombinations(Matrix, Index + 1, M2, ZVectors, AllLinearCombs)
