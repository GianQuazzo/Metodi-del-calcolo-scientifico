cimport cdct as cd
from libcpp.vector cimport vector 
import numpy as np

def calculate_dct2(const vector[int] X, const int n, const int m):
    return cd.calculate_dct2(X, n, m)

def dct2(X):
    X_shape = np.shape(X)
    return np.reshape(calculate_dct2(np.ravel(X), X_shape[0], X_shape[1]), (X_shape[0],X_shape[1]))