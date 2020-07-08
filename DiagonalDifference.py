import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    #n is the size of the matrix // number of rows and columns
    first_diagonal = sum(arr[i][i] for i in range(n))
    second_diagonal = sum(arr[i][n-i-1] for i in range(n))
    return abs(first_diagonal - second_diagonal)

