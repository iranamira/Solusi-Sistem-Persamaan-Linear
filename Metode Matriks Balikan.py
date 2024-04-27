# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qHoreolh0FjoUYrq4StLToyBLQkammxI

Namira Nurfaliani
21120122140135
Metode Numerik - C

Metode Matriks Balikan
"""

import numpy as np

def solve_linear_equation(A, b):

    A_inv = np.linalg.inv(A)
    x = np.dot(A_inv, b)
    return x

A = np.array([[2, 1], [1, -1]])
b = np.array([4, 1])
x = solve_linear_equation(A, b)
print("Solution:", x)

verification = np.allclose(np.dot(A, x), b)
if verification:
    print("Solution verified successfully!")
else:
    print("Solution verification failed!")