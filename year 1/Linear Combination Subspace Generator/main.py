"""
Name: MARTA RARES
Group: 1012
Description:
(2^n-1)(2^n-2)(2^n-4) ... (2^n-2^(k-1)) / (2^k-1)(2^k-2)(2^k-4) ... (2^k-2^(k-1))
<x1,x2,x3,...,xn> = <y1,y2,y3,...,yn> only if all y's can be both written as linear combinations of x's.
Using this principle my algorithm generates all linear combinations of previous vectors and
checks upon this if a basis generates a new subspace.
"""

from formula import *
import math

n = int(input("N: "))
k = int(input("K: "))

#1. K dim subspaces
TotalN = 1
TotalK = 1

MaxN = 2 ** n
MaxK = 2 ** k

index = 0

while index < k:
    CurrentI = 2 ** index

    TotalN *= (MaxN - CurrentI)
    TotalK *= (MaxK - CurrentI)

    index+=1

print("K dimensional subspaces: ", int(TotalN/TotalK))

#2. Generate basis

ZVectors,matrix = GenerateZVectors(n,k)

PrevLinearCombs = []

index = 1

def Solve(Matrix, size, ZVectors):
    if size == k:
        IsRight = True

        for Combination in PrevLinearCombs:
            Check = sum(1 for t in Matrix if t in Combination)

            if Check == len(Matrix):
                IsRight = False
                break

        if IsRight:
            NewComb = []
            AllLinearCombinations(Matrix, 0, ZVectors[0], ZVectors, NewComb)

            PrevLinearCombs.append(NewComb)
            
            global index

            print(index)
            for row in Matrix:
                print(row)
            print('\n')

            index += 1 
    else:
        for i in range(len(ZVectors)):
            CurrVecComb = []
            AllLinearCombinations(Matrix, 0, ZVectors[0], ZVectors, CurrVecComb)

            if ZVectors[i] not in CurrVecComb:
                Matrix[size] = ZVectors[i]
                Solve(Matrix.copy(), size + 1, ZVectors)
                Matrix[size] = ZVectors[0]

Solve(matrix, 0, ZVectors)


