# cdct.pxd
import cython
from libcpp.vector cimport vector

cdef extern from "cdct.h":
    vector[float] calculate_dct2 (const vector[int] X, const int n, const int m)